$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (event) {
      if (event.keyCode === 13) {
        const url = 'https://www.fourtonfish.com/hellosalut/?';
        $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
          $('DIV#hello').html(data.hello);
        });
      }
    });
  });
});
