document.addEventListener("DOMContentLoaded", () => {
    // 1. Menú Hamburguesa Responsivo
    const hamburger = document.getElementById("hamburger");
    const navLinks = document.getElementById("nav-links");

    hamburger.addEventListener("click", () => {
        navLinks.classList.toggle("open");
    });

    document.querySelectorAll(".nav-links a").forEach(link => {
        link.addEventListener("click", () => {
            navLinks.classList.remove("open");
        });
    });

    // 2. Filtro Dinámico de Proyectos
    const pills = document.querySelectorAll(".pill");
    const projectCards = document.querySelectorAll(".project-card");

    pills.forEach(pill => {
        pill.addEventListener("click", () => {
            pills.forEach(p => p.classList.remove("active"));
            pill.classList.add("active");

            const filterValue = pill.getAttribute("data-filter");

            projectCards.forEach(card => {
                if (filterValue === "todos" || card.getAttribute("data-category") === filterValue) {
                    card.style.display = "block";
                } else {
                    card.style.display = "none";
                }
            });
        });
    });

    // 3. Conteo Animado de Métricas
    const counters = document.querySelectorAll(".metric-number");

    const runCounters = () => {
        counters.forEach(counter => {
            const target = +counter.getAttribute("data-target");
            let count = 0;
            const speed = target / 30;

            const updateCount = () => {
                count += speed;
                if (count < target) {
                    counter.innerText = Math.ceil(count);
                    setTimeout(updateCount, 40);
                } else {
                    counter.innerText = target;
                }
            };
            updateCount();
        });
    };

    runCounters();

    // 4. Efecto de inclinación 3D (Tilt Effect)
    const tiltCards = document.querySelectorAll(".tilt-card");

    tiltCards.forEach(card => {
        card.addEventListener("mousemove", (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            card.style.transform = `perspective(1000px) rotateX(${-y / 40}deg) rotateY(${x / 40}deg)`;
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg)";
        });
    });
});