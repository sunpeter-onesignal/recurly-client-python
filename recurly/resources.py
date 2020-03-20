#
# This file is automatically created by Recurly's OpenAPI generation process
# and thus any edits you make by hand will be lost. If you wish to make a
# change to this file, please create a Github issue explaining the changes you
# need and we will usher them to the appropriate places.
from .resource import Resource
import datetime


class Site(Resource):
    """
    Attributes
    ----------
    address : Address
    created_at : datetime
        Created at
    deleted_at : datetime
        Deleted at
    features : :obj:`list` of :obj:`str`
        A list of features enabled for the site.
    id : str
        Site ID
    mode : str
        Mode
    object : str
        Object type
    public_api_key : str
        This value is used to configure RecurlyJS to submit tokenized billing information.
    settings : Settings
    subdomain : str
    updated_at : datetime
        Updated at
    """

    schema = {
        "address": "Address",
        "created_at": datetime,
        "deleted_at": datetime,
        "features": list,
        "id": str,
        "mode": str,
        "object": str,
        "public_api_key": str,
        "settings": "Settings",
        "subdomain": str,
        "updated_at": datetime,
    }


class Address(Resource):
    """
    Attributes
    ----------
    city : str
        City
    country : str
        Country, 2-letter ISO code.
    first_name : str
        First name
    last_name : str
        Last name
    phone : str
        Phone number
    postal_code : str
        Zip or postal code.
    region : str
        State or province.
    street1 : str
        Street 1
    street2 : str
        Street 2
    """

    schema = {
        "city": str,
        "country": str,
        "first_name": str,
        "last_name": str,
        "phone": str,
        "postal_code": str,
        "region": str,
        "street1": str,
        "street2": str,
    }


class Settings(Resource):
    """
    Attributes
    ----------
    accepted_currencies : :obj:`list` of :obj:`str`
    billing_address_requirement : str
        - full:      Full Address (Street, City, State, Postal Code and Country)
        - streetzip: Street and Postal Code only
        - zip:       Postal Code only
        - none:      No Address
    default_currency : str
        The default 3-letter ISO 4217 currency code.
    """

    schema = {
        "accepted_currencies": list,
        "billing_address_requirement": str,
        "default_currency": str,
    }


class Error(Resource):
    """
    Attributes
    ----------
    message : str
        Message
    params : :obj:`list` of :obj:`dict`
        Parameter specific errors
    type : str
        Type
    """

    schema = {"message": str, "params": list, "type": str}


class Account(Resource):
    """
    Attributes
    ----------
    address : Address
    bill_to : str
        An enumerable describing the billing behavior of the account, specifically whether the account is self-paying or will rely on the parent account to pay.
    billing_info : BillingInfo
    cc_emails : str
        Additional email address that should receive account correspondence. These should be separated only by commas. These CC emails will receive all emails that the `email` field also receives.
    code : str
        The unique identifier of the account. This cannot be changed once the account is created.
    company : str
    created_at : datetime
        When the account was created.
    custom_fields : :obj:`list` of :obj:`CustomField`
        The custom fields will only be altered when they are included in a request. Sending an empty array will not remove any existing values. To remove a field send the name with a null or empty value.
    deleted_at : datetime
        If present, when the account was last marked inactive.
    email : str
        The email address used for communicating with this customer. The customer will also use this email address to log into your hosted account management pages. This value does not need to be unique.
    exemption_certificate : str
        The tax exemption certificate number for the account. If the merchant has an integration for the Vertex tax provider, this optional value will be sent in any tax calculation requests for the account.
    first_name : str
    has_active_subscription : bool
        Indicates if the account has an active subscription.
    has_canceled_subscription : bool
        Indicates if the account has a canceled subscription.
    has_future_subscription : bool
        Indicates if the account has a future subscription.
    has_live_subscription : bool
        Indicates if the account has a subscription that is either active, canceled, future, or paused.
    has_past_due_invoice : bool
        Indicates if the account has a past due invoice.
    has_paused_subscription : bool
        Indicates if the account has a paused subscription.
    hosted_login_token : str
        The unique token for automatically logging the account in to the hosted management pages. You may automatically log the user into their hosted management pages by directing the user to: `https://{subdomain}.recurly.com/account/{hosted_login_token}`.
    id : str
    last_name : str
    object : str
        Object type
    parent_account_id : str
        The UUID of the parent account associated with this account.
    preferred_locale : str
        Used to determine the language and locale of emails sent on behalf of the merchant to the customer.
    shipping_addresses : :obj:`list` of :obj:`ShippingAddress`
        The shipping addresses on the account.
    state : str
        Accounts can be either active or inactive.
    tax_exempt : bool
        The tax status of the account. `true` exempts tax on the account, `false` applies tax on the account.
    updated_at : datetime
        When the account was last changed.
    username : str
        A secondary value for the account.
    vat_number : str
        The VAT number of the account (to avoid having the VAT applied). This is only used for manually collected invoices.
    """

    schema = {
        "address": "Address",
        "bill_to": str,
        "billing_info": "BillingInfo",
        "cc_emails": str,
        "code": str,
        "company": str,
        "created_at": datetime,
        "custom_fields": ["CustomField"],
        "deleted_at": datetime,
        "email": str,
        "exemption_certificate": str,
        "first_name": str,
        "has_active_subscription": bool,
        "has_canceled_subscription": bool,
        "has_future_subscription": bool,
        "has_live_subscription": bool,
        "has_past_due_invoice": bool,
        "has_paused_subscription": bool,
        "hosted_login_token": str,
        "id": str,
        "last_name": str,
        "object": str,
        "parent_account_id": str,
        "preferred_locale": str,
        "shipping_addresses": ["ShippingAddress"],
        "state": str,
        "tax_exempt": bool,
        "updated_at": datetime,
        "username": str,
        "vat_number": str,
    }


class ShippingAddress(Resource):
    """
    Attributes
    ----------
    account_id : str
        Account ID
    city : str
    company : str
    country : str
        Country, 2-letter ISO code.
    created_at : datetime
        Created at
    email : str
    first_name : str
    id : str
        Shipping Address ID
    last_name : str
    nickname : str
    object : str
        Object type
    phone : str
    postal_code : str
        Zip or postal code.
    region : str
        State or province.
    street1 : str
    street2 : str
    updated_at : datetime
        Updated at
    vat_number : str
    """

    schema = {
        "account_id": str,
        "city": str,
        "company": str,
        "country": str,
        "created_at": datetime,
        "email": str,
        "first_name": str,
        "id": str,
        "last_name": str,
        "nickname": str,
        "object": str,
        "phone": str,
        "postal_code": str,
        "region": str,
        "street1": str,
        "street2": str,
        "updated_at": datetime,
        "vat_number": str,
    }


class BillingInfo(Resource):
    """
    Attributes
    ----------
    account_id : str
    address : Address
    company : str
    created_at : datetime
        When the billing information was created.
    first_name : str
    fraud : FraudInfo
        Most recent fraud result.
    id : str
    last_name : str
    object : str
        Object type
    payment_method : PaymentMethod
    updated_at : datetime
        When the billing information was last changed.
    updated_by : BillingInfoUpdatedBy
    valid : bool
    vat_number : str
        Customer's VAT number (to avoid having the VAT applied). This is only used for automatically collected invoices.
    """

    schema = {
        "account_id": str,
        "address": "Address",
        "company": str,
        "created_at": datetime,
        "first_name": str,
        "fraud": "FraudInfo",
        "id": str,
        "last_name": str,
        "object": str,
        "payment_method": "PaymentMethod",
        "updated_at": datetime,
        "updated_by": "BillingInfoUpdatedBy",
        "valid": bool,
        "vat_number": str,
    }


class PaymentMethod(Resource):
    """
    Attributes
    ----------
    account_type : str
        The bank account type. Only present for ACH payment methods.
    billing_agreement_id : str
        Billing Agreement identifier. Only present for Amazon or Paypal payment methods.
    card_type : str
        Visa, MasterCard, American Express, Discover, JCB, etc.
    exp_month : int
        Expiration month.
    exp_year : int
        Expiration year.
    first_six : str
        Credit card number's first six digits.
    gateway_code : str
        An identifier for a specific payment gateway.
    gateway_token : str
        A token used in place of a credit card in order to perform transactions.
    last_four : str
        Credit card number's last four digits. Will refer to bank account if payment method is ACH.
    last_two : str
        The IBAN bank account's last two digits.
    object : str
    routing_number : str
        The bank account's routing number. Only present for ACH payment methods.
    routing_number_bank : str
        The bank name of this routing number.
    """

    schema = {
        "account_type": str,
        "billing_agreement_id": str,
        "card_type": str,
        "exp_month": int,
        "exp_year": int,
        "first_six": str,
        "gateway_code": str,
        "gateway_token": str,
        "last_four": str,
        "last_two": str,
        "object": str,
        "routing_number": str,
        "routing_number_bank": str,
    }


class FraudInfo(Resource):
    """
    Attributes
    ----------
    decision : str
        Kount decision
    risk_rules_triggered : dict
        Kount rules
    score : int
        Kount score
    """

    schema = {"decision": str, "risk_rules_triggered": dict, "score": int}


class BillingInfoUpdatedBy(Resource):
    """
    Attributes
    ----------
    country : str
        Country of IP address, if known by Recurly.
    ip : str
        Customer's IP address when updating their billing information.
    """

    schema = {"country": str, "ip": str}


class CustomField(Resource):
    """
    Attributes
    ----------
    name : str
        Fields must be created in the UI before values can be assigned to them.
    value : str
        Any values that resemble a credit card number or security code (CVV/CVC) will be rejected.
    """

    schema = {"name": str, "value": str}


class ErrorMayHaveTransaction(Resource):
    """
    Attributes
    ----------
    message : str
        Message
    params : :obj:`list` of :obj:`dict`
        Parameter specific errors
    transaction_error : TransactionError
        This is only included on errors with `type=transaction`.
    type : str
        Type
    """

    schema = {
        "message": str,
        "params": list,
        "transaction_error": "TransactionError",
        "type": str,
    }


class TransactionError(Resource):
    """
    Attributes
    ----------
    category : str
        Category
    code : str
        Code
    merchant_advice : str
        Merchant message
    message : str
        Customer message
    object : str
        Object type
    three_d_secure_action_token_id : str
        Returned when 3-D Secure authentication is required for a transaction. Pass this value to Recurly.js so it can continue the challenge flow.
    transaction_id : str
        Transaction ID
    """

    schema = {
        "category": str,
        "code": str,
        "merchant_advice": str,
        "message": str,
        "object": str,
        "three_d_secure_action_token_id": str,
        "transaction_id": str,
    }


class AccountAcquisition(Resource):
    """
    Attributes
    ----------
    account : AccountMini
        Account mini details
    campaign : str
        An arbitrary identifier for the marketing campaign that led to the acquisition of this account.
    channel : str
        The channel through which the account was acquired.
    cost : AccountAcquisitionCost
        Account balance
    created_at : datetime
        When the account acquisition data was created.
    id : str
    object : str
        Object type
    subchannel : str
        An arbitrary subchannel string representing a distinction/subcategory within a broader channel.
    updated_at : datetime
        When the account acquisition data was last changed.
    """

    schema = {
        "account": "AccountMini",
        "campaign": str,
        "channel": str,
        "cost": "AccountAcquisitionCost",
        "created_at": datetime,
        "id": str,
        "object": str,
        "subchannel": str,
        "updated_at": datetime,
    }


class AccountAcquisitionCost(Resource):
    """
    Attributes
    ----------
    amount : float
        The amount of the corresponding currency used to acquire the account.
    currency : str
        3-letter ISO 4217 currency code.
    """

    schema = {"amount": float, "currency": str}


class AccountMini(Resource):
    """
    Attributes
    ----------
    bill_to : str
    code : str
        The unique identifier of the account.
    company : str
    email : str
        The email address used for communicating with this customer.
    first_name : str
    id : str
    last_name : str
    object : str
        Object type
    parent_account_id : str
    """

    schema = {
        "bill_to": str,
        "code": str,
        "company": str,
        "email": str,
        "first_name": str,
        "id": str,
        "last_name": str,
        "object": str,
        "parent_account_id": str,
    }


class AccountBalance(Resource):
    """
    Attributes
    ----------
    account : AccountMini
        Account mini details
    balances : :obj:`list` of :obj:`AccountBalanceAmount`
    object : str
        Object type
    past_due : bool
    """

    schema = {
        "account": "AccountMini",
        "balances": ["AccountBalanceAmount"],
        "object": str,
        "past_due": bool,
    }


class AccountBalanceAmount(Resource):
    """
    Attributes
    ----------
    amount : float
        Total amount the account is past due.
    currency : str
        3-letter ISO 4217 currency code.
    """

    schema = {"amount": float, "currency": str}


class CouponRedemption(Resource):
    """
    Attributes
    ----------
    account : AccountMini
        The Account on which the coupon was applied.
    coupon : Coupon
    created_at : datetime
        Created at
    currency : str
        3-letter ISO 4217 currency code.
    discounted : float
        The amount that was discounted upon the application of the coupon, formatted with the currency.
    id : str
        Coupon Redemption ID
    object : str
        Will always be `coupon`.
    removed_at : datetime
        The date and time the redemption was removed from the account (un-redeemed).
    state : str
        Coupon Redemption state
    updated_at : datetime
        Last updated at
    """

    schema = {
        "account": "AccountMini",
        "coupon": "Coupon",
        "created_at": datetime,
        "currency": str,
        "discounted": float,
        "id": str,
        "object": str,
        "removed_at": datetime,
        "state": str,
        "updated_at": datetime,
    }


class Coupon(Resource):
    """
    Attributes
    ----------
    applies_to_all_plans : bool
        The coupon is valid for all plans if true. If false then `plans` and `plans_names` will list the applicable plans.
    applies_to_non_plan_charges : bool
        The coupon is valid for one-time, non-plan charges if true.
    code : str
        The code the customer enters to redeem the coupon.
    coupon_type : str
        Whether the coupon is "single_code" or "bulk". Bulk coupons will require a `unique_code_template` and will generate unique codes through the `/generate` endpoint.
    created_at : datetime
        Created at
    discount : CouponDiscount
        Details of the discount a coupon applies. Will contain a `type`
        property and one of the following properties: `percent`, `fixed`, `trial`.
    duration : str
        - "single_use" coupons applies to the first invoice only.
        - "temporal" coupons will apply to invoices for the duration determined by the `temporal_unit` and `temporal_amount` attributes.
    expired_at : datetime
        The date and time the coupon was expired early or reached its `max_redemptions`.
    free_trial_amount : int
        Sets the duration of time the `free_trial_unit` is for.
    free_trial_unit : str
        Description of the unit of time the coupon is for. Used with `free_trial_amount` to determine the duration of time the coupon is for.
    hosted_page_description : str
        This description will show up when a customer redeems a coupon on your Hosted Payment Pages, or if you choose to show the description on your own checkout page.
    id : str
        Coupon ID
    invoice_description : str
        Description of the coupon on the invoice.
    max_redemptions : int
        A maximum number of redemptions for the coupon. The coupon will expire when it hits its maximum redemptions.
    max_redemptions_per_account : int
        Redemptions per account is the number of times a specific account can redeem the coupon. Set redemptions per account to `1` if you want to keep customers from gaming the system and getting more than one discount from the coupon campaign.
    name : str
        The internal name for the coupon.
    object : str
        Object type
    plans : :obj:`list` of :obj:`PlanMini`
        A list of plans for which this coupon applies. This will be `null` if `applies_to_all_plans=true`.
    plans_names : :obj:`list` of :obj:`str`
        TODO
    redeem_by : datetime
        The date and time the coupon will expire and can no longer be redeemed. Time is always 11:59:59, the end-of-day Pacific time.
    redeemed_at : datetime
        The date and time the unique coupon code was redeemed. This is only present for bulk coupons.
    redemption_resource : str
        Whether the discount is for all eligible charges on the account, or only a specific subscription.
    state : str
        Indicates if the coupon is redeemable, and if it is not, why.
    temporal_amount : int
        If `duration` is "temporal" than `temporal_amount` is an integer which is multiplied by `temporal_unit` to define the duration that the coupon will be applied to invoices for.
    temporal_unit : str
        If `duration` is "temporal" than `temporal_unit` is multiplied by `temporal_amount` to define the duration that the coupon will be applied to invoices for.
    unique_code_template : str
        On a bulk coupon, the template from which unique coupon codes are generated.
    unique_coupon_codes_count : int
        When this number reaches `max_redemptions` the coupon will no longer be redeemable.
    updated_at : datetime
        Last updated at
    """

    schema = {
        "applies_to_all_plans": bool,
        "applies_to_non_plan_charges": bool,
        "code": str,
        "coupon_type": str,
        "created_at": datetime,
        "discount": "CouponDiscount",
        "duration": str,
        "expired_at": datetime,
        "free_trial_amount": int,
        "free_trial_unit": str,
        "hosted_page_description": str,
        "id": str,
        "invoice_description": str,
        "max_redemptions": int,
        "max_redemptions_per_account": int,
        "name": str,
        "object": str,
        "plans": ["PlanMini"],
        "plans_names": list,
        "redeem_by": datetime,
        "redeemed_at": datetime,
        "redemption_resource": str,
        "state": str,
        "temporal_amount": int,
        "temporal_unit": str,
        "unique_code_template": str,
        "unique_coupon_codes_count": int,
        "updated_at": datetime,
    }


class PlanMini(Resource):
    """
    Attributes
    ----------
    code : str
        Unique code to identify the plan. This is used in Hosted Payment Page URLs and in the invoice exports.
    id : str
        Plan ID
    name : str
        This name describes your plan and will appear on the Hosted Payment Page and the subscriber's invoice.
    object : str
        Object type
    """

    schema = {"code": str, "id": str, "name": str, "object": str}


class CouponDiscount(Resource):
    """
    Attributes
    ----------
    currencies : :obj:`list` of :obj:`CouponDiscountPricing`
        This is only present when `type=fixed`.
    percent : int
        This is only present when `type=percent`.
    trial : CouponDiscountTrial
        This is only present when `type=free_trial`.
    type : str
    """

    schema = {
        "currencies": ["CouponDiscountPricing"],
        "percent": int,
        "trial": "CouponDiscountTrial",
        "type": str,
    }


class CouponDiscountPricing(Resource):
    """
    Attributes
    ----------
    amount : float
        Value of the fixed discount that this coupon applies.
    currency : str
        3-letter ISO 4217 currency code.
    """

    schema = {"amount": float, "currency": str}


class CouponDiscountTrial(Resource):
    """
    Attributes
    ----------
    length : int
        Trial length measured in the units specified by the sibling `unit` property
    unit : str
        Temporal unit of the free trial
    """

    schema = {"length": int, "unit": str}


class CreditPayment(Resource):
    """
    Attributes
    ----------
    account : AccountMini
        Account mini details
    action : str
        The action for which the credit was created.
    amount : float
        Total credit payment amount applied to the charge invoice.
    applied_to_invoice : InvoiceMini
        Invoice mini details
    created_at : datetime
        Created at
    currency : str
        3-letter ISO 4217 currency code.
    id : str
        Credit Payment ID
    object : str
        Object type
    original_credit_payment_id : str
        For credit payments with action `refund`, this is the credit payment that was refunded.
    original_invoice : InvoiceMini
        Invoice mini details
    refund_transaction : Transaction
    updated_at : datetime
        Last updated at
    uuid : str
        The UUID is useful for matching data with the CSV exports and building URLs into Recurly's UI.
    voided_at : datetime
        Voided at
    """

    schema = {
        "account": "AccountMini",
        "action": str,
        "amount": float,
        "applied_to_invoice": "InvoiceMini",
        "created_at": datetime,
        "currency": str,
        "id": str,
        "object": str,
        "original_credit_payment_id": str,
        "original_invoice": "InvoiceMini",
        "refund_transaction": "Transaction",
        "updated_at": datetime,
        "uuid": str,
        "voided_at": datetime,
    }


class InvoiceMini(Resource):
    """
    Attributes
    ----------
    id : str
        Invoice ID
    number : str
        Invoice number
    object : str
        Object type
    state : str
        Invoice state
    type : str
        Invoice type
    """

    schema = {"id": str, "number": str, "object": str, "state": str, "type": str}


class Transaction(Resource):
    """
    Attributes
    ----------
    account : AccountMini
        Account mini details
    amount : float
        Total transaction amount sent to the payment gateway.
    avs_check : str
        When processed, result from checking the overall AVS on the transaction.
    billing_address : Address
    collected_at : datetime
        Collected at, or if not collected yet, the time the transaction was created.
    collection_method : str
        The method by which the payment was collected.
    created_at : datetime
        Created at
    currency : str
        3-letter ISO 4217 currency code.
    customer_message : str
        For declined (`success=false`) transactions, the message displayed to the customer.
    customer_message_locale : str
        Language code for the message
    cvv_check : str
        When processed, result from checking the CVV/CVC value on the transaction.
    gateway_approval_code : str
        Transaction approval code from the payment gateway.
    gateway_message : str
        Transaction message from the payment gateway.
    gateway_reference : str
        Transaction reference number from the payment gateway.
    gateway_response_code : str
        For declined transactions (`success=false`), this field lists the gateway error code.
    gateway_response_time : float
        Time, in seconds, for gateway to process the transaction.
    gateway_response_values : dict
        The values in this field will vary from gateway to gateway.
    id : str
        Transaction ID
    invoice : InvoiceMini
        Invoice mini details
    ip_address_country : str
        IP address's country
    ip_address_v4 : str
        IP address provided when the billing information was collected:

        - When the customer enters billing information into the Recurly.js or Hosted Payment Pages, Recurly records the IP address.
        - When the merchant enters billing information using the API, the merchant may provide an IP address.
        - When the merchant enters billing information using the UI, no IP address is recorded.
    object : str
        Object type
    origin : str
        Describes how the transaction was triggered.
    original_transaction_id : str
        If this transaction is a refund (`type=refund`), this will be the ID of the original transaction on the invoice being refunded.
    payment_gateway : TransactionPaymentGateway
    payment_method : PaymentMethod
    refunded : bool
        Indicates if part or all of this transaction was refunded.
    status : str
        The current transaction status. Note that the status may change, e.g. a `pending` transaction may become `declined` or `success` may later become `void`.
    status_code : str
        Status code
    status_message : str
        For declined (`success=false`) transactions, the message displayed to the merchant.
    subscription_ids : :obj:`list` of :obj:`str`
        If the transaction is charging or refunding for one or more subscriptions, these are their IDs.
    success : bool
        Did this transaction complete successfully?
    type : str
        - `authorization` – verifies billing information and places a hold on money in the customer's account.
        - `capture` – captures funds held by an authorization and completes a purchase.
        - `purchase` – combines the authorization and capture in one transaction.
        - `refund` – returns all or a portion of the money collected in a previous transaction to the customer.
        - `verify` – a $0 or $1 transaction used to verify billing information which is immediately voided.
    uuid : str
        The UUID is useful for matching data with the CSV exports and building URLs into Recurly's UI.
    voided_at : datetime
        Voided at
    voided_by_invoice : InvoiceMini
        Invoice mini details
    """

    schema = {
        "account": "AccountMini",
        "amount": float,
        "avs_check": str,
        "billing_address": "Address",
        "collected_at": datetime,
        "collection_method": str,
        "created_at": datetime,
        "currency": str,
        "customer_message": str,
        "customer_message_locale": str,
        "cvv_check": str,
        "gateway_approval_code": str,
        "gateway_message": str,
        "gateway_reference": str,
        "gateway_response_code": str,
        "gateway_response_time": float,
        "gateway_response_values": dict,
        "id": str,
        "invoice": "InvoiceMini",
        "ip_address_country": str,
        "ip_address_v4": str,
        "object": str,
        "origin": str,
        "original_transaction_id": str,
        "payment_gateway": "TransactionPaymentGateway",
        "payment_method": "PaymentMethod",
        "refunded": bool,
        "status": str,
        "status_code": str,
        "status_message": str,
        "subscription_ids": list,
        "success": bool,
        "type": str,
        "uuid": str,
        "voided_at": datetime,
        "voided_by_invoice": "InvoiceMini",
    }


class TransactionPaymentGateway(Resource):
    """
    Attributes
    ----------
    id : str
    name : str
    object : str
        Object type
    type : str
    """

    schema = {"id": str, "name": str, "object": str, "type": str}


class Invoice(Resource):
    """
    Attributes
    ----------
    account : AccountMini
        Account mini details
    address : InvoiceAddress
    balance : float
        The outstanding balance remaining on this invoice.
    closed_at : datetime
        Date invoice was marked paid or failed.
    collection_method : str
        An automatic invoice means a corresponding transaction is run using the account's billing information at the same time the invoice is created. Manual invoices are created without a corresponding transaction. The merchant must enter a manual payment transaction or have the customer pay the invoice with an automatic method, like credit card, PayPal, Amazon, or ACH bank payment.
    created_at : datetime
        Created at
    credit_payments : :obj:`list` of :obj:`CreditPayment`
        Credit payments
    currency : str
        3-letter ISO 4217 currency code.
    customer_notes : str
        This will default to the Customer Notes text specified on the Invoice Settings. Specify custom notes to add or override Customer Notes.
    discount : float
        Total discounts applied to this invoice.
    due_at : datetime
        Date invoice is due. This is the date the net terms are reached.
    id : str
        Invoice ID
    line_items : LineItemList
    net_terms : int
        Integer representing the number of days after an invoice's creation that the invoice will become past due. If an invoice's net terms are set to '0', it is due 'On Receipt' and will become past due 24 hours after it’s created. If an invoice is due net 30, it will become past due at 31 days exactly.
    number : str
        If VAT taxation and the Country Invoice Sequencing feature are enabled, invoices will have country-specific invoice numbers for invoices billed to EU countries (ex: FR1001). Non-EU invoices will continue to use the site-level invoice number sequence.
    object : str
        Object type
    origin : str
        The event that created the invoice.
    paid : float
        The total amount of successful payments transaction on this invoice.
    po_number : str
        For manual invoicing, this identifies the PO number associated with the subscription.
    previous_invoice_id : str
        On refund invoices, this value will exist and show the invoice ID of the purchase invoice the refund was created from.
    refundable_amount : float
        The refundable amount on a charge invoice. It will be null for all other invoices.
    shipping_address : ShippingAddress
    state : str
        Invoice state
    subscription_ids : :obj:`list` of :obj:`str`
        If the invoice is charging or refunding for one or more subscriptions, these are their IDs.
    subtotal : float
        The summation of charges, discounts, and credits, before tax.
    tax : float
        The total tax on this invoice.
    tax_info : TaxInfo
        Tax info
    terms_and_conditions : str
        This will default to the Terms and Conditions text specified on the Invoice Settings page in your Recurly admin. Specify custom notes to add or override Terms and Conditions.
    total : float
        The final total on this invoice. The summation of invoice charges, discounts, credits, and tax.
    transactions : :obj:`list` of :obj:`Transaction`
        Transactions
    type : str
        Invoices are either charge, credit, or legacy invoices.
    updated_at : datetime
        Last updated at
    vat_number : str
        VAT registration number for the customer on this invoice. This will come from the VAT Number field in the Billing Info or the Account Info depending on your tax settings and the invoice collection method.
    vat_reverse_charge_notes : str
        VAT Reverse Charge Notes only appear if you have EU VAT enabled or are using your own Avalara AvaTax account and the customer is in the EU, has a VAT number, and is in a different country than your own. This will default to the VAT Reverse Charge Notes text specified on the Tax Settings page in your Recurly admin, unless custom notes were created with the original subscription.
    """

    schema = {
        "account": "AccountMini",
        "address": "InvoiceAddress",
        "balance": float,
        "closed_at": datetime,
        "collection_method": str,
        "created_at": datetime,
        "credit_payments": ["CreditPayment"],
        "currency": str,
        "customer_notes": str,
        "discount": float,
        "due_at": datetime,
        "id": str,
        "line_items": "LineItemList",
        "net_terms": int,
        "number": str,
        "object": str,
        "origin": str,
        "paid": float,
        "po_number": str,
        "previous_invoice_id": str,
        "refundable_amount": float,
        "shipping_address": "ShippingAddress",
        "state": str,
        "subscription_ids": list,
        "subtotal": float,
        "tax": float,
        "tax_info": "TaxInfo",
        "terms_and_conditions": str,
        "total": float,
        "transactions": ["Transaction"],
        "type": str,
        "updated_at": datetime,
        "vat_number": str,
        "vat_reverse_charge_notes": str,
    }


class InvoiceAddress(Resource):
    """
    Attributes
    ----------
    city : str
        City
    company : str
        Company
    country : str
        Country, 2-letter ISO code.
    first_name : str
        First name
    last_name : str
        Last name
    name_on_account : str
        Name on account
    phone : str
        Phone number
    postal_code : str
        Zip or postal code.
    region : str
        State or province.
    street1 : str
        Street 1
    street2 : str
        Street 2
    """

    schema = {
        "city": str,
        "company": str,
        "country": str,
        "first_name": str,
        "last_name": str,
        "name_on_account": str,
        "phone": str,
        "postal_code": str,
        "region": str,
        "street1": str,
        "street2": str,
    }


class TaxInfo(Resource):
    """
    Attributes
    ----------
    rate : float
        Rate
    region : str
        Provides the tax region applied on an invoice. For U.S. Sales Tax, this will be the 2 letter state code. For EU VAT this will be the 2 letter country code. For all country level tax types, this will display the regional tax, like VAT, GST, or PST.
    type : str
        Provides the tax type as "vat" for EU VAT, "usst" for U.S. Sales Tax, or the 2 letter country code for country level tax types like Canada, Australia, New Zealand, Israel, and all non-EU European countries.
    """

    schema = {"rate": float, "region": str, "type": str}


class LineItemList(Resource):
    """
    Attributes
    ----------
    data : :obj:`list` of :obj:`LineItem`
    has_more : bool
        Indicates there are more results on subsequent pages.
    next : str
        Path to subsequent page of results.
    object : str
        Will always be List.
    """

    schema = {"data": ["LineItem"], "has_more": bool, "next": str, "object": str}


class LineItem(Resource):
    """
    Attributes
    ----------
    account : AccountMini
        Account mini details
    accounting_code : str
        Internal accounting code to help you reconcile your revenue to the correct ledger. Line items created as part of a subscription invoice will use the plan or add-on's accounting code, otherwise the value will only be present if you define an accounting code when creating the line item.
    add_on_code : str
        If the line item is a charge or credit for an add-on, this is its code.
    add_on_id : str
        If the line item is a charge or credit for an add-on this is its ID.
    amount : float
        `(quantity * unit_amount) - (discount + tax)`
    created_at : datetime
        When the line item was created.
    credit_applied : float
        The amount of credit from this line item that was applied to the invoice.
    credit_reason_code : str
        The reason the credit was given when line item is `type=credit`.
    currency : str
        3-letter ISO 4217 currency code.
    description : str
        Description that appears on the invoice. For subscription related items this will be filled in automatically.
    discount : float
        The discount applied to the line item.
    end_date : datetime
        If this date is provided, it indicates the end of a time range.
    external_sku : str
        Optional Stock Keeping Unit assigned to an item. Available when the Credit Invoices and Subscription Billing Terms features are enabled.
    id : str
        Line item ID
    invoice_id : str
        Once the line item has been invoiced this will be the invoice's ID.
    invoice_number : str
        Once the line item has been invoiced this will be the invoice's number. If VAT taxation and the Country Invoice Sequencing feature are enabled, invoices will have country-specific invoice numbers for invoices billed to EU countries (ex: FR1001). Non-EU invoices will continue to use the site-level invoice number sequence.
    item_code : str
        Unique code to identify an item. Available when the Credit Invoices and Subscription Billing Terms features are enabled.
    item_id : str
        System-generated unique identifier for an item. Available when the Credit Invoices and Subscription Billing Terms features are enabled.
    legacy_category : str
        Category to describe the role of a line item on a legacy invoice:
        - "charges" refers to charges being billed for on this invoice.
        - "credits" refers to refund or proration credits. This portion of the invoice can be considered a credit memo.
        - "applied_credits" refers to previous credits applied to this invoice. See their original_line_item_id to determine where the credit first originated.
        - "carryforwards" can be ignored. They exist to consume any remaining credit balance. A new credit with the same amount will be created and placed back on the account.
    object : str
        Object type
    origin : str
        A credit created from an original charge will have the value of the charge's origin.
    original_line_item_invoice_id : str
        The invoice where the credit originated. Will only have a value if the line item is a credit created from a previous credit, or if the credit was created from a charge refund.
    plan_code : str
        If the line item is a charge or credit for a plan or add-on, this is the plan's code.
    plan_id : str
        If the line item is a charge or credit for a plan or add-on, this is the plan's ID.
    previous_line_item_id : str
        Will only have a value if the line item is a credit created from a previous credit, or if the credit was created from a charge refund.
    product_code : str
        For plan-related line items this will be the plan's code, for add-on related line items it will be the add-on's code. For item-related line itmes it will be the item's `external_sku`.
    proration_rate : float
        When a line item has been prorated, this is the rate of the proration. Proration rates were made available for line items created after March 30, 2017. For line items created prior to that date, the proration rate will be `null`, even if the line item was prorated.
    quantity : int
        This number will be multiplied by the unit amount to compute the subtotal before any discounts or taxes.
    refund : bool
        Refund?
    refunded_quantity : int
        For refund charges, the quantity being refunded. For non-refund charges, the total quantity refunded (possibly over multiple refunds).
    revenue_schedule_type : str
        Revenue schedule type
    shipping_address : ShippingAddress
    start_date : datetime
        If an end date is present, this is value indicates the beginning of a billing time range. If no end date is present it indicates billing for a specific date.
    state : str
        Pending line items are charges or credits on an account that have not been applied to an invoice yet. Invoiced line items will always have an `invoice_id` value.
    subscription_id : str
        If the line item is a charge or credit for a subscription, this is its ID.
    subtotal : float
        `quantity * unit_amount`
    tax : float
        The tax amount for the line item.
    tax_code : str
        Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system. If you are using Recurly’s EU VAT feature you can use `unknown`, `physical`, or `digital`.
    tax_exempt : bool
        `true` exempts tax on charges, `false` applies tax on charges. If not defined, then defaults to the Plan and Site settings. This attribute does not work for credits (negative line items). Credits are always applied post-tax. Pre-tax discounts should use the Coupons feature.
    tax_info : TaxInfo
        Tax info
    taxable : bool
        `true` if the line item is taxable, `false` if it is not.
    type : str
        Charges are positive line items that debit the account. Credits are negative line items that credit the account.
    unit_amount : float
        Positive amount for a charge, negative amount for a credit.
    updated_at : datetime
        When the line item was last changed.
    uuid : str
        The UUID is useful for matching data with the CSV exports and building URLs into Recurly's UI.
    """

    schema = {
        "account": "AccountMini",
        "accounting_code": str,
        "add_on_code": str,
        "add_on_id": str,
        "amount": float,
        "created_at": datetime,
        "credit_applied": float,
        "credit_reason_code": str,
        "currency": str,
        "description": str,
        "discount": float,
        "end_date": datetime,
        "external_sku": str,
        "id": str,
        "invoice_id": str,
        "invoice_number": str,
        "item_code": str,
        "item_id": str,
        "legacy_category": str,
        "object": str,
        "origin": str,
        "original_line_item_invoice_id": str,
        "plan_code": str,
        "plan_id": str,
        "previous_line_item_id": str,
        "product_code": str,
        "proration_rate": float,
        "quantity": int,
        "refund": bool,
        "refunded_quantity": int,
        "revenue_schedule_type": str,
        "shipping_address": "ShippingAddress",
        "start_date": datetime,
        "state": str,
        "subscription_id": str,
        "subtotal": float,
        "tax": float,
        "tax_code": str,
        "tax_exempt": bool,
        "tax_info": "TaxInfo",
        "taxable": bool,
        "type": str,
        "unit_amount": float,
        "updated_at": datetime,
        "uuid": str,
    }


class InvoiceCollection(Resource):
    """
    Attributes
    ----------
    charge_invoice : Invoice
    credit_invoices : :obj:`list` of :obj:`Invoice`
        Credit invoices
    object : str
        Object type
    """

    schema = {
        "charge_invoice": "Invoice",
        "credit_invoices": ["Invoice"],
        "object": str,
    }


class AccountNote(Resource):
    """
    Attributes
    ----------
    account_id : str
    created_at : datetime
    id : str
    message : str
    object : str
        Object type
    user : User
    """

    schema = {
        "account_id": str,
        "created_at": datetime,
        "id": str,
        "message": str,
        "object": str,
        "user": "User",
    }


class User(Resource):
    """
    Attributes
    ----------
    created_at : datetime
    deleted_at : datetime
    email : str
    first_name : str
    id : str
    last_name : str
    object : str
        Object type
    time_zone : str
    """

    schema = {
        "created_at": datetime,
        "deleted_at": datetime,
        "email": str,
        "first_name": str,
        "id": str,
        "last_name": str,
        "object": str,
        "time_zone": str,
    }


class Subscription(Resource):
    """
    Attributes
    ----------
    account : AccountMini
        Account mini details
    activated_at : datetime
        Activated at
    add_ons : :obj:`list` of :obj:`SubscriptionAddOn`
        Add-ons
    add_ons_total : float
        Total price of add-ons
    auto_renew : bool
        Whether the subscription renews at the end of its term.
    bank_account_authorized_at : datetime
        Recurring subscriptions paid with ACH will have this attribute set. This timestamp is used for alerting customers to reauthorize in 3 years in accordance with NACHA rules. If a subscription becomes inactive or the billing info is no longer a bank account, this timestamp is cleared.
    canceled_at : datetime
        Canceled at
    collection_method : str
        Collection method
    coupon_redemptions : :obj:`list` of :obj:`CouponRedemptionMini`
        Coupon redemptions
    created_at : datetime
        Created at
    currency : str
        3-letter ISO 4217 currency code.
    current_period_ends_at : datetime
        Current billing period ends at
    current_period_started_at : datetime
        Current billing period started at
    current_term_ends_at : datetime
        When the term ends. This is calculated by a plan's interval and `total_billing_cycles` in a term. Subscription changes with a `timeframe=renewal` will be applied on this date.
    current_term_started_at : datetime
        The start date of the term when the first billing period starts. The subscription term is the length of time that a customer will be committed to a subscription. A term can span multiple billing periods.
    custom_fields : :obj:`list` of :obj:`CustomField`
        The custom fields will only be altered when they are included in a request. Sending an empty array will not remove any existing values. To remove a field send the name with a null or empty value.
    customer_notes : str
        Customer notes
    expiration_reason : str
        Expiration reason
    expires_at : datetime
        Expires at
    id : str
        Subscription ID
    net_terms : int
        Integer representing the number of days after an invoice's creation that the invoice will become past due. If an invoice's net terms are set to '0', it is due 'On Receipt' and will become past due 24 hours after it’s created. If an invoice is due net 30, it will become past due at 31 days exactly.
    object : str
        Object type
    paused_at : datetime
        Null unless subscription is paused or will pause at the end of the current billing period.
    pending_change : SubscriptionChange
        Subscription Change
    plan : PlanMini
        Just the important parts.
    po_number : str
        For manual invoicing, this identifies the PO number associated with the subscription.
    quantity : int
        Subscription quantity
    remaining_billing_cycles : int
        The remaining billing cycles in the current term.
    remaining_pause_cycles : int
        Null unless subscription is paused or will pause at the end of the current billing period.
    renewal_billing_cycles : int
        If `auto_renew=true`, when a term completes, `total_billing_cycles` takes this value as the length of subsequent terms. Defaults to the plan's `total_billing_cycles`.
    revenue_schedule_type : str
        Revenue schedule type
    shipping : SubscriptionShipping
        Subscription shipping details
    state : str
        State
    subtotal : float
        Estimated total, before tax.
    terms_and_conditions : str
        Terms and conditions
    total_billing_cycles : int
        The number of cycles/billing periods in a term. When `remaining_billing_cycles=0`, if `auto_renew=true` the subscription will renew and a new term will begin, otherwise the subscription will expire.
    trial_ends_at : datetime
        Trial period ends at
    trial_started_at : datetime
        Trial period started at
    unit_amount : float
        Subscription unit price
    updated_at : datetime
        Last updated at
    uuid : str
        The UUID is useful for matching data with the CSV exports and building URLs into Recurly's UI.
    """

    schema = {
        "account": "AccountMini",
        "activated_at": datetime,
        "add_ons": ["SubscriptionAddOn"],
        "add_ons_total": float,
        "auto_renew": bool,
        "bank_account_authorized_at": datetime,
        "canceled_at": datetime,
        "collection_method": str,
        "coupon_redemptions": ["CouponRedemptionMini"],
        "created_at": datetime,
        "currency": str,
        "current_period_ends_at": datetime,
        "current_period_started_at": datetime,
        "current_term_ends_at": datetime,
        "current_term_started_at": datetime,
        "custom_fields": ["CustomField"],
        "customer_notes": str,
        "expiration_reason": str,
        "expires_at": datetime,
        "id": str,
        "net_terms": int,
        "object": str,
        "paused_at": datetime,
        "pending_change": "SubscriptionChange",
        "plan": "PlanMini",
        "po_number": str,
        "quantity": int,
        "remaining_billing_cycles": int,
        "remaining_pause_cycles": int,
        "renewal_billing_cycles": int,
        "revenue_schedule_type": str,
        "shipping": "SubscriptionShipping",
        "state": str,
        "subtotal": float,
        "terms_and_conditions": str,
        "total_billing_cycles": int,
        "trial_ends_at": datetime,
        "trial_started_at": datetime,
        "unit_amount": float,
        "updated_at": datetime,
        "uuid": str,
    }


class SubscriptionShipping(Resource):
    """
    Attributes
    ----------
    address : ShippingAddress
    amount : float
        Subscription's shipping cost
    method : ShippingMethodMini
    object : str
        Object type
    """

    schema = {
        "address": "ShippingAddress",
        "amount": float,
        "method": "ShippingMethodMini",
        "object": str,
    }


class ShippingMethodMini(Resource):
    """
    Attributes
    ----------
    code : str
        The internal name used identify the shipping method.
    id : str
        Shipping Method ID
    name : str
        The name of the shipping method displayed to customers.
    object : str
        Object type
    """

    schema = {"code": str, "id": str, "name": str, "object": str}


class CouponRedemptionMini(Resource):
    """
    Attributes
    ----------
    coupon : CouponMini
    created_at : datetime
        Created at
    discounted : float
        The amount that was discounted upon the application of the coupon, formatted with the currency.
    id : str
        Coupon Redemption ID
    object : str
        Will always be `coupon`.
    state : str
        Invoice state
    """

    schema = {
        "coupon": "CouponMini",
        "created_at": datetime,
        "discounted": float,
        "id": str,
        "object": str,
        "state": str,
    }


class CouponMini(Resource):
    """
    Attributes
    ----------
    code : str
        The code the customer enters to redeem the coupon.
    coupon_type : str
        Whether the coupon is "single_code" or "bulk". Bulk coupons will require a `unique_code_template` and will generate unique codes through the `/generate` endpoint.
    discount : CouponDiscount
        Details of the discount a coupon applies. Will contain a `type`
        property and one of the following properties: `percent`, `fixed`, `trial`.
    expired_at : datetime
        The date and time the coupon was expired early or reached its `max_redemptions`.
    id : str
        Coupon ID
    name : str
        The internal name for the coupon.
    object : str
        Object type
    state : str
        Indicates if the coupon is redeemable, and if it is not, why.
    """

    schema = {
        "code": str,
        "coupon_type": str,
        "discount": "CouponDiscount",
        "expired_at": datetime,
        "id": str,
        "name": str,
        "object": str,
        "state": str,
    }


class SubscriptionChange(Resource):
    """
    Attributes
    ----------
    activate_at : datetime
        Activated at
    activated : bool
        Returns `true` if the subscription change is activated.
    add_ons : :obj:`list` of :obj:`SubscriptionAddOn`
        These add-ons will be used when the subscription renews.
    created_at : datetime
        Created at
    deleted_at : datetime
        Deleted at
    id : str
        The ID of the Subscription Change.
    object : str
        Object type
    plan : PlanMini
        Just the important parts.
    quantity : int
        Subscription quantity
    revenue_schedule_type : str
        Revenue schedule type
    setup_fee_revenue_schedule_type : str
        Setup fee revenue schedule type
    shipping : SubscriptionShipping
        Subscription shipping details
    subscription_id : str
        The ID of the subscription that is going to be changed.
    unit_amount : float
        Unit amount
    updated_at : datetime
        Updated at
    """

    schema = {
        "activate_at": datetime,
        "activated": bool,
        "add_ons": ["SubscriptionAddOn"],
        "created_at": datetime,
        "deleted_at": datetime,
        "id": str,
        "object": str,
        "plan": "PlanMini",
        "quantity": int,
        "revenue_schedule_type": str,
        "setup_fee_revenue_schedule_type": str,
        "shipping": "SubscriptionShipping",
        "subscription_id": str,
        "unit_amount": float,
        "updated_at": datetime,
    }


class SubscriptionAddOn(Resource):
    """
    Attributes
    ----------
    add_on : AddOnMini
        Just the important parts.
    created_at : datetime
        Created at
    expired_at : datetime
        Expired at
    id : str
        Subscription Add-on ID
    object : str
        Object type
    quantity : int
        Add-on quantity
    subscription_id : str
        Subscription ID
    unit_amount : float
        This is priced in the subscription's currency.
    updated_at : datetime
        Updated at
    """

    schema = {
        "add_on": "AddOnMini",
        "created_at": datetime,
        "expired_at": datetime,
        "id": str,
        "object": str,
        "quantity": int,
        "subscription_id": str,
        "unit_amount": float,
        "updated_at": datetime,
    }


class AddOnMini(Resource):
    """
    Attributes
    ----------
    accounting_code : str
        Accounting code for invoice line items for this add-on. If no value is provided, it defaults to add-on's code.
    code : str
        The unique identifier for the add-on within its plan.
    external_sku : str
        Optional, stock keeping unit to link the item to other inventory systems.
    id : str
        Add-on ID
    item_id : str
        Item ID
    name : str
        Describes your add-on and will appear in subscribers' invoices.
    object : str
        Object type
    """

    schema = {
        "accounting_code": str,
        "code": str,
        "external_sku": str,
        "id": str,
        "item_id": str,
        "name": str,
        "object": str,
    }


class UniqueCouponCode(Resource):
    """
    Attributes
    ----------
    code : str
        The code the customer enters to redeem the coupon.
    created_at : datetime
        Created at
    expired_at : datetime
        The date and time the coupon was expired early or reached its `max_redemptions`.
    id : str
        Unique Coupon Code ID
    object : str
        Object type
    redeemed_at : datetime
        The date and time the unique coupon code was redeemed.
    state : str
        Indicates if the unique coupon code is redeemable or why not.
    updated_at : datetime
        Updated at
    """

    schema = {
        "code": str,
        "created_at": datetime,
        "expired_at": datetime,
        "id": str,
        "object": str,
        "redeemed_at": datetime,
        "state": str,
        "updated_at": datetime,
    }


class CustomFieldDefinition(Resource):
    """
    Attributes
    ----------
    created_at : datetime
        Created at
    deleted_at : datetime
        Definitions are initially soft deleted, and once all the values are removed from the accouts or subscriptions, will be hard deleted an no longer visible.
    display_name : str
        Used to label the field when viewing and editing the field in Recurly's admin UI.
    id : str
        Custom field definition ID
    name : str
        Used by the API to identify the field or reading and writing. The name can only be used once per Recurly object type.
    object : str
        Object type
    related_type : str
        Related Recurly object type
    tooltip : str
        Displayed as a tooltip when editing the field in the Recurly admin UI.
    updated_at : datetime
        Last updated at
    user_access : str
        The access control applied inside Recurly's admin UI:
        - `api_only` - No one will be able to view or edit this field's data via the admin UI.
        - `read_only` - Users with the Customers role will be able to view this field's data via the admin UI, but
          editing will only be available via the API.
        - `write` - Users with the Customers role will be able to view and edit this field's data via the admin UI.
    """

    schema = {
        "created_at": datetime,
        "deleted_at": datetime,
        "display_name": str,
        "id": str,
        "name": str,
        "object": str,
        "related_type": str,
        "tooltip": str,
        "updated_at": datetime,
        "user_access": str,
    }


class Item(Resource):
    """
    Attributes
    ----------
    accounting_code : str
        Accounting code for invoice line items.
    code : str
        Unique code to identify the item.
    created_at : datetime
        Created at
    currencies : :obj:`list` of :obj:`Pricing`
        Item Pricing
    custom_fields : :obj:`list` of :obj:`CustomField`
        The custom fields will only be altered when they are included in a request. Sending an empty array will not remove any existing values. To remove a field send the name with a null or empty value.
    deleted_at : datetime
        Deleted at
    description : str
        Optional, description.
    external_sku : str
        Optional, stock keeping unit to link the item to other inventory systems.
    id : str
        Item ID
    name : str
        This name describes your item and will appear on the invoice when it's purchased on a one time basis.
    object : str
        Object type
    revenue_schedule_type : str
        Revenue schedule type
    state : str
        The current state of the item.
    tax_code : str
        Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system. If you are using Recurly’s EU VAT feature you can use `unknown`, `physical`, or `digital`.
    tax_exempt : bool
        `true` exempts tax on the item, `false` applies tax on the item.
    updated_at : datetime
        Last updated at
    """

    schema = {
        "accounting_code": str,
        "code": str,
        "created_at": datetime,
        "currencies": ["Pricing"],
        "custom_fields": ["CustomField"],
        "deleted_at": datetime,
        "description": str,
        "external_sku": str,
        "id": str,
        "name": str,
        "object": str,
        "revenue_schedule_type": str,
        "state": str,
        "tax_code": str,
        "tax_exempt": bool,
        "updated_at": datetime,
    }


class Pricing(Resource):
    """
    Attributes
    ----------
    currency : str
        3-letter ISO 4217 currency code.
    unit_amount : float
        Unit price
    """

    schema = {"currency": str, "unit_amount": float}


class BinaryFile(Resource):
    """
    Attributes
    ----------
    data : str
    """

    schema = {"data": str}


class Plan(Resource):
    """
    Attributes
    ----------
    accounting_code : str
        Accounting code for invoice line items for the plan. If no value is provided, it defaults to plan's code.
    auto_renew : bool
        Subscriptions will automatically inherit this value once they are active. If `auto_renew` is `true`, then a subscription will automatically renew its term at renewal. If `auto_renew` is `false`, then a subscription will expire at the end of its term. `auto_renew` can be overridden on the subscription record itself.
    code : str
        Unique code to identify the plan. This is used in Hosted Payment Page URLs and in the invoice exports.
    created_at : datetime
        Created at
    currencies : :obj:`list` of :obj:`PlanPricing`
        Pricing
    deleted_at : datetime
        Deleted at
    description : str
        Optional description, not displayed.
    hosted_pages : PlanHostedPages
        Hosted pages settings
    id : str
        Plan ID
    interval_length : int
        Length of the plan's billing interval in `interval_unit`.
    interval_unit : str
        Unit for the plan's billing interval.
    name : str
        This name describes your plan and will appear on the Hosted Payment Page and the subscriber's invoice.
    object : str
        Object type
    revenue_schedule_type : str
        Revenue schedule type
    setup_fee_accounting_code : str
        Accounting code for invoice line items for the plan's setup fee. If no value is provided, it defaults to plan's accounting code.
    setup_fee_revenue_schedule_type : str
        Setup fee revenue schedule type
    state : str
        The current state of the plan.
    tax_code : str
        Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system. If you are using Recurly’s EU VAT feature you can use `unknown`, `physical`, or `digital`.
    tax_exempt : bool
        `true` exempts tax on the plan, `false` applies tax on the plan.
    total_billing_cycles : int
        Automatically terminate subscriptions after a defined number of billing cycles. Number of billing cycles before the plan automatically stops renewing, defaults to `null` for continuous, automatic renewal.
    trial_length : int
        Length of plan's trial period in `trial_units`. `0` means `no trial`.
    trial_unit : str
        Units for the plan's trial period.
    updated_at : datetime
        Last updated at
    """

    schema = {
        "accounting_code": str,
        "auto_renew": bool,
        "code": str,
        "created_at": datetime,
        "currencies": ["PlanPricing"],
        "deleted_at": datetime,
        "description": str,
        "hosted_pages": "PlanHostedPages",
        "id": str,
        "interval_length": int,
        "interval_unit": str,
        "name": str,
        "object": str,
        "revenue_schedule_type": str,
        "setup_fee_accounting_code": str,
        "setup_fee_revenue_schedule_type": str,
        "state": str,
        "tax_code": str,
        "tax_exempt": bool,
        "total_billing_cycles": int,
        "trial_length": int,
        "trial_unit": str,
        "updated_at": datetime,
    }


class PlanPricing(Resource):
    """
    Attributes
    ----------
    currency : str
        3-letter ISO 4217 currency code.
    setup_fee : float
        Amount of one-time setup fee automatically charged at the beginning of a subscription billing cycle. For subscription plans with a trial, the setup fee will be charged at the time of signup. Setup fees do not increase with the quantity of a subscription plan.
    unit_amount : float
        Unit price
    """

    schema = {"currency": str, "setup_fee": float, "unit_amount": float}


class PlanHostedPages(Resource):
    """
    Attributes
    ----------
    bypass_confirmation : bool
        If `true`, the customer will be sent directly to your `success_url` after a successful signup, bypassing Recurly's hosted confirmation page.
    cancel_url : str
        URL to redirect to on canceled signup on the hosted payment pages.
    display_quantity : bool
        Determines if the quantity field is displayed on the hosted pages for the plan.
    success_url : str
        URL to redirect to after signup on the hosted payment pages.
    """

    schema = {
        "bypass_confirmation": bool,
        "cancel_url": str,
        "display_quantity": bool,
        "success_url": str,
    }


class AddOn(Resource):
    """
    Attributes
    ----------
    accounting_code : str
        Accounting code for invoice line items for this add-on. If no value is provided, it defaults to add-on's code.
    code : str
        The unique identifier for the add-on within its plan.
    created_at : datetime
        Created at
    currencies : :obj:`list` of :obj:`AddOnPricing`
        Add-on pricing
    default_quantity : int
        Default quantity for the hosted pages.
    deleted_at : datetime
        Deleted at
    display_quantity : bool
        Determines if the quantity field is displayed on the hosted pages for the add-on.
    external_sku : str
        Optional, stock keeping unit to link the item to other inventory systems.
    id : str
        Add-on ID
    item : ItemMini
        Just the important parts.
    name : str
        Describes your add-on and will appear in subscribers' invoices.
    object : str
        Object type
    optional : bool
        Whether the add-on is optional for the customer to include in their purchase on the hosted payment page. If false, the add-on will be included when a subscription is created through the Recurly UI. However, the add-on will not be included when a subscription is created through the API.
    plan_id : str
        Plan ID
    revenue_schedule_type : str
        When this add-on is invoiced, the line item will use this revenue schedule. If `item_code`/`item_id` is part of the request then `revenue_schedule_type` must be absent in the request as the value will be set from the item.
    state : str
        Add-ons can be either active or inactive.
    tax_code : str
        Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system. If you are using Recurly’s EU VAT feature you can use `unknown`, `physical`, or `digital`.
    updated_at : datetime
        Last updated at
    """

    schema = {
        "accounting_code": str,
        "code": str,
        "created_at": datetime,
        "currencies": ["AddOnPricing"],
        "default_quantity": int,
        "deleted_at": datetime,
        "display_quantity": bool,
        "external_sku": str,
        "id": str,
        "item": "ItemMini",
        "name": str,
        "object": str,
        "optional": bool,
        "plan_id": str,
        "revenue_schedule_type": str,
        "state": str,
        "tax_code": str,
        "updated_at": datetime,
    }


class AddOnPricing(Resource):
    """
    Attributes
    ----------
    currency : str
        3-letter ISO 4217 currency code.
    unit_amount : float
        Unit price
    """

    schema = {"currency": str, "unit_amount": float}


class ItemMini(Resource):
    """
    Attributes
    ----------
    code : str
        Unique code to identify the item.
    description : str
        Optional, description.
    id : str
        Item ID
    name : str
        This name describes your item and will appear on the invoice when it's purchased on a one time basis.
    object : str
        Object type
    state : str
        The current state of the item.
    """

    schema = {
        "code": str,
        "description": str,
        "id": str,
        "name": str,
        "object": str,
        "state": str,
    }


class ShippingMethod(Resource):
    """
    Attributes
    ----------
    code : str
        The internal name used identify the shipping method.
    created_at : datetime
        Created at
    deleted_at : datetime
        Deleted at
    id : str
        Shipping Method ID
    name : str
        The name of the shipping method displayed to customers.
    object : str
        Object type
    tax_code : str
        Used by Avalara, Vertex, and Recurly’s built-in tax feature. The tax
        code values are specific to each tax system. If you are using Recurly’s
        built-in taxes the values are:

        - `FR` – Common Carrier FOB Destination
        - `FR022000` – Common Carrier FOB Origin
        - `FR020400` – Non Common Carrier FOB Destination
        - `FR020500` – Non Common Carrier FOB Origin
        - `FR010100` – Delivery by Company Vehicle Before Passage of Title
        - `FR010200` – Delivery by Company Vehicle After Passage of Title
        - `NT` – Non-Taxable
    updated_at : datetime
        Last updated at
    """

    schema = {
        "code": str,
        "created_at": datetime,
        "deleted_at": datetime,
        "id": str,
        "name": str,
        "object": str,
        "tax_code": str,
        "updated_at": datetime,
    }
