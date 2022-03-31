
$("#submit").click(function(){
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        var data = JSON.stringify({
                "card_number": $('#cardNumber').val(),
                "card_holder": $('#cardHolder').val(),
                "card_exp_month": $('#cardExpMonth').val(),
                "card_exp_year": $('#cardExpYear').val(),
                "card_cvv": $('#cardCvv').val(),
                "amount": $('#amount').val()
            })
//                console.log(data);
        $.ajax({
              type: "POST",
              url: "../../api/v1/add-cash/",
              headers: {'X-CSRFToken': csrftoken},
              dataType: 'json',
              contentType: 'application/json',
              data: data,
              success: function(data) {
                   if(data.ok)
                  {
                    $("#errorAlert").removeClass("hide");
                    $("#error").css("transition", "opacity 1s");
                    $("#error").text("Payment Done Successfully!");
                    setTimeout(function(){ $("#errorAlert").addClass("hide"); $("#errorAlert").css("transition", "opacity 1s"); }, 8000);
                  }
              },
              error: function(data) {
                  $("#cardHolderError").text(JSON.parse(data.responseText)["card_holder"]);
                  $("#cardNoError").text(JSON.parse(data.responseText)["card_number"]);
                  $("#cardCvcError").text(JSON.parse(data.responseText)["card_cvv"]);
                  $("#cardExpMonthError").text(JSON.parse(data.responseText)["card_exp_month"]);
                  $("#cardExpYearError").text(JSON.parse(data.responseText)["card_exp_year"]);
                  $("#cardAmountError").text(JSON.parse(data.responseText)["amount"]);
                  setTimeout(function(){
                  $("#cardHolderError").text("");
                  $("#cardNoError").text("");
                  $("#cardCvcError").text("");
                  $("#cardExpMonthError").text("");
                  $("#cardExpYearError").text("");
                  $("#cardAmountError").text("");
                  }, 3000);

                  var error = JSON.parse(data.responseText)["message"];
                  var amounterror = JSON.parse(data.responseText)["error"];

                  if(error != null)
                  {
                    $("#errorAlert").removeClass("hide");
                    $("#error").css("transition", "opacity 1s");
                    $("#error").text(JSON.parse(data.responseText)["message"]);
                    setTimeout(function(){ $("#errorAlert").addClass("hide"); $("#errorAlert").css("transition", "opacity 1s"); }, 4000);
                  }
                  if(amounterror != null && error == null)
                  {
                    $("#errorAlert").removeClass("hide");
                    $("#error").css("transition", "opacity 1s");
                    amounterror = amounterror.slice(27, 500)
                    $("#error").text(amounterror);
                    setTimeout(function(){ $("#errorAlert").addClass("hide"); $("#errorAlert").css("transition", "opacity 1s"); }, 8000);
                  }

              }
        })
});