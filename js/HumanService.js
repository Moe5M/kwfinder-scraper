"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});
exports["default"] = void 0;

var _hmacSha = _interopRequireDefault(require("crypto-js/hmac-sha1"));

var _encBase = _interopRequireDefault(require("crypto-js/enc-base64"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

var HumanService = /*#__PURE__*/function () {
    function HumanService() {
        _classCallCheck(this, HumanService);
    }

    _createClass(HumanService, null, [{
        key: "gen",
        value: function gen() {
            var svalue = this.gets();
            var rvalue = this.getu();

            var hvalue = _encBase["default"].stringify((0, _hmacSha["default"])(rvalue, svalue));

            return "".concat(rvalue, "::").concat(hvalue);
        }
    }, {
        key: "gets",
        value: function gets() {
            var a = 'yIHdas83xd2do9obDAS8FNX';
            var b = '4lBdsNANmdsaQ6321DWVb';
            return a + b + 'daspC5eUosr3t1fMBH50'; // eslint-disable-line prefer-template
        }
        /* eslint-disable no-bitwise */

    }, {
        key: "getu",
        value: function getu() {
            var uuid = '';
            var ii;

            for (ii = 0; ii < 32; ii += 1) {
                switch (ii) {
                    case 8:
                    case 20:
                        uuid += '-';
                        uuid += (Math.random() * 16 | 0).toString(16);
                        break;

                    case 12:
                        uuid += '-';
                        uuid += '4';
                        break;

                    case 16:
                        uuid += '-';
                        uuid += (Math.random() * 4 | 8).toString(16);
                        break;

                    default:
                        uuid += (Math.random() * 16 | 0).toString(16);
                }
            }

            return uuid;
        }
        /* eslint-enable no-bitwise */

    }]);

    return HumanService;
}();

var _default = HumanService;
exports["default"] = _default;