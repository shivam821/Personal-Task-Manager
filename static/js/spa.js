document.addEventListener('DOMContentLoaded', function() {
    // Get all menu items and pages
    const menuItems = document.querySelectorAll('.menu-item');
    const pages = document.querySelectorAll('.page');

    // Add click event to each menu item
    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            // Remove active class from all menu items and pages
            menuItems.forEach(i => i.classList.remove('active'));
            pages.forEach(page => page.classList.remove('active'));
            
            // Add active class to clicked menu item
            this.classList.add('active');
            
            // Show the corresponding page
            const pageId = this.getAttribute('data-page');
            document.getElementById(pageId).classList.add('active');
            
            // Update URL hash
            window.location.hash = pageId;
        });
    });
    
    // Handle URL hash changes for bookmarking
    window.addEventListener('hashchange', function() {
        const hash = window.location.hash.substring(1);
        if (hash) {
            const targetItem = document.querySelector(`.menu-item[data-page="${hash}"]`);
            if (targetItem) {
                targetItem.click();
            }
        }
    });
    
    // Initialize based on URL hash
    if (window.location.hash) {
        const hash = window.location.hash.substring(1);
        const targetItem = document.querySelector(`.menu-item[data-page="${hash}"]`);
        if (targetItem) {
            targetItem.click();
        }
    }
});

const usernameInput = document.getElementById('input-usernname');
const usernameSavebutton = document.getElementById('save-username-button');
usernameSavebutton.addEventListener("click",(event)=>{
    event.preventDefault();
    sessionStorage.setItem("Username",usernameInput.value);
    let storageUsername1 = sessionStorage.getItem("Username");
    document.getElementById("storageUsername").innerHTML = storageUsername1;
    document.getElementById('input-usernname').value='';
    document.getElementById('name').value = storageUsername1;
});