$(document).ready(function() {
	var searchBlock = $('.header-search-form');
	var first = $('.header_buttons').clone(true);
	var second = $(".header-search-panel").clone(true);
	searchBlock.hide();

	$(document).on("click", "#button_full_search", function() {
		searchBlock.slideToggle(function() {
			if (searchBlock.is(':visible')) {
				// $(".header-search-panel").remove();
				// $('.header_buttons').after(second);


				// $('.header_buttons').css({"order":"1"});
				// $(".header-search-panel").css({"order":"2"});
				// $(".header-search-panel").css({"width": "inherit"});
				$('#words_search').hide();
				$('.header-button-full-search-void-block').show();
			}
			else {
				// $('.header_buttons').remove();
				// $(".header-search-panel").after(first);

				// $('.header_buttons').css({"order":"2"});
				// $(".header-search-panel").css({"order":"1"});
				// $(".header-search-panel").css({"width": "350px"});
				$('#words_search').show();
				$('.header-button-full-search-void-block').hide();
			}
			});
		return false;
	});


	$(window).ready(myFunction);
	$(window).resize(myFunction);

	function myFunction() {
		if ($(window).width() < '665') {

			$(".pagination-block-li-forward").hide();
			$(".pagination-block-li-back").hide();

			if ($(".pagination-block-side-left").length == 0) {
				$(".pagination-block-side-right").css({"width": "100%"});
			}

			else if ($(".pagination-block-side-right").length == 0) {
				$(".pagination-block-side-left").css({"width": "100%"});
			}

			else {

				$(".pagination-block-side-right").css({
					"width": "50%", 
					"border-left": "1px solid #A98C42"
				});

				$(".pagination-block-side-left").css({
					"width": "50%", 
					"border-right": "1px solid #A98C42"
				});

			}
		}

		else {
			
			$(".pagination-block-side-left").css({
				"width": "", 
				"border-right": ""
			});

			$(".pagination-block-side-right").css({
				"width": "", 
				"border-left": ""
			});
			
			$(".pagination-block-li-forward").show();
			$(".pagination-block-li-back").show();
		}
	}

});
