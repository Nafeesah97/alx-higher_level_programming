$(function() {
    var $title = $('UL#list_movies')

    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function(data) {
            $.each(data.results, function(i, item) {
                $title.append('<li> '+ item.title +' </li>');
            })
        }
    })
})