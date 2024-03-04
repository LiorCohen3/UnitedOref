document.addEventListener('DOMContentLoaded', function() {
    const sortButton = document.getElementById('sortButton');

    // Function to toggle the sort button class based on sort direction
    const toggleSortButton = (sort_direction) => {
        if (sort_direction === 'up') {
            sortButton.classList.remove('bi-sort-down');
            sortButton.classList.add('bi-sort-up');
        } else {
            sortButton.classList.remove('bi-sort-up');
            sortButton.classList.add('bi-sort-down');
        }
    };

    // Check if sortButton and sort_direction parameter exist in URL
    if (sortButton) {
        const urlParams = new URLSearchParams(window.location.search);
        const sort_direction = urlParams.get('sort_direction');

        // Set initial state of sort button based on sort direction
        if (sort_direction === 'up' || sort_direction === 'down') {
            toggleSortButton(sort_direction);
        }

        // Add click event listener to sortButton
        sortButton.addEventListener('click', function() {
            let newSortDirection = 'down';
            if (sortButton.classList.contains('bi-sort-down')) {
                newSortDirection = 'up';
            }

            // Construct the URL with updated sort direction
            const currentUrl = window.location.href;
            const url = new URL(currentUrl);
            url.searchParams.set('sort_direction', newSortDirection);
            window.location.href = url;
        });
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const applyFilterBtn = document.getElementById('applyFilterBtn');

    applyFilterBtn.addEventListener('click', function() {
        let filters = [];

        // Iterate over all checkboxes in the dropdown menus
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                filters.push(checkbox.value);
            }
        });

        // Build the filter parameters
        let filterParams = '';
        if (filters.length > 0) {
            filterParams = '&filter=' + filters.join('&filter=');
        }

        // Redirect the user to the URL with the selected filter parameters applied
        const currentUrl = window.location.href;
        const url = new URL(currentUrl);
        url.searchParams.delete('filter');
        if (url.searchParams.toString() === '') {
            filterParams = '?' + filterParams.substring(1);
        }
        window.location.href = url + filterParams;
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var submitBtn = document.getElementById('submitBtn');
    if (submitBtn) {
        submitBtn.addEventListener('click', function() {
            var urlParams = new URLSearchParams(window.location.search);
            var selectedOption = urlParams.get('option');

            if (selectedOption === 'option1') {
                window.location = "{% url 'Donation Form' %}";
            } else if (selectedOption === 'option2') {
                window.location = "{% url 'Manual Donation' %}";
            }
        });
    }
});

function handleCardClick(cardId) {
    var card = document.getElementById(cardId);
    card.classList.add('selected-card');

    var allCards = document.querySelectorAll('.card');
    allCards.forEach(function(card) {
        if (card.id !== cardId) {
            card.classList.remove('selected-card');
        }
    });
}

