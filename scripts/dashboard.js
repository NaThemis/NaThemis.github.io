// docs/scripts/dashboard.js
document.addEventListener("DOMContentLoaded", function () {
    const loginWrapper = document.getElementById("admin-login-wrapper");
    // Polling mechanism to wait for Firebase CDNs to load and initialize
    let attempts = 0;
    
    function checkFirebase() {
        attempts++;
        if (window.auth && window.db && typeof window.auth.onAuthStateChanged === 'function') {
            loginError.style.display = "none";
            // Auth State Listener
            window.auth.onAuthStateChanged(user => {
                if (user && user.email === "nat42195nat@gmail.com") {
                    loginWrapper.style.display = "none";
                    dashboardWrapper.style.display = "block";
                    loadDashboardData();
                } else if (user) {
                    window.auth.signOut();
                    loginError.innerText = "Accès refusé. Compte non autorisé.";
                    loginError.style.display = "block";
                } else {
                    loginWrapper.style.display = "block";
                    dashboardWrapper.style.display = "none";
                }
            });

            // Login Action
            document.getElementById("btn-login").addEventListener("click", () => {
                const email = document.getElementById("admin-email").value;
                const password = document.getElementById("admin-password").value;
                window.auth.signInWithEmailAndPassword(email, password).catch(error => {
                    loginError.innerText = error.message;
                    loginError.style.display = "block";
                });
            });

            // Logout Action
            document.getElementById("btn-logout").addEventListener("click", () => {
                window.auth.signOut();
            });

        } else if (attempts < 50) {
            // Check again in 100ms (max 5 seconds)
            setTimeout(checkFirebase, 100);
        } else {
            loginError.innerText = "Firebase mal configuré. Veuillez vérifier firebase-config.js.";
            loginError.style.display = "block";
        }
    }

    checkFirebase();

    function loadDashboardData() {
        const thirtyDaysAgo = new Date();
        thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);

        db.collection("page_views")
            .where("timestamp", ">=", thirtyDaysAgo)
            .orderBy("timestamp", "asc")
            .get()
            .then(snapshot => {
                const views = [];
                snapshot.forEach(doc => {
                    const data = doc.data();
                    if (data.timestamp) {
                        views.push({
                            ...data,
                            date: data.timestamp.toDate()
                        });
                    }
                });
                renderCards(views);
                renderCharts(views);
                renderJourneys(views);
            })
            .catch(err => {
                console.error("Error loading data", err);
                if (err.code === 'permission-denied') {
                    alert("Erreur de permission: Vérifiez les règles de sécurité Firestore.");
                } else if (err.code === 'failed-precondition') {
                    // This often means an index needs to be created
                    console.warn("Index manquant dans Firestore : ", err.message);
                }
            });
    }

    function renderCards(views) {
        document.getElementById("stat-total-views").innerText = views.length;
        const uniqueVisitors = new Set(views.map(v => v.visitor_id)).size;
        document.getElementById("stat-unique-visitors").innerText = uniqueVisitors;

        const twentyFourHoursAgo = new Date();
        twentyFourHoursAgo.setHours(twentyFourHoursAgo.getHours() - 24);
        const recentSessions = new Set(views.filter(v => v.date >= twentyFourHoursAgo).map(v => v.session_id)).size;
        document.getElementById("stat-active-sessions").innerText = recentSessions;
    }

    function renderCharts(views) {
        // Vues par jour
        const viewsByDate = {};
        const pagesCount = {};

        views.forEach(v => {
            // By date
            const dateStr = v.date.toISOString().split('T')[0];
            viewsByDate[dateStr] = (viewsByDate[dateStr] || 0) + 1;

            // By page url
            pagesCount[v.page_url] = (pagesCount[v.page_url] || 0) + 1;
        });

        const dates = Object.keys(viewsByDate).sort();
        const counts = dates.map(d => viewsByDate[d]);

        if (window.viewsChartInstance) window.viewsChartInstance.destroy();
        window.viewsChartInstance = new Chart(document.getElementById('viewsChart'), {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Vues par jour',
                    data: counts,
                    borderColor: '#1b98ff',
                    tension: 0.1,
                    fill: false
                }]
            }
        });

        // Top Pages
        const topPages = Object.entries(pagesCount)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5);

        if (window.topPagesChartInstance) window.topPagesChartInstance.destroy();
        window.topPagesChartInstance = new Chart(document.getElementById('topPagesChart'), {
            type: 'bar',
            data: {
                labels: topPages.map(p => p[0].substring(0, 25) + (p[0].length > 25 ? '...' : '')),
                datasets: [{
                    label: 'Vues globales',
                    data: topPages.map(p => p[1]),
                    backgroundColor: '#ff4081'
                }]
            }
        });
    }

    function renderJourneys(views) {
        // Group by session
        const sessions = {};
        views.forEach(v => {
            if (!sessions[v.session_id]) {
                sessions[v.session_id] = {
                    visitor_id: v.visitor_id,
                    start_date: v.date,
                    pages: []
                };
            }
            sessions[v.session_id].pages.push(v);
        });

        const tbody = document.getElementById("journeys-table-body");
        tbody.innerHTML = "";

        // Sort sessions by date desc
        const sessionArray = Object.values(sessions).sort((a, b) => b.start_date - a.start_date).slice(0, 15);

        if (sessionArray.length === 0) {
            tbody.innerHTML = '<tr><td colspan="4">Aucun parcours récent.</td></tr>';
            return;
        }

        sessionArray.forEach(s => {
            const tr = document.createElement("tr");
            
            // Sort pages by timestamp
            s.pages.sort((a, b) => a.date - b.date);
            const pathHtml = s.pages.map(p => `<span style="background:var(--md-code-bg-color); padding: 2px 6px; border-radius: 4px; font-size: 0.85em; display:inline-block; margin-bottom: 4px;">${p.page_url}</span>`).join(' ➔ ');

            tr.innerHTML = `
                <td>${s.start_date.toLocaleString()}</td>
                <td title="${s.visitor_id}">${s.visitor_id.substring(0,8)}...</td>
                <td title="${s.session_id}">${s.session_id.substring(0,8)}...</td>
                <td class="journey-cell">${pathHtml}</td>
            `;
            tbody.appendChild(tr);
        });
    }
});
