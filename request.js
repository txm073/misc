window.onload = function (e) {
  const http = new XMLHttpRequest();
  http.open(
    "GET",
    "https://stackoverflow.com/questions/247483/http-get-request-in-javascript"
  );
  http.send();
  http.onload = () => {
    console.log(http.responseText);
  };
};
