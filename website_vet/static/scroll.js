const vista = new IntersectionObserver((entradas) => {
    entradas.forEach((entrar, index) => {
        if (entrar.isIntersecting) {
            setTimeout(() => {
                entrar.target.classList.add('visible');
            }, index * 100);
        }
    });
})

document.querySelectorAll('.animar').forEach(e => {
    vista.observe(e);
});