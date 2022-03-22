$(document).ready(function () {
    $('#increment').click(function(){
        var width = $("#container_width");
        var input;
        var input = $("<input>").attr("type","text").attr("name","width[]");
        var br = $("<br>");
        width.append(br);
        width.append(input);
  
        var height = $("#container_height");
        var input = $("<input>").attr("type","text").attr("name","height[]");
        var br = $("<br>");
        height.append(br);
        height.append(input);
    });
    $("#exampleForm").submit(function () {
        alert(JSON.stringify($(this).serialize()));
        return false;
    });
  });

function myFunc() {
    alert("works");
}