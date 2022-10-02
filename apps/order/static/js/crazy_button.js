function choose(btn)
{
    var form = document.getElementById("order")
    if (form != null){
        pizza = btn.getAttribute('data-pizza')
        $('.pizza')[0].value = pizza
        $("#request").remove()
        $("#order").append('<button id="request" type="button" class="btn btn-primary" style="position: relative; z-index: 2;" onclick="$(\'#order\').submit();">Order</button>')
        btn_order = $("#request")
        if (pizza == "Hawaiian"){
            btn_order.on("mouseenter", function(){
                var randX = Math.floor(Math.random() * (window.innerWidth - 100));
                var randY = Math.floor(Math.random() * (window.innerHeight - 100));
                btn_order.stop().animate({"left": randX + "px", "top": randY + "px"});
            })
        }
    }
}