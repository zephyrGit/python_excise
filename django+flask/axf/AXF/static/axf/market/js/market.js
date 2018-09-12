$(function () {
    var type_icon_is_down = true;
    $("#all_type").click(function () {
        //
        type_icon_is_down = type_icon_toggle(type_icon_is_down);
        $("#type_containor").toggle();
    })
    $("#type_containor").click(function () {
        $(this).toggle();
        type_icon_is_down = type_icon_toggle(type_icon_is_down);
    })
})
function type_icon_toggle(type_icon_is_down) {
    if (type_icon_is_down){
            $("#type_icon").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
            type_icon_is_down = false;
        } else {
            $("#type_icon").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
            type_icon_is_down = true;
        }
        return type_icon_is_down;
}