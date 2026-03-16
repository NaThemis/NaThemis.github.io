// docs/scripts/firebase-config.js
// using compat libraries
const firebaseConfig = {
    apiKey: "AIzaSyDkWIPAmld1kzTnuTkThwhg4D2xvwddjy4",
    authDomain: "nathaliedecode-website-c8f01.firebaseapp.com",
    projectId: "nathaliedecode-website-c8f01",
    storageBucket: "nathaliedecode-website-c8f01.firebasestorage.app",
    messagingSenderId: "1037992720881",
    appId: "1:1037992720881:web:e4b3e9f3de51750b5aec50",
    measurementId: "G-W22WSG8SSR"
};

// Initialize Firebase only if the config is not the placeholder
var db = null;
var auth = null;

if (firebaseConfig.apiKey !== "YOUR_API_KEY") {
    console.log("[FIREBASE] Initializing Firebase SDK...");
    firebase.initializeApp(firebaseConfig);
    
    db = firebase.firestore();
    auth = firebase.auth();
    
    // Explicitly attach to window for dashboard.js and tracker.js
    window.db = db;
    window.auth = auth;
    console.log("[FIREBASE] Initialization complete. window.auth exists:", !!window.auth);

    // Dispatch a custom event so other scripts know it's ready
    document.dispatchEvent(new Event("firebaseReady"));
} else {
    console.warn("Firebase is not configured yet. Analytics will not be tracked.");
}
