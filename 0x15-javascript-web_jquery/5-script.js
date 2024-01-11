$(function() {
    $('#add_item').on('click', function() {
        var item = '<li>Item</li>';

        $('UL.my_list').append(item);
    });
});