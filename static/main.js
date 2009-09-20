var bit = 0;

$(function (){
	$("#footer").click(function () {
		
		if($("#content").is(":hidden")) {
			$("#content").slideDown();
		} else {
			$("#content").slideUp();
		}
	});
	
	$("#advance_link").click(function() {
		display = $("#advance").css("display");
		if(display == "none") {
			$("#advance").css({'display':'inline'});
			$("#advance_link").attr("innerText","advance off");
		}
		else {
			$("#advance").css({'display':'none'});
			$("#advance_link").attr("innerText","advance on");
		}
	});
	
	/*$.getJSON("test2.json", function(data) {
		$.each(data.items, function(i,item){
            $("<img/>").attr("id","news").attr("src", item.location).appendTo("#pdf");
        });
	});*/
	
	
	$('form').submit(function(e) {
		e.preventDefault();
		json = {};
		json['topics'] = $('input[name="topics"]').val();
		json['title'] = $('input[name="title"]').val();
		json['numcols'] = $('input[name="column"]').val();
		json['numarts'] = $('input[name="articles"]').val();
	    $.post("gen_news", "json=" + encodeURIComponent($.toJSON(json)), function(data) {
			console.log(data);
			$.each(data, function(i,item){
			    if(i == 0)
				$("<a/>").attr("href", item).text("PDF Download").appendTo("#pdf");
			    else
				$("<img/>").attr("id","news").attr("src", item).appendTo("#pdf");
	        });
	    }, 'json');		
	});
	

	
	
});
