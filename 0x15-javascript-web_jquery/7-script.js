$(function() {
    var $character = $('#character')
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        success: function(character) {
            $character.text(character.name)
        }
    });
});