$(function() {
    var target = '#news';
    var csvList;
    var insert = '';
    $.ajax({
        url: 'list.csv',
        success: function(data) {
 
            // csv‚ğ”z—ñ‚ÉŠi”[
            csvList = $.csv()(data);
 
            // ‘}“ü‚·‚éHTML‚ğì¬
            for (var i = 1; i < csvList.length; i++) {
                insert += '<li id="' + csvList[i][0] + '">';
                insert += '<div class="image"><img src="' + csvList[i][4] + '" /></div>';
                insert += '<p class="date">' + csvList[i][1] + '</p>';
                insert += '<p class="title">' + csvList[i][2] + '</p>';
                insert += '<p class="sentence">' + csvList[i][3] + '</p>';
                insert += '</li>';
            };
            $(target).append(insert);
        }
    });
});
