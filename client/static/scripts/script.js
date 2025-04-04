
function get_data() {
    $.getJSON('http://172.20.0.5:9000/', function(data) {
        display = document.getElementsByTagName('textarea')[0]
        display.textContent = 'Ответ сервера: ' + data["response"];
      });
}