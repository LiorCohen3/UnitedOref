document.addEventListener('DOMContentLoaded', function() {
    const sortButton = document.getElementById('sortButton');

    sortButton.addEventListener('click', function() {
        if (sortButton.classList.contains('bi-sort-down')) {
            sortButton.classList.remove('bi-sort-down');
            sortButton.classList.add('bi-sort-up');
        } else {
            sortButton.classList.remove('bi-sort-up');
            sortButton.classList.add('bi-sort-down');
        }
    });
});
