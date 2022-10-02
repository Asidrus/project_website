$(document).ready(function() {
    $('#order').submit(function() {
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success: function(response) {
                $('#order').remove()
                $('.modal-body').append("<p>"+"Order number: "+response.orderID+"</p>"
                +"<p>"+"Order status: "+response.status+"</p>")
                document.getElementById("status-block").style.display = "block"
                $('#order-number').first().text("Number: "+response.orderID)
                $('#order-status').first().text("Status: "+response.status)

//                $('.status-card-body').append("<p id='order-number' class='card-text'>"+"Order number: "+response.orderID+"</p>"
//                +"<p id='order-status' class='card-text'>"+"Order status: "+response.status+"</p>")
                document.cookie = "orderID="+response.orderID
            },
            error: function(e, x, r) {
                alert("error")
            }
        });
        return false;
    });
});