
$("#submit").click(function(){

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        var data = JSON.stringify({
                "country": $('#country').val(),
                "currency": $('#currency').val(),
                "account_holder_name": $('#accountHolderName').val(),
                "account_holder_type": $('#accountHolderType').val(),
                "routing_number": $('#routingNumber').val(),
                "account_number": $('#accountNumber').val(),
                "amount": $('#amount').val()
            })
        $.ajax({
              type: "POST",
              url: "../../api/v1/add-bank/",
              headers: {'X-CSRFToken': csrftoken},
              dataType: 'json',
              contentType: 'application/json',
              data: data,
              success: function(data) {
                    if(data.ok)
                  {
                    $("#errorAlert").removeClass("hide");
                    $("#error").css("transition", "opacity 1s");
                    $("#error").text("Success!");
                    setTimeout(function(){ $("#errorAlert").addClass("hide"); $("#errorAlert").css("transition", "opacity 1s"); }, 8000);
                  }
                 console.log(data);
              },
              error: function(data) {
                  $("#accountNumberError").text(JSON.parse(data.responseText)["account_number"]);
                  $("#accountHolderError").text(JSON.parse(data.responseText)["account_holder_name"]);
                  $("#routingNumberError").text(JSON.parse(data.responseText)["routing_number"]);
                  $("#amountError").text(JSON.parse(data.responseText)["amount"]);

                  setTimeout(function(){
                  $("#accountNumberError").text("");
                  $("#accountHolderError").text("");
                  $("#routingNumberError").text("");
                  $("#amountError").text("");
                  }, 3000);
                  var error = JSON.parse(data.responseText)["message"];
                  var amounterror = JSON.parse(data.responseText)["error"];

                  if(error != null)
                  {
                    $("#errorAlert").removeClass("hide");
                    $("#error").css("transition", "opacity 1s");
                    error = error.slice(47, 84);
                    $("#error").text(error);
                    setTimeout(function(){ $("#errorAlert").addClass("hide"); $("#errorAlert").css("transition", "opacity 1s"); }, 4000);
                  }
                  console.log(data);
              }
        })
});