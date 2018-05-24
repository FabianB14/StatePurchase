$(document).ready(function() {
  var id;
  $('.info_panel').hide();

  $(document).on('click', '.building', function() {
    id = $(this).attr('id');
    $('.info_panel').show();
    $.ajax({
      url: "/data/buildings/" + id,
      method: "GET",
      success: function(data) {
        var obj = JSON.parse(data);
        $('.info_panel h1').text(obj.type);
        var status = "Healthy";
        if (obj.status == 1) {
          status = "Rundown";
        }else if (obj.status == 0){
          status = "Abandoned";
        }
        var ec = "Highly Efficent";
        if (obj.efficency == 1) {
          ec = "Mediocre";
        }else if (obj.efficency == 0){
          ec = "Poor";
        }
        var sz = "Small";
        if (obj.size >= 3 && obj.size < 7) {
          sz = "Medium";
        }else if (obj.size >= 7){
          sz = "Large";
        }
        var html = ""
        html += "<div>Status: "+ status +"</div>";
        html += "<div>Efficency: "+ ec +"</div>";
        html += "<div>Size: "+ sz +"</div>";
        if (obj.status != 2) {
          html += "<a class='fix-button' href='/fix/buildings/"+id+"'>Fix (2.5m)</a>"
        }
        $('.info_panel .content').html(html);
      }
    });
  });

  $('.upgrades_menu_button').click(function() {
    $('.menu_home').hide();
    $('.menu_upgrades').removeClass("hidden");
    return false;
  });

  $('.main_button').click(function() {
    $(this).parent().parent().addClass("hidden");
    $('.menu_home').show();
    return false;
  });

  $('.traffic_upgrades_button').click(function() {
    $(this).parent().parent().addClass("hidden");
    $('.menu_upgrades_traffic').removeClass("hidden");
    return false;
  });

  $('.police_upgrades_button').click(function() {
    $(this).parent().parent().addClass("hidden");
    $('.menu_upgrades_police').removeClass("hidden");
    return false;
  });

  $('.education_upgrades_button').click(function() {
    $(this).parent().parent().addClass("hidden");
    $('.menu_upgrades_education').removeClass("hidden");
    return false;
  });

});
