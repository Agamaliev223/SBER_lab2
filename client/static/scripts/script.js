
function get_data() {
    $.getJSON('http://172.20.0.5:9000/', function(data) {
        display = document.getElementsByTagName('textarea')[0]
        display.textContent = 'Время на сервере: ' + data["server_time"];
      });
}