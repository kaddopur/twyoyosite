BEGINNER_LIST_LV1 = {'caption': '入門玩家 Lv1', \
                     'start': 1, \
                     'tricks': [['Windmill', '3 reps', '0o3anZdp0Xw'], ['360', 'shoulder', 'oZY8mMsMf1k']]}

TABLE_TEMPLATE = "<table class='table table-condensed table-hover'>
                   <caption><h4></h4></caption>
                   <thead>
                     <tr>
                      <th>編號</th>
                      <th>招式名稱</th>
                      <th>備註</th>
                     </tr>
                   </thead>
                   <tbody>
                   </tbody>
                 </table>"


clickAway = false
isVisible = false

$ ->
  pageSetup()
  
  
pageSetup = ->
  $('#nav_tutorial').addClass('active')
  $('body').attr('data-spy', 'scroll').attr('data-target', '.span3').attr('data-offset', '80')

  # for popovers
  $(document).click (e) ->
    if clickAway and isVisible
      $('.icon-film').popover('hide')
      isVisible = clickAway = false
    else
      clickAway = true

  # Beginner
  $('#beginner ~ .row .span6').html(TABLE_TEMPLATE)
  $('#beginner ~ .row table:last-child h4').text(BEGINNER_LIST_LV1.caption)
  for trick, i in BEGINNER_LIST_LV1.tricks
    $("<tr>
         <td>#{i+BEGINNER_LIST_LV1.start}</td>
         <td>#{trick[0]}</td>
         <td>#{trick[1]}</td>
         <td>
           <a><i class='icon-film icon-large' id='beginner#{i+BEGINNER_LIST_LV1.start}'></i></a>
         </td>
       </tr>").appendTo('#beginner ~ .row table:last-child tbody')
    $("#beginner#{i+BEGINNER_LIST_LV1.start}").popover({'content': "<iframe width='560' height='315' src='http://www.youtube.com/embed/#{trick[2]}?rel=0' frameborder='0' allowfullscreen></iframe>", 'placement': 'bottom', 'trigger': 'manual'}).click (e) ->
      $(this).popover('show')
      clickAway = false
      isVisible = true
      e.preventDefault()

