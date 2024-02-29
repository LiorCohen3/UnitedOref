document.addEventListener('DOMContentLoaded', function() {
    const sortButton = document.getElementById('sortButton');

    if (sortButton) {
        sortButton.addEventListener('click', function() {
            if (sortButton.classList.contains('bi-sort-down')) {
                sortButton.classList.remove('bi-sort-down');
                sortButton.classList.add('bi-sort-up');
            } else {
                sortButton.classList.remove('bi-sort-up');
                sortButton.classList.add('bi-sort-down');
            }
        });
    }
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

