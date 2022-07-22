odoo.define('us.phonenumber.widget', require => {
    'use strict';

    let FieldChar = require('web.basic_fields').FieldChar;
    let registry = require('web.field_registry');
    let USPhoneNumber = FieldChar.extend({
        events: _.extend({}, FieldChar.prototype.events, {
            'keyup': '_onKeyUp'
        }),
        _onKeyUp: function(e){
            var cleaned = ('' + e.target.value).replace(/\D/g, '');
            var match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
            if (match) {
                e.target.value = '(' + match[1] + ') ' + match[2] + '-' + match[3];
            }
        }
    })
    registry.add("us_phone_number", USPhoneNumber);
    return USPhoneNumber;
});