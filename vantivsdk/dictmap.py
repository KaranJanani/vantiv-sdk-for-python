# -*- coding: utf-8 -*-l
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
from __future__ import unicode_literals

# The following dict is automatically generated by tools/postGeneration.py, Please DO NOT manually change it.

txns_dict = {'accountUpdate': {'cardOrToken': 'cardOrToken',
                 'customerId': '',
                 'id': '',
                 'orderId': '',
                 'reportGroup': ''},
'activate': {'amount': '',
            'card': 'giftCardCardType',
            'customerId': '',
            'id': '',
            'orderId': '',
            'orderSource': '',
            'reportGroup': '',
            'virtualGiftCard': 'virtualGiftCardType'},
'activateReversal': {'card': 'giftCardCardType',
                    'cnpTxnId': '',
                    'customerId': '',
                    'id': '',
                    'originalAmount': '',
                    'originalRefCode': '',
                    'originalSequenceNumber': '',
                    'originalSystemTraceId': '',
                    'originalTxnTime': '',
                    'reportGroup': '',
                    'virtualGiftCardBin': ''},
'authReversal': {'actionReason': '',
                'amount': '',
                'cnpTxnId': '',
                'customerId': '',
                'id': '',
                'payPalNotes': '',
                'reportGroup': '',
                'surchargeAmount': ''},
'authorization': {'additionalCOFData': 'additionalCOFData',
                 'advancedFraudChecks': 'advancedFraudChecksType',
                 'allowPartialAuth': '',
                 'amount': '',
                 'applepay': 'applepayType',
                 'billToAddress': 'billToAddress',
                 'businessIndicator': '',
                 'card': 'cardType',
                 'cardholderAuthentication': 'fraudCheckType',
                 'cnpTxnId': '',
                 'crypto': '',
                 'customBilling': 'customBilling',
                 'customerId': '',
                 'customerInfo': 'customerInfo',
                 'debtRepayment': '',
                 'enhancedData': 'enhancedData',
                 'filtering': 'filteringType',
                 'fraudCheckStatus': '',
                 'fraudFilterOverride': '',
                 'healthcareIIAS': 'healthcareIIAS',
                 'id': '',
                 'lodgingInfo': 'lodgingInfo',
                 'merchantCategoryCode': '',
                 'merchantData': 'merchantDataType',
                 'mpos': 'mposType',
                 'orderChannel': '',
                 'orderId': '',
                 'orderSource': '',
                 'originalNetworkTransactionId': '',
                 'originalTransactionAmount': '',
                 'paypage': 'cardPaypageType',
                 'paypal': 'payPal',
                 'pinlessDebitRequest': 'pinlessDebitRequestType',
                 'pos': 'pos',
                 'processingInstructions': 'processingInstructions',
                 'processingType': '',
                 'recurringRequest': 'recurringRequestType',
                 'recyclingRequest': 'recyclingRequestType',
                 'reportGroup': '',
                 'retailerAddress': 'retailerAddress',
                 'secondaryAmount': '',
                 'shipToAddress': 'shipToAddress',
                 'skipRealtimeAU': '',
                 'surchargeAmount': '',
                 'taxType': '',
                 'token': 'cardTokenType',
                 'wallet': 'wallet'},
'balanceInquiry': {'card': 'giftCardCardType',
                  'customerId': '',
                  'id': '',
                  'orderId': '',
                  'orderSource': '',
                  'reportGroup': ''},
'cancelSubscription': {'subscriptionId': ''},
'capture': {'amount': '',
           'cnpTxnId': '',
           'customBilling': 'customBilling',
           'customerId': '',
           'enhancedData': 'enhancedData',
           'id': '',
           'lodgingInfo': 'lodgingInfo',
           'orderId': '',
           'partial': '',
           'payPalNotes': '',
           'payPalOrderComplete': '',
           'pin': '',
           'processingInstructions': 'processingInstructions',
           'reportGroup': '',
           'surchargeAmount': ''},
'captureGivenAuth': {'additionalCOFData': 'additionalCOFData',
                    'amount': '',
                    'authInformation': 'authInformation',
                    'billToAddress': 'billToAddress',
                    'businessIndicator': '',
                    'card': 'cardType',
                    'crypto': '',
                    'customBilling': 'customBilling',
                    'customerId': '',
                    'debtRepayment': '',
                    'enhancedData': 'enhancedData',
                    'id': '',
                    'lodgingInfo': 'lodgingInfo',
                    'merchantCategoryCode': '',
                    'merchantData': 'merchantDataType',
                    'mpos': 'mposType',
                    'orderId': '',
                    'orderSource': '',
                    'originalNetworkTransactionId': '',
                    'originalTransactionAmount': '',
                    'paypage': 'cardPaypageType',
                    'pos': 'pos',
                    'processingInstructions': 'processingInstructions',
                    'processingType': '',
                    'reportGroup': '',
                    'retailerAddress': 'retailerAddress',
                    'secondaryAmount': '',
                    'shipToAddress': 'shipToAddress',
                    'surchargeAmount': '',
                    'taxType': '',
                    'token': 'cardTokenType'},
'createPlan': {'active': '',
              'amount': '',
              'description': '',
              'intervalType': '',
              'name': '',
              'numberOfPayments': '',
              'planCode': '',
              'trialIntervalType': '',
              'trialNumberOfIntervals': ''},
'credit': {'actionReason': '',
          'amount': '',
          'billToAddress': 'billToAddress',
          'businessIndicator': '',
          'card': 'cardType',
          'cnpTxnId': '',
          'customBilling': 'customBilling',
          'customerId': '',
          'enhancedData': 'enhancedData',
          'id': '',
          'lodgingInfo': 'lodgingInfo',
          'merchantCategoryCode': '',
          'merchantData': 'merchantDataType',
          'mpos': 'mposType',
          'orderId': '',
          'orderSource': '',
          'payPalNotes': '',
          'paypage': 'cardPaypageType',
          'paypal': 'payPal',
          'pin': '',
          'pos': 'pos',
          'processingInstructions': 'processingInstructions',
          'reportGroup': '',
          'secondaryAmount': '',
          'surchargeAmount': '',
          'taxType': '',
          'token': 'cardTokenType'},
'customerCredit': {'accountInfo': 'echeckType',
                  'amount': '',
                  'customIdentifier': '',
                  'customerId': '',
                  'customerName': '',
                  'fundingCustomerId': '',
                  'fundsTransferId': '',
                  'id': '',
                  'reportGroup': ''},
'customerDebit': {'accountInfo': 'echeckType',
                 'amount': '',
                 'customIdentifier': '',
                 'customerId': '',
                 'customerName': '',
                 'fundingCustomerId': '',
                 'fundsTransferId': '',
                 'id': '',
                 'reportGroup': ''},
'deactivate': {'card': 'giftCardCardType',
              'customerId': '',
              'id': '',
              'orderId': '',
              'orderSource': '',
              'reportGroup': ''},
'deactivateReversal': {'card': 'giftCardCardType',
                      'cnpTxnId': '',
                      'customerId': '',
                      'id': '',
                      'originalRefCode': '',
                      'originalSequenceNumber': '',
                      'originalSystemTraceId': '',
                      'originalTxnTime': '',
                      'reportGroup': ''},
'depositReversal': {'card': 'giftCardCardType',
                   'cnpTxnId': '',
                   'customerId': '',
                   'id': '',
                   'originalAmount': '',
                   'originalRefCode': '',
                   'originalSequenceNumber': '',
                   'originalSystemTraceId': '',
                   'originalTxnTime': '',
                   'reportGroup': ''},
'depositTransactionReversal': {'amount': '',
                              'cnpTxnId': '',
                              'customBilling': 'customBilling',
                              'customerId': '',
                              'enhancedData': 'enhancedData',
                              'id': '',
                              'lodgingInfo': 'lodgingInfo',
                              'pin': '',
                              'processingInstructions': 'processingInstructions',
                              'reportGroup': '',
                              'surchargeAmount': ''},
'echeckCredit': {'amount': '',
                'billToAddress': 'billToAddress',
                'cnpTxnId': '',
                'customBilling': 'customBilling',
                'customIdentifier': '',
                'customerId': '',
                'echeck': 'echeckType',
                'echeckToken': 'echeckTokenType',
                'id': '',
                'merchantData': 'merchantDataType',
                'orderId': '',
                'orderSource': '',
                'reportGroup': '',
                'secondaryAmount': ''},
'echeckPreNoteCredit': {'billToAddress': 'billToAddress',
                       'customerId': '',
                       'echeck': 'echeckType',
                       'id': '',
                       'merchantData': 'merchantDataType',
                       'orderId': '',
                       'orderSource': '',
                       'reportGroup': ''},
'echeckPreNoteSale': {'billToAddress': 'billToAddress',
                     'customerId': '',
                     'echeck': 'echeckType',
                     'id': '',
                     'merchantData': 'merchantDataType',
                     'orderId': '',
                     'orderSource': '',
                     'reportGroup': ''},
'echeckRedeposit': {'cnpTxnId': '',
                   'customIdentifier': '',
                   'customerId': '',
                   'echeck': 'echeckType',
                   'echeckToken': 'echeckTokenType',
                   'id': '',
                   'merchantData': 'merchantDataType',
                   'reportGroup': ''},
'echeckSale': {'amount': '',
              'billToAddress': 'billToAddress',
              'cnpTxnId': '',
              'customBilling': 'customBilling',
              'customIdentifier': '',
              'customerId': '',
              'echeck': 'echeckType',
              'echeckToken': 'echeckTokenType',
              'id': '',
              'merchantData': 'merchantDataType',
              'orderId': '',
              'orderSource': '',
              'reportGroup': '',
              'secondaryAmount': '',
              'shipToAddress': 'shipToAddress',
              'verify': ''},
'echeckVerification': {'amount': '',
                      'billToAddress': 'billToAddress',
                      'customerId': '',
                      'echeck': 'echeckType',
                      'echeckToken': 'echeckTokenType',
                      'id': '',
                      'merchantData': 'merchantDataType',
                      'orderId': '',
                      'orderSource': '',
                      'reportGroup': ''},
'echeckVoid': {'cnpTxnId': '', 'customerId': '', 'id': '', 'reportGroup': ''},
'fastAccessFunding': {'amount': '',
                     'card': 'cardType',
                     'cardholderAddress': 'address',
                     'customerId': '',
                     'customerName': '',
                     'disbursementType': '',
                     'fundingCustomerId': '',
                     'fundingSubmerchantId': '',
                     'fundsTransferId': '',
                     'id': '',
                     'paypage': 'cardPaypageType',
                     'reportGroup': '',
                     'submerchantName': '',
                     'token': 'cardTokenType'},
'forceCapture': {'amount': '',
                'billToAddress': 'billToAddress',
                'businessIndicator': '',
                'card': 'cardType',
                'customBilling': 'customBilling',
                'customerId': '',
                'debtRepayment': '',
                'enhancedData': 'enhancedData',
                'id': '',
                'lodgingInfo': 'lodgingInfo',
                'merchantCategoryCode': '',
                'merchantData': 'merchantDataType',
                'mpos': 'mposType',
                'orderId': '',
                'orderSource': '',
                'paypage': 'cardPaypageType',
                'pos': 'pos',
                'processingInstructions': 'processingInstructions',
                'processingType': '',
                'reportGroup': '',
                'secondaryAmount': '',
                'surchargeAmount': '',
                'taxType': '',
                'token': 'cardTokenType'},
'fraudCheck': {'accountLogin': '',
              'accountPasshash': '',
              'advancedFraudChecks': 'advancedFraudChecksType',
              'amount': '',
              'billToAddress': 'billToAddress',
              'customerId': '',
              'eventType': '',
              'id': '',
              'reportGroup': '',
              'shipToAddress': 'shipToAddress'},
'fundingInstructionVoid': {'cnpTxnId': '',
                          'customerId': '',
                          'id': '',
                          'reportGroup': ''},
'giftCardAuthReversal': {'card': 'giftCardCardType',
                        'cnpTxnId': '',
                        'customerId': '',
                        'id': '',
                        'originalAmount': '',
                        'originalRefCode': '',
                        'originalSequenceNumber': '',
                        'originalSystemTraceId': '',
                        'originalTxnTime': '',
                        'reportGroup': ''},
'giftCardCapture': {'captureAmount': '',
                   'card': 'giftCardCardType',
                   'cnpTxnId': '',
                   'customerId': '',
                   'id': '',
                   'originalAmount': '',
                   'originalRefCode': '',
                   'originalTxnTime': '',
                   'partial': '',
                   'reportGroup': ''},
'giftCardCredit': {'card': 'giftCardCardType',
                  'cnpTxnId': '',
                  'creditAmount': '',
                  'customerId': '',
                  'id': '',
                  'orderId': '',
                  'orderSource': '',
                  'reportGroup': ''},
'load': {'amount': '',
        'card': 'giftCardCardType',
        'customerId': '',
        'id': '',
        'orderId': '',
        'orderSource': '',
        'reportGroup': ''},
'loadReversal': {'card': 'giftCardCardType',
                'cnpTxnId': '',
                'customerId': '',
                'id': '',
                'originalAmount': '',
                'originalRefCode': '',
                'originalSequenceNumber': '',
                'originalSystemTraceId': '',
                'originalTxnTime': '',
                'reportGroup': ''},
'payFacCredit': {'amount': '',
                'customerId': '',
                'fundingSubmerchantId': '',
                'fundsTransferId': '',
                'id': '',
                'reportGroup': ''},
'payFacDebit': {'amount': '',
               'customerId': '',
               'fundingSubmerchantId': '',
               'fundsTransferId': '',
               'id': '',
               'reportGroup': ''},
'payoutOrgCredit': {'amount': '',
                   'customerId': '',
                   'fundingCustomerId': '',
                   'fundsTransferId': '',
                   'id': '',
                   'reportGroup': ''},
'payoutOrgDebit': {'amount': '',
                  'customerId': '',
                  'fundingCustomerId': '',
                  'fundsTransferId': '',
                  'id': '',
                  'reportGroup': ''},
'physicalCheckCredit': {'amount': '',
                       'customerId': '',
                       'fundingCustomerId': '',
                       'fundingSubmerchantId': '',
                       'fundsTransferId': '',
                       'id': '',
                       'reportGroup': ''},
'physicalCheckDebit': {'amount': '',
                      'customerId': '',
                      'fundingCustomerId': '',
                      'fundingSubmerchantId': '',
                      'fundsTransferId': '',
                      'id': '',
                      'reportGroup': ''},
'queryTransaction': {'customerId': '',
                    'id': '',
                    'origActionType': '',
                    'origCnpTxnId': '',
                    'origId': '',
                    'reportGroup': '',
                    'showStatusOnly': ''},
'refundReversal': {'card': 'giftCardCardType',
                  'cnpTxnId': '',
                  'customerId': '',
                  'id': '',
                  'originalAmount': '',
                  'originalRefCode': '',
                  'originalSequenceNumber': '',
                  'originalSystemTraceId': '',
                  'originalTxnTime': '',
                  'reportGroup': ''},
'refundTransactionReversal': {'amount': '',
                             'cnpTxnId': '',
                             'customBilling': 'customBilling',
                             'customerId': '',
                             'enhancedData': 'enhancedData',
                             'id': '',
                             'lodgingInfo': 'lodgingInfo',
                             'pin': '',
                             'processingInstructions': 'processingInstructions',
                             'reportGroup': '',
                             'surchargeAmount': ''},
'registerTokenRequest': {'accountNumber': '',
                        'applepay': 'applepayType',
                        'cardValidationNum': '',
                        'customerId': '',
                        'echeckForToken': 'echeckForTokenType',
                        'encryptedAccountNumber': '',
                        'encryptedCardValidationNum': '',
                        'encryptionKeyId': '',
                        'id': '',
                        'mpos': 'mposType',
                        'orderId': '',
                        'paypageRegistrationId': '',
                        'reportGroup': ''},
'reserveCredit': {'amount': '',
                 'customerId': '',
                 'fundingCustomerId': '',
                 'fundingSubmerchantId': '',
                 'fundsTransferId': '',
                 'id': '',
                 'reportGroup': ''},
'reserveDebit': {'amount': '',
                'customerId': '',
                'fundingCustomerId': '',
                'fundingSubmerchantId': '',
                'fundsTransferId': '',
                'id': '',
                'reportGroup': ''},
'sale': {'additionalCOFData': 'additionalCOFData',
        'advancedFraudChecks': 'advancedFraudChecksType',
        'allowPartialAuth': '',
        'amount': '',
        'applepay': 'applepayType',
        'billToAddress': 'billToAddress',
        'businessIndicator': '',
        'card': 'cardType',
        'cardholderAuthentication': 'fraudCheckType',
        'cnpInternalRecurringRequest': 'cnpInternalRecurringRequestType',
        'cnpTxnId': '',
        'crypto': '',
        'customBilling': 'customBilling',
        'customerId': '',
        'customerInfo': 'customerInfo',
        'debtRepayment': '',
        'enhancedData': 'enhancedData',
        'filtering': 'filteringType',
        'fraudCheck': 'fraudCheckType',
        'fraudCheckStatus': '',
        'fraudFilterOverride': '',
        'giropay': 'giropayType',
        'healthcareIIAS': 'healthcareIIAS',
        'id': '',
        'ideal': 'idealType',
        'lodgingInfo': 'lodgingInfo',
        'merchantCategoryCode': '',
        'merchantData': 'merchantDataType',
        'mpos': 'mposType',
        'orderChannel': '',
        'orderId': '',
        'orderSource': '',
        'originalNetworkTransactionId': '',
        'originalTransactionAmount': '',
        'payPalNotes': '',
        'payPalOrderComplete': '',
        'paypage': 'cardPaypageType',
        'paypal': 'payPal',
        'pinlessDebitRequest': 'pinlessDebitRequestType',
        'pos': 'pos',
        'processingInstructions': 'processingInstructions',
        'processingType': '',
        'recurringRequest': 'recurringRequestType',
        'recyclingRequest': 'recyclingRequestType',
        'reportGroup': '',
        'retailerAddress': 'retailerAddress',
        'secondaryAmount': '',
        'sepaDirectDebit': 'sepaDirectDebitType',
        'shipToAddress': 'shipToAddress',
        'skipRealtimeAU': '',
        'sofort': 'sofortType',
        'surchargeAmount': '',
        'taxType': '',
        'token': 'cardTokenType',
        'wallet': 'wallet'},
'serviceStatusRequest': {'customerId': '',
                        'id': '',
                        'pathId': '',
                        'reportGroup': '',
                        'serviceId': ''},
'submerchantCredit': {'accountInfo': 'echeckType',
                     'amount': '',
                     'customIdentifier': '',
                     'customerId': '',
                     'fundingSubmerchantId': '',
                     'fundsTransferId': '',
                     'id': '',
                     'reportGroup': '',
                     'submerchantName': ''},
'submerchantDebit': {'accountInfo': 'echeckType',
                    'amount': '',
                    'customIdentifier': '',
                    'customerId': '',
                    'fundingSubmerchantId': '',
                    'fundsTransferId': '',
                    'id': '',
                    'reportGroup': '',
                    'submerchantName': ''},
'translateToLowValueTokenRequest': {'customerId': '',
                                   'id': '',
                                   'orderId': '',
                                   'reportGroup': '',
                                   'token': ''},
'unload': {'amount': '',
          'card': 'giftCardCardType',
          'customerId': '',
          'id': '',
          'orderId': '',
          'orderSource': '',
          'reportGroup': ''},
'unloadReversal': {'card': 'giftCardCardType',
                  'cnpTxnId': '',
                  'customerId': '',
                  'id': '',
                  'originalAmount': '',
                  'originalRefCode': '',
                  'originalSequenceNumber': '',
                  'originalSystemTraceId': '',
                  'originalTxnTime': '',
                  'reportGroup': ''},
'updateCardValidationNumOnToken': {'cardValidationNum': '',
                                  'cnpToken': '',
                                  'customerId': '',
                                  'id': '',
                                  'orderId': '',
                                  'reportGroup': ''},
'updatePlan': {'active': '', 'planCode': ''},
'updateSubscription': {'billToAddress': 'billToAddress',
                      'billingDate': '',
                      'card': 'cardType',
                      'createAddOn': 'createAddOnType',
                      'createDiscount': 'createDiscountType',
                      'deleteAddOn': 'deleteAddOnType',
                      'deleteDiscount': 'deleteDiscountType',
                      'paypage': 'cardPaypageType',
                      'planCode': '',
                      'subscriptionId': '',
                      'token': 'cardTokenType',
                      'updateAddOn': 'updateAddOnType',
                      'updateDiscount': 'updateDiscountType'},
'vendorCredit': {'accountInfo': 'echeckType',
                'amount': '',
                'customerId': '',
                'fundingCustomerId': '',
                'fundingSubmerchantId': '',
                'fundsTransferId': '',
                'id': '',
                'reportGroup': '',
                'vendorAddress': 'address',
                'vendorName': ''},
'vendorDebit': {'accountInfo': 'echeckType',
               'amount': '',
               'customerId': '',
               'fundingCustomerId': '',
               'fundingSubmerchantId': '',
               'fundsTransferId': '',
               'id': '',
               'reportGroup': '',
               'vendorAddress': 'address',
               'vendorName': ''},
'void': {'cnpTxnId': '',
        'customerId': '',
        'id': '',
        'processingInstructions': 'processingInstructions',
        'reportGroup': ''}}

used_type_dict = {'additionalCOFData': {'frequencyOfMIT': '',
                     'paymentType': '',
                     'sequenceIndicator': '',
                     'totalPaymentCount': '',
                     'uniqueId': '',
                     'validationReference': ''},
'address': {'addressLine1': '',
           'addressLine2': '',
           'addressLine3': '',
           'city': '',
           'country': '',
           'state': '',
           'zip': ''},
'advancedFraudChecksType': {'customAttribute1': '',
                           'customAttribute2': '',
                           'customAttribute3': '',
                           'customAttribute4': '',
                           'customAttribute5': '',
                           'threatMetrixSessionId': '',
                           'webSessionId': ''},
'advancedFraudResultsType': {'deviceReputationScore': '',
                            'deviceReviewStatus': '',
                            'triggeredRule': ''},
'applepayHeaderType': {'applicationData': '',
                      'ephemeralPublicKey': '',
                      'publicKeyHash': '',
                      'transactionId': ''},
'applepayType': {'data': '',
                'header': 'applepayHeaderType',
                'signature': '',
                'version': ''},
'authInformation': {'authAmount': '',
                   'authCode': '',
                   'authDate': '',
                   'fraudResult': 'fraudResult'},
'billToAddress': {'addressLine1': '',
                 'addressLine2': '',
                 'addressLine3': '',
                 'city': '',
                 'companyName': '',
                 'country': '',
                 'email': '',
                 'firstName': '',
                 'lastName': '',
                 'middleInitial': '',
                 'name': '',
                 'phone': '',
                 'sellerId': '',
                 'state': '',
                 'url': '',
                 'zip': ''},
'card': {'cardValidationNum': '',
        'expDate': '',
        'number': '',
        'pin': '',
        'track': '',
        'type': ''},
'cardPaypageType': {'cardValidationNum': '',
                   'expDate': '',
                   'paypageRegistrationId': '',
                   'type': ''},
'cardTokenType': {'authenticatedShopperID': '',
                 'cardValidationNum': '',
                 'checkoutId': '',
                 'cnpToken': '',
                 'expDate': '',
                 'tokenURL': '',
                 'type': ''},
'cardType': {'cardValidationNum': '',
            'expDate': '',
            'number': '',
            'pin': '',
            'track': '',
            'type': ''},
'cnpInternalRecurringRequestType': {'finalPayment': '',
                                   'recurringTxnId': '',
                                   'subscriptionId': ''},
'createAddOnType': {'addOnCode': '',
                   'amount': '',
                   'endDate': '',
                   'name': '',
                   'startDate': ''},
'createDiscountType': {'amount': '',
                      'discountCode': '',
                      'endDate': '',
                      'name': '',
                      'startDate': ''},
'customBilling': {'city': '', 'descriptor': '', 'phone': '', 'url': ''},
'customerInfo': {'accountCreatedDate': '',
                'accountUsername': '',
                'customerCheckingAccount': '',
                'customerRegistrationDate': '',
                'customerSavingAccount': '',
                'customerType': '',
                'customerWorkTelephone': '',
                'dob': '',
                'employerName': '',
                'incomeAmount': '',
                'incomeCurrency': '',
                'membershipEmail': '',
                'membershipId': '',
                'membershipName': '',
                'membershipPhone': '',
                'residenceStatus': '',
                'ssn': '',
                'userAccountEmail': '',
                'userAccountNumber': '',
                'userAccountPhone': '',
                'yearsAtEmployer': '',
                'yearsAtResidence': ''},
'deleteAddOnType': {'addOnCode': ''},
'deleteDiscountType': {'discountCode': ''},
'detailTax': {'cardAcceptorTaxId': '',
             'taxAmount': '',
             'taxIncludedInTotal': '',
             'taxRate': '',
             'taxTypeIdentifier': ''},
'echeckForTokenType': {'accNum': '', 'routingNum': ''},
'echeckTokenType': {'accType': '',
                   'checkNum': '',
                   'cnpToken': '',
                   'routingNum': ''},
'echeckType': {'accNum': '',
              'accType': '',
              'ccdPaymentInformation': '',
              'checkNum': '',
              'routingNum': ''},
'enhancedData': {'customerReference': '',
                'deliveryType': '',
                'destinationCountryCode': '',
                'destinationPostalCode': '',
                'detailTax': 'detailTax',
                'discountAmount': '',
                'discountCode': '',
                'discountPercent': '',
                'dutyAmount': '',
                'fulfilmentMethodType': '',
                'invoiceReferenceNumber': '',
                'lineItemData': 'lineItemData',
                'orderDate': '',
                'salesTax': '',
                'shipFromPostalCode': '',
                'shippingAmount': '',
                'taxExempt': ''},
'filteringType': {'chargeback': '', 'international': '', 'prepaid': ''},
'fraudCheckType': {'authenticatedByMerchant': '',
                  'authenticationProtocolVersion': '',
                  'authenticationTransactionId': '',
                  'authenticationValue': '',
                  'customerIpAddress': '',
                  'tokenAuthenticationValue': ''},
'fraudResult': {'advancedAVSResult': '',
               'advancedFraudResults': 'advancedFraudResultsType',
               'authenticationResult': '',
               'avsResult': '',
               'cardValidationResult': ''},
'giftCardCardType': {'cardValidationNum': '',
                    'expDate': '',
                    'number': '',
                    'pin': '',
                    'track': '',
                    'type': ''},
'giropayType': {'preferredLanguage': ''},
'healthcareAmounts': {'RxAmount': '',
                     'clinicOtherAmount': '',
                     'copayAmount': '',
                     'dentalAmount': '',
                     'totalHealthcareAmount': '',
                     'visionAmount': ''},
'healthcareIIAS': {'IIASFlag': '', 'healthcareAmounts': 'healthcareAmounts'},
'idealType': {'preferredLanguage': ''},
'lineItemData': {'commodityCode': '',
                'detailTax': 'detailTax',
                'itemCategory': '',
                'itemDescription': '',
                'itemDiscountAmount': '',
                'itemSequenceNumber': '',
                'itemSubCategory': '',
                'lineItemTotal': '',
                'lineItemTotalWithTax': '',
                'productCode': '',
                'productId': '',
                'productName': '',
                'quantity': '',
                'taxAmount': '',
                'unitCost': '',
                'unitOfMeasure': ''},
'lodgingCharge': {'name': ''},
'lodgingInfo': {'checkInDate': '',
               'checkOutDate': '',
               'customerServicePhone': '',
               'duration': '',
               'fireSafetyIndicator': '',
               'hotelFolioNumber': '',
               'lodgingCharge': 'lodgingCharge',
               'numAdults': '',
               'programCode': '',
               'propertyLocalPhone': '',
               'roomRate': '',
               'roomTax': ''},
'merchantDataType': {'affiliate': '', 'campaign': '', 'merchantGroupingId': ''},
'mposType': {'encryptedTrack': '',
            'formatId': '',
            'ksn': '',
            'track1Status': '',
            'track2Status': ''},
'payPal': {'payerEmail': '',
          'payerId': '',
          'token': 'cardTokenType',
          'transactionId': ''},
'pinlessDebitRequestType': {'preferredDebitNetworks': 'preferredDebitNetworksType',
                           'routingPreference': ''},
'pos': {'capability': '',
       'cardholderId': '',
       'catLevel': '',
       'entryMode': '',
       'terminalId': ''},
'preferredDebitNetworksType': {'debitNetworkName': ''},
'processingInstructions': {'bypassVelocityCheck': ''},
'recurringRequestType': {'createSubscription': 'recurringSubscriptionType'},
'recurringSubscriptionType': {'amount': '',
                             'createAddOn': 'createAddOnType',
                             'createDiscount': 'createDiscountType',
                             'numberOfPayments': '',
                             'planCode': '',
                             'startDate': ''},
'recyclingRequestType': {'recycleBy': '', 'recycleId': ''},
'retailerAddress': {'addressLine1': '',
                   'addressLine2': '',
                   'addressLine3': '',
                   'city': '',
                   'companyName': '',
                   'country': '',
                   'email': '',
                   'firstName': '',
                   'lastName': '',
                   'middleInitial': '',
                   'name': '',
                   'phone': '',
                   'sellerId': '',
                   'state': '',
                   'url': '',
                   'zip': ''},
'sepaDirectDebitType': {'iban': '',
                       'mandateProvider': '',
                       'mandateReference': '',
                       'mandateSignatureDate': '',
                       'mandateUrl': '',
                       'preferredLanguage': '',
                       'sequenceType': ''},
'shipToAddress': {'addressLine1': '',
                 'addressLine2': '',
                 'addressLine3': '',
                 'city': '',
                 'companyName': '',
                 'country': '',
                 'email': '',
                 'firstName': '',
                 'lastName': '',
                 'middleInitial': '',
                 'name': '',
                 'phone': '',
                 'sellerId': '',
                 'state': '',
                 'url': '',
                 'zip': ''},
'sofortType': {'preferredLanguage': ''},
'token': {'authenticatedShopperID': '',
         'cardValidationNum': '',
         'checkoutId': '',
         'cnpToken': '',
         'expDate': '',
         'tokenURL': '',
         'type': ''},
'updateAddOnType': {'addOnCode': '',
                   'amount': '',
                   'endDate': '',
                   'name': '',
                   'startDate': ''},
'updateDiscountType': {'amount': '',
                      'discountCode': '',
                      'endDate': '',
                      'name': '',
                      'startDate': ''},
'virtualGiftCardType': {'accountNumberLength': '', 'giftCardBin': ''},
'wallet': {'walletSourceType': '', 'walletSourceTypeId': ''}}

abs_class_dict = {'cardOrToken': ['card', 'token']}
