document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. Buscador en tiempo real (Client-side) ---
    const searchInput = document.getElementById('searchInput');
    const tableRows = document.querySelectorAll('#dataTable tbody tr');

    searchInput.addEventListener('keyup', (e) => {
        const term = e.target.value.toLowerCase();

        tableRows.forEach(row => {
            if(row.id === 'noResultsRow') return;
            const text = row.textContent.toLowerCase();
            row.style.display = text.includes(term) ? '' : 'none';
        });
    });

    // --- 2. Cambiar Tema (Modo Oscuro / Claro) ---
    const themeBtn = document.getElementById('btnThemeToggle');
    themeBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-bs-theme', newTheme);
        themeBtn.innerHTML = newTheme === 'dark' 
            ? '<i class="fa-solid fa-sun text-warning"></i> Modo' 
            : '<i class="fa-solid fa-moon"></i> Modo';
    });
});

// --- 3. Ordenamiento de Columnas ---
let sortDirection = false;

function sortTable(columnIndex, isNumeric = false) {
    const table = document.getElementById("dataTable");
    const tbody = table.querySelector("tbody");
    const rows = Array.from(tbody.querySelectorAll("tr"));

    // Omitir ordenamiento si es la fila de sin resultados
    if (rows.length === 1 && rows[0].id === 'noResultsRow') return;

    sortDirection = !sortDirection;

    rows.sort((rowA, rowB) => {
        let cellA = rowA.children[columnIndex].innerText.trim();
        let cellB = rowB.children[columnIndex].innerText.trim();

        if (isNumeric) {
            // Limpiar formato de números (comas, letras M, etc.)
            cellA = parseFloat(cellA.replace(/,/g, '').replace(/[^0-9.-]+/g, '')) || 0;
            cellB = parseFloat(cellB.replace(/,/g, '').replace(/[^0-9.-]+/g, '')) || 0;
            return sortDirection ? cellA - cellB : cellB - cellA;
        }

        return sortDirection 
            ? cellA.localeCompare(cellB) 
            : cellB.localeCompare(cellA);
    });

    // Reordenar elementos en el DOM
    rows.forEach(row => tbody.appendChild(row));
}