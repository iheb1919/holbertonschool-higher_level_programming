$(function () {
    const x = document.getElementById('language_code').value;
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang='+ x ,
    /*success: function(data) {
      $('DIV#hello').append(data.hello);
    }*/
  });
});
