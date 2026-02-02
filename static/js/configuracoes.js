const toggle = document.getElementById('theme-toggle');
const storedTheme = localStorage.getItem('theme');

if (storedTheme) {
    document.documentElement.setAttribute('data-theme', storedTheme);
    if (toggle) {
        toggle.checked = storedTheme === 'dark';
    }
}

if (toggle) {
    toggle.addEventListener('change', function(e) {
        const theme = e.target.checked ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    });
}