// Toggle the navigation menu on smaller screens
const menuToggle = document.getElementById('menu-toggle');
const navMenu = document.querySelector('header nav ul');

menuToggle.addEventListener('click', () => {
  navMenu.classList.toggle('active');
});
