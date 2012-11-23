if (typeof django !== 'undefined' && django.jQuery) {
	if (typeof $ == 'undefined')
		$ = django.jQuery;
	if (typeof jQuery == 'undefined')
		jQuery = django.jQuery;
}
