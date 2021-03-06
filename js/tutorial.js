// Generated by CoffeeScript 1.3.3
var BEGINNER_LIST_LV1, TABLE_TEMPLATE, clickAway, isVisible, pageSetup;

BEGINNER_LIST_LV1 = {
  'caption': '入門玩家 Lv1',
  'start': 1,
  'tricks': [['Windmill', '3 reps', '0o3anZdp0Xw'], ['360', 'shoulder', 'oZY8mMsMf1k']]
};

TABLE_TEMPLATE = "<table class='table table-condensed table-hover'>                   <caption><h4></h4></caption>                   <thead>                     <tr>                      <th>編號</th>                      <th>招式名稱</th>                      <th>備註</th>                     </tr>                   </thead>                   <tbody>                   </tbody>                 </table>";

clickAway = false;

isVisible = false;

$(function() {
  return pageSetup();
});

pageSetup = function() {
  var i, trick, _i, _len, _ref, _results;
  $('#nav_tutorial').addClass('active');
  $('body').attr('data-spy', 'scroll').attr('data-target', '.span3').attr('data-offset', '80');
  $(document).click(function(e) {
    if (clickAway && isVisible) {
      $('.icon-film').popover('hide');
      return isVisible = clickAway = false;
    } else {
      return clickAway = true;
    }
  });
  $('#beginner ~ .row .span6').html(TABLE_TEMPLATE);
  $('#beginner ~ .row table:last-child h4').text(BEGINNER_LIST_LV1.caption);
  _ref = BEGINNER_LIST_LV1.tricks;
  _results = [];
  for (i = _i = 0, _len = _ref.length; _i < _len; i = ++_i) {
    trick = _ref[i];
    $("<tr>         <td>" + (i + BEGINNER_LIST_LV1.start) + "</td>         <td>" + trick[0] + "</td>         <td>" + trick[1] + "</td>         <td>           <a><i class='icon-film icon-large' id='beginner" + (i + BEGINNER_LIST_LV1.start) + "'></i></a>         </td>       </tr>").appendTo('#beginner ~ .row table:last-child tbody');
    _results.push($("#beginner" + (i + BEGINNER_LIST_LV1.start)).popover({
      'content': "<iframe width='560' height='315' src='http://www.youtube.com/embed/" + trick[2] + "?rel=0' frameborder='0' allowfullscreen></iframe>",
      'placement': 'bottom',
      'trigger': 'manual',
      'title': '<a class="close" href="#">&times;</a>'
    }).click(function(e) {
      $(this).popover('show');
      clickAway = false;
      isVisible = true;
      return e.preventDefault();
    }));
  }
  return _results;
};
