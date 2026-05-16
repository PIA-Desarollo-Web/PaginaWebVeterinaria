const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            // Retraso escalonado para que aparezcan uno por uno
            setTimeout(() => {
                entry.target.classList.add('visible');
            }, index * 100);
        }
    });
}, {
    threshold: 0.1 // Aparece cuando el 10% del elemento es visible
});

document.querySelectorAll('.animar').forEach(el => {
    observer.observe(el);
});