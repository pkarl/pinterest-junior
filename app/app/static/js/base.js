$(function() {

	$.fn.reverse = [].reverse;

	var pinjr = (function() {

		var app = {};

		app.targetBreakpoint = 0;
		app.timeout = false;

		app.pins = $('.pin');
		app.pin_col_width = $('.pin-col:first').outerWidth();
		app.pinboard = $('.pinboard');
		app.num_cols = 0;


		// this timer method ensures that we only redraw if a new
		// breakpoint has been set, and absorbs fast resizes so we
		// don't trigger a million redraws when a page is resized
		app.timer = function() {

			if (app.timeout) {
				clearTimeout(app.timeout);
			}
			app.timeout = setTimeout(app.redraw, 150, app.targetBreakpoint);

		}

		// this actually re-distributes pin nodes across columns.
		// It's a simplified version of pinterest's behavior
		app.redraw = function(width) {

			// recalculate how many columns we can fit
			app.num_cols = Math.round(width / app.pin_col_width, 0);

			// update the container width to keep columns from floating into 
			// one another during resize
			app.pinboard.css('width', app.num_cols * app.pin_col_width);

			// figure out the distribution of chunks
			var chunkSize = Math.round(app.pins.length / app.num_cols, 0);

			// clone the pins collection so we can splice the shit out of it
			var pins = app.pins.clone();

			// create and destroy pin columns as necessary
			var index = 0;
			while(index++ <= app.num_cols) {
				
				if(app.num_cols > $('.pin-col').length) {
					$('.pinboard').append( '<div class="pin-col"> </div>' );
				} else if( app.num_cols < $('.pin-col').length) {
					$('.pin-col:last').fadeOut("fast").remove();
				}

				$('.pin-col:nth-child(' + index + ')')
					.html('')
					.append( pins.splice(0, chunkSize) )
					.animate({"opacity":"1.0"}, 1000);

			}

		};

		return app;

	}());

	breakpoints([0, 500, 720, 960, 1200, 1440], function(oldP, newP) { 

		pinjr.targetBreakpoint = newP;

		pinjr.timer();

	});

});