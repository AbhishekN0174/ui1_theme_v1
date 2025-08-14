// Glass UI Frontend Entry Point 
console.log("Glass UI loaded successfully!"); 
 
// Add your custom JavaScript here 
frappe.ready(() => { 
    console.log("Glass UI initialized with Frappe"); 
    addGlassEffects(); 
}); 
 
function addGlassEffects() { 
    $(".navbar, .desk-sidebar, .page-card").addClass("glass-effect"); 
    console.log("Glass effects applied"); 
