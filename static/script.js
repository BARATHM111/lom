$(document).ready(function () {
  $("#connect-form").on("submit", function (e) {
    e.preventDefault();
    const data = {
      host: $("#host").val(),
      user: $("#user").val(),
      password: $("#password").val(),
    };
    $.ajax({
      type: "POST",
      url: "/connect",
      contentType: "application/json",
      data: JSON.stringify(data),
      success: function (response) {
        if (response.status === "success") {
          alert(
            "Connected successfully! Databases: " +
              response.databases.join(", ")
          );
        } else {
          alert("Error: " + response.message);
        }
      },
    });
  });

  $("#query-form").on("submit", function (e) {
    e.preventDefault();
    const data = {
      host: $("#host").val(),
      user: $("#user").val(),
      password: $("#password").val(),
      database: $("#database").val(),
      query: $("#query").val(),
    };
    $.ajax({
      type: "POST",
      url: "/query",
      contentType: "application/json",
      data: JSON.stringify(data),
      success: function (response) {
        if (response.status === "success") {
          $("#result").html("<pre>" + response.response + "</pre>");
        } else {
          $("#result").html("<p>Error: " + response.message + "</p>");
        }
      },
    });
  });
});