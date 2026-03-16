document.addEventListener("DOMContentLoaded", function() {
    // 1. Handle GDPR Consent
    const consentKey = "analytics_consent";
    let hasConsent = localStorage.getItem(consentKey);

    if (hasConsent === null) {
        showConsentBanner();
    } else if (hasConsent === "true") {
        initTracking();
    }

    function showConsentBanner() {
        const banner = document.createElement("div");
        banner.id = "gdpr-banner";
        banner.innerHTML = `
            <div class="gdpr-content">
                <p>Nous utilisons des cookies (Firebase) pour analyser le trafic et le parcours utilisateur. Acceptez-vous le suivi anonymisé ?</p>
                <div class="gdpr-buttons">
                    <button id="btn-accept-gdpr" class="md-button md-button--primary">Accepter</button>
                    <button id="btn-refuse-gdpr" class="md-button">Refuser</button>
                </div>
            </div>
        `;
        document.body.appendChild(banner);

        document.getElementById("btn-accept-gdpr").addEventListener("click", () => {
            localStorage.setItem(consentKey, "true");
            banner.remove();
            initTracking();
        });

        document.getElementById("btn-refuse-gdpr").addEventListener("click", () => {
            localStorage.setItem(consentKey, "false");
            banner.remove();
        });
    }

    // 2. Tracking Logic
    function initTracking() {
        if (!window.db) return; // Firebase not configured

        // Generate or retrieve Visitor ID (Persistent across sessions)
        let visitorId = localStorage.getItem("visitor_id");
        if (!visitorId) {
            visitorId = (window.crypto && crypto.randomUUID) ? crypto.randomUUID() : 'v_' + Math.random().toString(36).substr(2, 9);
            localStorage.setItem("visitor_id", visitorId);
        }

        // Generate Session ID (Changes if they close the tab/browser)
        let sessionId = sessionStorage.getItem("session_id");
        if (!sessionId) {
            sessionId = (window.crypto && crypto.randomUUID) ? crypto.randomUUID() : 's_' + Math.random().toString(36).substr(2, 9);
            sessionStorage.setItem("session_id", sessionId);
        }

        const currentUrl = window.location.pathname;
        const timestamp = firebase.firestore.FieldValue.serverTimestamp();

        // Track Page View
        db.collection("page_views").add({
            visitor_id: visitorId,
            session_id: sessionId,
            page_url: currentUrl,
            timestamp: timestamp,
            referrer: document.referrer || "Direct",
            user_agent: navigator.userAgent
        }).catch(err => console.error("Error tracking view", err));

        // Track Link Clicks
        document.addEventListener('click', function(e) {
            const link = e.target.closest('a');
            if (link) {
                db.collection("clicks").add({
                    visitor_id: visitorId,
                    session_id: sessionId,
                    page_url: currentUrl,
                    clicked_url: link.href,
                    link_text: link.innerText || link.title,
                    timestamp: firebase.firestore.FieldValue.serverTimestamp()
                }).catch(err => console.error("Error tracking click", err));
            }
        });
    }
});
