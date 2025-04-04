from django.db import models
from pybirdai.annotations.decorators import lineage

class ASST_PL(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	ASST_PL_uniqueID = models.CharField("ASST_PL_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	ASST_PL_ID = models.CharField("ASST_PL_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ASST_PL_TYP_domain = {		"1":"Asset_pool_subject_to_a_Covered_bond_programme",
		"2":"Asset_pool_subject_to_a_credit_transfer_other_than_securitisation_and_covered_bond_programme",
		"3":"Asset_pool_subject_to_a_Securitisation",
}

	ASST_PL_TYP = models.CharField("ASST_PL_TYP",max_length=255, choices=ASST_PL_TYP_domain,default=None, blank=True, null=True, db_comment="ASST_PL_TYP_domain")

	ASST_SPCFC_VL = models.BigIntegerField("ASST_SPCFC_VL",default=None, blank=True, null=True)

	CRRYNG_AMNT = models.BigIntegerField("CRRYNG_AMNT",default=None, blank=True, null=True)

	PRMRY_ASST_CLSS_CVR_PL_INPT_domain = {		"0":"Not_applicable",
		"a":"Exposures_to_or_guaranteed_by_central_governments_ESCB_central_banks_public_sector_entities_regional_governments_or_local_authorities_in_the_Union",
		"b":"Exposures_to_or_guaranteed_by_third_country_central_governments_third_country_central_banks_multilateral_development_banks_international_organisations_that_fullfill_specific_requirements",
		"c":"Exposures_to_institutions_that_fullfilll_specific_requirements",
		"d":"Loans_secured_by_i_residential_property_or_ii_senior_units_issued_by_French_Fonds_Communs_de_Titrisation_or_equivalent_securitisation_entities_governed_by_the_laws_of_a_Member_State_securitising_residential_property_exposures",
		"e":"Residential_loans_fully_guaranteed_by_an_eligible_rpotection_provider",
		"f":"Loans_secured_by_i_commercial_immovable_property_or_ii_senior_units_issued_by_French_Fonds_Communs_de_Titrisation_or_equivalent_securitisation_entities_governed_by_the_law_of_a_Member_State_securitising_commercial_immovable_property_exposures",
		"g":"Loans_secured_by_maritime_liens_on_ships_up_to_the_difference_between_60_of_the_value_of_the_pledged_ship_and_the_value_of_any_prior_maritime_liens",
		"h":"Other_exposures",
}

	PRMRY_ASST_CLSS_CVR_PL = models.CharField("PRMRY_ASST_CLSS_CVR_PL",max_length=255, choices=PRMRY_ASST_CLSS_CVR_PL_INPT_domain,default=None, blank=True, null=True, db_comment="PRMRY_ASST_CLSS_CVR_PL_INPT_domain")

	PRSNT_VL = models.BigIntegerField("PRSNT_VL",default=None, blank=True, null=True)

	TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT_domain = {		"1":"Entirely_recognised_Instrument_entirely_recognised_in_accordance_with_Implementing_Regulation_EU_No_680_2014",
		"2":"Recognised_to_the_extent_of_the_institution_s_continuing_involvement_Instrument_recognised_to_the_extent_of_the_institution_s_continuing_involvement_in_accordance_with_Implementing_Regulation_EU_No_680_2014",
		"3":"Entirely_derecognised_Instrument_entirely_derecognised_in_accordance_with_Implementing_Regulation_EU_No_680_2014",
}

	TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT = models.CharField("TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT",max_length=255, choices=TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT_domain,default=None, blank=True, null=True, db_comment="TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT_domain")

	class Meta:

		verbose_name = 'ASST_PL'

		verbose_name_plural = 'ASST_PLs'

class ASST_PL_CLLTRL_RCVD_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	ASST_PL_CLLTRL_RCVD_ASSGNMNT_uniqueID = models.CharField("ASST_PL_CLLTRL_RCVD_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	ASST_PL_ID = models.CharField("ASST_PL_ID",max_length=255,default=None, blank=True, null=True)

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	CLLTRL_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"1":"Collateral_received",
		"2":"Collateral_given",
}

	CLLTRL_RL_TYP = models.CharField("CLLTRL_RL_TYP",max_length=255, choices=CLLTRL_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="CLLTRL_RL_TYP_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	TRNSFRRD_AMNT = models.BigIntegerField("TRNSFRRD_AMNT",default=None, blank=True, null=True)

	theASST_PL = models.ForeignKey("ASST_PL", models.SET_NULL,blank=True,null=True,related_name="ASST_PL_CLLTRL_RCVD_ASSGNMNT_to_theASST_PLs")

	theCLLTRL_RL = models.ForeignKey("CLLTRL_RL", models.SET_NULL,blank=True,null=True,related_name="ASST_PL_CLLTRL_RCVD_ASSGNMNT_to_theCLLTRL_RLs")

	class Meta:

		verbose_name = 'ASST_PL_CLLTRL_RCVD_ASSGNMNT'

		verbose_name_plural = 'ASST_PL_CLLTRL_RCVD_ASSGNMNTs'

class ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT_uniqueID = models.CharField("ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	ASST_PL_ID = models.CharField("ASST_PL_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	TRNSFRRD_AMNT = models.BigIntegerField("TRNSFRRD_AMNT",default=None, blank=True, null=True)

	theASST_PL = models.ForeignKey("ASST_PL", models.SET_NULL,blank=True,null=True,related_name="ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT_to_theASST_PLs")

	theSCRTY_PSTN = models.ForeignKey("SCRTY_PSTN", models.SET_NULL,blank=True,null=True,related_name="ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT_to_theSCRTY_PSTNs")

	class Meta:

		verbose_name = 'ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT'

		verbose_name_plural = 'ASST_PL_DBT_SCRTY_PSTN_ASSGNMNTs'

class ASST_PL_EXCHNG_TRDBL_DRVTV_PSTN_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	ASST_PL_EXCHNG_TRDBL_DRVTV_PSTN_ASSGNMNT_uniqueID = models.CharField("ASST_PL_EXCHNG_TRDBL_DRVTV_PSTN_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	ASST_PL_ID = models.CharField("ASST_PL_ID",max_length=255,default=None, blank=True, null=True)

	BYR_PRTY_ID = models.CharField("BYR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	BYR_PRTY_RL_TYP = models.CharField("BYR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	SLLR_PRTY_ID = models.CharField("SLLR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	SLLR_PRTY_RL_TYP = models.CharField("SLLR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	NTNL_AMNT = models.BigIntegerField("NTNL_AMNT",default=None, blank=True, null=True)

	theASST_PL = models.ForeignKey("ASST_PL", models.SET_NULL,blank=True,null=True,related_name="ASST_PL_EXCHNG_TRDBL_DRVTV_PSTN_ASSGNMNT_to_theASST_PLs")

	theEXCHNG_TRDBL_DRVTV_PSTN = models.ForeignKey("EXCHNG_TRDBL_DRVTV_PSTN", models.SET_NULL,blank=True,null=True,related_name="ASST_PL_EXCHNG_TRDBL_DRVTV_PSTN_ASSGNMNT_to_theEXCHNG_TRDBL_DRVTV_PSTNs")

	class Meta:

		verbose_name = 'ASST_PL_EXCHNG_TRDBL_DRVTV_PSTN_ASSGNMNT'

		verbose_name_plural = 'ASST_PL_EXCHNG_TRDBL_DRVTV_PSTN_ASSGNMNTs'

class ASST_PL_INSTRMNT_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	ASST_PL_INSTRMNT_ASSGNMNT_uniqueID = models.CharField("ASST_PL_INSTRMNT_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	ASST_PL_ID = models.CharField("ASST_PL_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ASST_PL_INSTRMNT_ASSGNMNT_TYP_domain = {		"1":"Asset_pool_Equity_instrument_that_is_not_a_security_assignment",
		"2":"Asset_pool_Loan_excluding_repurchase_agreement_assignment",
		"3":"Asset_pool_Over_the_counter_OTC_Derivative_instrument_assignment",
}

	ASST_PL_INSTRMNT_ASSGNMNT_TYP = models.CharField("ASST_PL_INSTRMNT_ASSGNMNT_TYP",max_length=255, choices=ASST_PL_INSTRMNT_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="ASST_PL_INSTRMNT_ASSGNMNT_TYP_domain")

	PRCNTG_RTND = models.FloatField("PRCNTG_RTND",default=None, blank=True, null=True)

	PRCNTG_TRNSFRD = models.FloatField("PRCNTG_TRNSFRD",default=None, blank=True, null=True)

	theASST_PL = models.ForeignKey("ASST_PL", models.SET_NULL,blank=True,null=True,related_name="ASST_PL_INSTRMNT_ASSGNMNT_to_theASST_PLs")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="ASST_PL_INSTRMNT_ASSGNMNT_to_theINSTRMNTs")

	class Meta:

		verbose_name = 'ASST_PL_INSTRMNT_ASSGNMNT'

		verbose_name_plural = 'ASST_PL_INSTRMNT_ASSGNMNTs'

class BLNC_SHT_NTTNG(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	BLNC_SHT_NTTNG_uniqueID = models.CharField("BLNC_SHT_NTTNG_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	BLNC_SHT_NTTNG_ID = models.CharField("BLNC_SHT_NTTNG_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	class Meta:

		verbose_name = 'BLNC_SHT_NTTNG'

		verbose_name_plural = 'BLNC_SHT_NTTNGs'

class CLLTRL(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CLLTRL_uniqueID = models.CharField("CLLTRL_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ACCMLTD_CHNG_NGTV = models.BigIntegerField("ACCMLTD_CHNG_NGTV",default=None, blank=True, null=True)

	ACCMLTD_CHNGS_FV_CR = models.BigIntegerField("ACCMLTD_CHNGS_FV_CR",default=None, blank=True, null=True)

	ACCMLTD_IMPRMNT = models.BigIntegerField("ACCMLTD_IMPRMNT",default=None, blank=True, null=True)

	OBTND_CLLTRL_RCVD_INSTRMNT_TYP_INPT_domain = {		"0":"Not_applicable",
		"71":"Collateral_received_instrument_obtained_by_taking_possession",
		"72":"Not_obtained_collateral_received_instrument",
}

	CLLTRL_OBTND_TYP = models.CharField("CLLTRL_OBTND_TYP",max_length=255, choices=OBTND_CLLTRL_RCVD_INSTRMNT_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="OBTND_CLLTRL_RCVD_INSTRMNT_TYP_INPT_domain")

	CLLTRL_RS_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Collateral_used_once",
		"2":"Collateral_reused",
}

	CLLTRL_RS_INDCTR = models.CharField("CLLTRL_RS_INDCTR",max_length=255, choices=CLLTRL_RS_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="CLLTRL_RS_INDCTR_INPT_domain")

	ISO4217_INPT_domain = {		"0":"Not_applicable",
		"AED":"UAE_Dirham",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"ARS":"Argentine_Peso",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYN":"Belarussian_Ruble",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHE":"WIR_Euro",
		"CHF":"Swiss_franc",
		"CHW":"WIR_Franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CZK":"Czech_koruna",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GTQ":"Quetzal",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"ILS":"New_Israeli_Sheqel",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MRU":"Ouguiya_x2",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDG":"Sudanese_Pound",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SRD":"Surinam_Dollar",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"STN":"Dobra_x2",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJS":"Somoni",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"USN":"US_Dollar_Next_day",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UYW":"Unidad_Previsional",
		"UZS":"Uzbekistan_Sum",
		"VEF":"Bolivar",
		"VES":"Bolivar_Soberano",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XAG":"Silver_one_Troy_ounce",
		"XAU":"Gold_one_Troy_ounce",
		"XBA":"Bond_Markets_Unit_European_Composite_Unit_EURCO",
		"XBB":"Bond_Markets_Unit_European_Monetary_Unit_E_M_U_6",
		"XBC":"Bond_Markets_Unit_European_Unit_of_Account_9_E_U_A_9",
		"XBD":"Bond_Markets_Unit_European_Unit_of_Account_17_E_U_A_17",
		"XCD":"East_Caribbean_Dollar",
		"XDR":"Special_Drawing_Rights_SDR",
		"XOF":"CFA_Franc_BCEAO",
		"XPD":"Palladium_one_Troy_ounce",
		"XPF":"CFP_Franc",
		"XPT":"Platinum_one_Troy_ounce",
		"XSU":"Sucre",
		"XTS":"Codes_specifically_reserved_for_testing_purposes",
		"XUA":"ADB_Unit_of_Account",
		"XXX":"Code_assigned_for_transactions_where_no_currency_is_involved",
		"YER":"Yemeni_Rial",
		"ZAR":"South_African_Rand",
		"ZMW":"Zambian_Kwacha",
		"ZWL":"Zimbabwe_Dollar",
}

	CRRNCY = models.CharField("CRRNCY",max_length=255, choices=ISO4217_INPT_domain,default=None, blank=True, null=True, db_comment="ISO4217_INPT_domain")

	CRRYNG_AMNT = models.BigIntegerField("CRRYNG_AMNT",default=None, blank=True, null=True)

	DT_ORGNL_PRTCTN_VL = models.DateTimeField("DT_ORGNL_PRTCTN_VL",default=None, blank=True, null=True)

	DT_PRTCTN_VL = models.DateTimeField("DT_PRTCTN_VL",default=None, blank=True, null=True)

	ENCMBRD_ASST_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Not_encumbered_asset",
		"100":"Encumbered_asset",
}

	ENCMBRD_ASST_INDCTR = models.CharField("ENCMBRD_ASST_INDCTR",max_length=255, choices=ENCMBRD_ASST_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="ENCMBRD_ASST_INDCTR_INPT_domain")

	FV = models.BigIntegerField("FV",default=None, blank=True, null=True)

	GCA_EXPSR_DRCGNSD_EXCHNG_CLLTRL = models.BigIntegerField("GCA_EXPSR_DRCGNSD_EXCHNG_CLLTRL",default=None, blank=True, null=True)

	INTL_RCGNTN_VL = models.BigIntegerField("INTL_RCGNTN_VL",default=None, blank=True, null=True)

	LT_SSTNBL_VL = models.BigIntegerField("LT_SSTNBL_VL",default=None, blank=True, null=True)

	MRKT_VL = models.BigIntegerField("MRKT_VL",default=None, blank=True, null=True)

	ISO3166_INPT_domain = {		"0":"Not_applicable",
		"AD":"Andorra",
		"AE":"United_Arab_Emirates_the",
		"AF":"Afghanistan",
		"AG":"Antigua_and_Barbuda",
		"AI":"Anguilla",
		"AL":"Albania",
		"AM":"Armenia",
		"AO":"Angola",
		"AQ":"Antarctica",
		"AR":"Argentina",
		"AS":"American_Samoa",
		"AT":"Austria",
		"AU":"Australia",
		"AW":"Aruba",
		"AX":"Aland_Islands",
		"AZ":"Azerbaijan",
		"BA":"Bosnia_and_Herzegovina",
		"BB":"Barbados",
		"BD":"Bangladesh",
		"BE":"Belgium",
		"BF":"Burkina_Faso",
		"BG":"Bulgaria",
		"BH":"Bahrain",
		"BI":"Burundi",
		"BJ":"Benin",
		"BL":"Saint_Barthelemy",
		"BM":"Bermuda",
		"BN":"Brunei_Darussalam",
		"BO":"Bolivia_Plurinational_State_of",
		"BQ":"Bonaire_Saint_Eustatius_and_Saba",
		"BR":"Brazil",
		"BS":"Bahamas_the",
		"BT":"Bhutan",
		"BV":"Bouvet_Island",
		"BW":"Botswana",
		"BY":"Belarus",
		"BZ":"Belize",
		"CA":"Canada",
		"CC":"Cocos_Keeling_Islands_the",
		"CD":"Congo_the_Democratic_Republic_of_the",
		"CF":"Central_African_Republic_the",
		"CG":"Congo_the",
		"CH":"Switzerland",
		"CI":"Cote_d_Ivoire",
		"CK":"Cook_Islands_the",
		"CL":"Chile",
		"CM":"Cameroon",
		"CN":"China_China_excluding_Taiwan_TW_Hong_Kong_HK_Macao_MO",
		"CO":"Colombia",
		"CR":"Costa_Rica",
		"CU":"Cuba",
		"CV":"Cabo_Verde",
		"CW":"Curacao",
		"CX":"Christmas_Island",
		"CY":"Cyprus",
		"CZ":"Czechia",
		"DE":"Germany",
		"DJ":"Djibouti",
		"DK":"Denmark",
		"DM":"Dominica",
		"DO":"Dominican_Republic_the",
		"DZ":"Algeria",
		"EC":"Ecuador",
		"EE":"Estonia",
		"EG":"Egypt",
		"EH":"Western_Sahara",
		"ER":"Eritrea",
		"ES":"Spain",
		"ET":"Ethiopia",
		"FI":"Finland_Finland_excluding_Aland_AX",
		"FJ":"Fiji",
		"FK":"Falkland_Islands_the_Malvinas",
		"FM":"Micronesia_Federated_States_of",
		"FO":"Faroe_Islands_the",
		"FR":"France_France_excluding_Guadeloupe_GP_Guyane_GF_La_Reunion_RE_Martinique_MQ_Mayotte_YT_Nouvelle_Caledonie_NC_Polynesie_francaise_PF_Saint_Barthelemy_BL_Saint_Martin_MF_Saint_Pierre_et_Miquelon_PM_Terres_australes_francaises_TF_Wallis_et_Futuna_WF",
		"GA":"Gabon",
		"GB":"United_Kingdom_of_Great_Britain_and_Northern_Ireland_the",
		"GD":"Grenada",
		"GE":"Georgia",
		"GF":"French_Guiana",
		"GG":"Guernsey",
		"GH":"Ghana",
		"GI":"Gibraltar",
		"GL":"Greenland",
		"GM":"Gambia_the",
		"GN":"Guinea",
		"GP":"Guadeloupe",
		"GQ":"Equatorial_Guinea",
		"GR":"Greece",
		"GS":"South_Georgia_and_the_South_Sandwich_Islands",
		"GT":"Guatemala",
		"GU":"Guam",
		"GW":"Guinea_Bissau",
		"GY":"Guyana",
		"HK":"Hong_Kong",
		"HM":"Heard_Island_and_McDonald_Islands",
		"HN":"Honduras",
		"HR":"Croatia",
		"HT":"Haiti",
		"HU":"Hungary",
		"ID":"Indonesia",
		"IE":"Ireland",
		"IL":"Israel",
		"IM":"Isle_of_Man",
		"IN":"India",
		"IO":"British_Indian_Ocean_Territory_the",
		"IQ":"Iraq",
		"IR":"Iran_Islamic_Republic_of",
		"IS":"Iceland",
		"IT":"Italy",
		"JE":"Jersey",
		"JM":"Jamaica",
		"JO":"Jordan",
		"JP":"Japan",
		"KE":"Kenya",
		"KG":"Kyrgyzstan",
		"KH":"Cambodia",
		"KI":"Kiribati",
		"KM":"Comoros_the",
		"KN":"Saint_Kitts_and_Nevis",
		"KP":"Korea_the_Democratic_People_s_Republic_of",
		"KR":"Korea_the_Republic_of",
		"KW":"Kuwait",
		"KY":"Cayman_Islands_the",
		"KZ":"Kazakhstan",
		"LA":"Lao_People_s_Democratic_Republic_the",
		"LB":"Lebanon",
		"LC":"Saint_Lucia",
		"LI":"Liechtenstein",
		"LK":"Sri_Lanka",
		"LR":"Liberia",
		"LS":"Lesotho",
		"LT":"Lithuania",
		"LU":"Luxembourg",
		"LV":"Latvia",
		"LY":"Libya",
		"MA":"Morocco",
		"MC":"Monaco",
		"MD":"Moldova_the_Republic_of",
		"ME":"Montenegro",
		"MF":"Saint_Martin_French_part",
		"MG":"Madagascar",
		"MH":"Marshall_Islands_the",
		"MK":"Macedonia_the_former_Yugoslav_Republic_of",
		"ML":"Mali",
		"MM":"Myanmar",
		"MN":"Mongolia",
		"MO":"Macao",
		"MP":"Northern_Mariana_Islands_the",
		"MQ":"Martinique",
		"MR":"Mauritania",
		"MS":"Montserrat",
		"MT":"Malta",
		"MU":"Mauritius",
		"MV":"Maldives",
		"MW":"Malawi",
		"MX":"Mexico",
		"MY":"Malaysia",
		"MZ":"Mozambique",
		"NA":"Namibia",
		"NC":"New_Caledonia",
		"NE":"Niger_the",
		"NF":"Norfolk_Island",
		"NG":"Nigeria",
		"NI":"Nicaragua",
		"NL":"Netherlands_the_Netherlands_excluding_Aruba_AW_Bonaire_Saint_Eustatius_and_Saba_BQ_Curacao_CW_Sint_Maarten_SX",
		"NO":"Norway_Norway_excluding_Svalbard_and_Jan_Mayen_SJ",
		"NP":"Nepal",
		"NR":"Nauru",
		"NU":"Niue",
		"NZ":"New_Zealand",
		"OM":"Oman",
		"PA":"Panama",
		"PE":"Peru",
		"PF":"French_Polynesia",
		"PG":"Papua_New_Guinea",
		"PH":"Philippines_the",
		"PK":"Pakistan",
		"PL":"Poland",
		"PM":"Saint_Pierre_and_Miquelon",
		"PN":"Pitcairn",
		"PR":"Puerto_Rico",
		"PS":"Palestine_State_of",
		"PT":"Portugal",
		"PW":"Palau",
		"PY":"Paraguay",
		"QA":"Qatar",
		"RE":"Reunion",
		"RO":"Romania",
		"RS":"Serbia",
		"RU":"Russian_Federation_the",
		"RW":"Rwanda",
		"SA":"Saudi_Arabia",
		"SB":"Solomon_Islands",
		"SC":"Seychelles",
		"SD":"Sudan_the",
		"SE":"Sweden",
		"SG":"Singapore",
		"SH":"Saint_Helena_Ascension_and_Tristan_da_Cunha",
		"SI":"Slovenia",
		"SJ":"Svalbard_and_Jan_Mayen",
		"SK":"Slovakia",
		"SL":"Sierra_Leone",
		"SM":"San_Marino",
		"SN":"Senegal",
		"SO":"Somalia",
		"SR":"Suriname",
		"SS":"South_Sudan",
		"ST":"Sao_Tome_and_Principe",
		"SV":"El_Salvador",
		"SX":"Sint_Maarten_Dutch_part",
		"SY":"Syrian_Arab_Republic",
		"SZ":"Swaziland",
		"TC":"Turks_and_Caicos_Islands_the",
		"TD":"Chad",
		"TF":"French_Southern_Territories_the",
		"TG":"Togo",
		"TH":"Thailand",
		"TJ":"Tajikistan",
		"TK":"Tokelau",
		"TL":"Timor_Leste",
		"TM":"Turkmenistan",
		"TN":"Tunisia",
		"TO":"Tonga",
		"TR":"Turkey",
		"TT":"Trinidad_and_Tobago",
		"TV":"Tuvalu",
		"TW":"Taiwan_Province_of_China",
		"TZ":"Tanzania_United_Republic_of",
		"UA":"Ukraine",
		"UG":"Uganda",
		"UM":"United_States_Minor_Outlying_Islands_the",
		"US":"United_States_of_America_the_United_States_excluding_American_Samoa_AS_Guam_GU_Northern_Mariana_Islands_MP_Puerto_Rico_PR_United_States_Minor_Outlying_Islands_UM_Virgin_Islands_U_S_VI",
		"UY":"Uruguay",
		"UZ":"Uzbekistan",
		"VA":"Holy_See_the",
		"VC":"Saint_Vincent_and_the_Grenadines",
		"VE":"Venezuela_Bolivarian_Republic_of",
		"VG":"Virgin_Islands_British",
		"VI":"Virgin_Islands_U_S",
		"VN":"Viet_Nam",
		"VU":"Vanuatu",
		"WF":"Wallis_and_Futuna",
		"WS":"Samoa",
		"YE":"Yemen",
		"YT":"Mayotte",
		"ZA":"South_Africa",
		"ZM":"Zambia",
		"ZW":"Zimbabwe",
}

	NN_MMBR_STT_CNTRY_CD = models.CharField("NN_MMBR_STT_CNTRY_CD",max_length=255, choices=ISO3166_INPT_domain,default=None, blank=True, null=True, db_comment="ISO3166_INPT_domain")

	NTNL_AMNT = models.BigIntegerField("NTNL_AMNT",default=None, blank=True, null=True)

	ORGNL_PRTCTN_VL = models.BigIntegerField("ORGNL_PRTCTN_VL",default=None, blank=True, null=True)

	PLNNNG_PRMSSN_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Land_with_planning_permission_for_developnment",
		"2":"Land_without_planning_permission_for_development",
}

	PLNNNG_PRMSSN_INDCTR = models.CharField("PLNNNG_PRMSSN_INDCTR",max_length=255, choices=PLNNNG_PRMSSN_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="PLNNNG_PRMSSN_INDCTR_INPT_domain")

	PSTL_CD = models.CharField("PSTL_CD",max_length=255,default=None, blank=True, null=True)

	RL_ESTT_CLLTRL_LCTN_TYP = models.FloatField("RL_ESTT_CLLTRL_LCTN_TYP",default=None, blank=True, null=True)

	TKN_PSSSSN_DT = models.DateTimeField("TKN_PSSSSN_DT",default=None, blank=True, null=True)

	TM_SNC_INTL_RCGNTN_domain = {		"27":"_lt_eq_2_years",
		"29":"_gt_2_years_lt_eq_5_years",
		"37":"_gt_5_years",
}

	TM_SNC_INTL_RCGNTN = models.CharField("TM_SNC_INTL_RCGNTN",max_length=255, choices=TM_SNC_INTL_RCGNTN_domain,default=None, blank=True, null=True, db_comment="TM_SNC_INTL_RCGNTN_domain")

	NUTS3_INPT_domain = {		"0":"Not_applicable",
		"AT111":"Mittelburgenland",
		"AT112":"Nordburgenland",
		"AT113":"Sudburgenland",
		"AT121":"Mostviertel_Eisenwurzen",
		"AT122":"Niederosterreich_Sud",
		"AT123":"Sankt_Polten",
		"AT124":"Waldviertel",
		"AT125":"Weinviertel",
		"AT126":"Wiener_Umland_Nordteil",
		"AT127":"Wiener_Umland_Sudteil",
		"AT130":"Wien",
		"AT211":"Klagenfurt_Villach",
		"AT212":"Oberkarnten",
		"AT213":"Unterkarnten",
		"AT221":"Graz",
		"AT222":"Liezen",
		"AT223":"Ostliche_Obersteiermark",
		"AT224":"Oststeiermark",
		"AT225":"West_und_Sudsteiermark",
		"AT226":"Westliche_Obersteiermark",
		"AT311":"Innviertel",
		"AT312":"Linz_Wels",
		"AT313":"Muhlviertel",
		"AT314":"Steyr_Kirchdorf",
		"AT315":"Traunviertel",
		"AT321":"Lungau",
		"AT322":"Pinzgau_Pongau",
		"AT323":"Salzburg_und_Umgebung",
		"AT331":"Ausserfern",
		"AT332":"Innsbruck",
		"AT333":"Osttirol",
		"AT334":"Tiroler_Oberland",
		"AT335":"Tiroler_Unterland",
		"AT341":"Bludenz_Bregenzer_Wald",
		"AT342":"Rheintal_Bodenseegebiet",
		"ATZZZ":"Extra_Regio_NUTS_3",
		"BE100":"Arr_de_Bruxelles_Capitale_Arr_van_Brussel_Hoofdstad",
		"BE211":"Arr_Antwerpen",
		"BE212":"Arr_Mechelen",
		"BE213":"Arr_Turnhout",
		"BE221":"Arr_Hasselt",
		"BE222":"Arr_Maaseik",
		"BE223":"Arr_Tongeren",
		"BE231":"Arr_Aalst",
		"BE232":"Arr_Dendermonde",
		"BE233":"Arr_Eeklo",
		"BE234":"Arr_Gent",
		"BE235":"Arr_Oudenaarde",
		"BE236":"Arr_Sint_Niklaas",
		"BE241":"Arr_Halle_Vilvoorde",
		"BE242":"Arr_Leuven",
		"BE251":"Arr_Brugge",
		"BE252":"Arr_Diksmuide",
		"BE253":"Arr_Ieper",
		"BE254":"Arr_Kortrijk",
		"BE255":"Arr_Oostende",
		"BE256":"Arr_Roeselare",
		"BE257":"Arr_Tielt",
		"BE258":"Arr_Veurne",
		"BE310":"Arr_Nivelles",
		"BE321":"Arr_Ath",
		"BE322":"Arr_Charleroi",
		"BE323":"Arr_Mons",
		"BE324":"Arr_Mouscron",
		"BE325":"Arr_Soignies",
		"BE326":"Arr_Thuin",
		"BE327":"Arr_Tournai",
		"BE331":"Arr_Huy",
		"BE332":"Arr_Liege",
		"BE334":"Arr_Waremme",
		"BE335":"Arr_Verviers_communes_francophones",
		"BE336":"Bezirk_Verviers_Deutschsprachige_Gemeinschaft",
		"BE341":"Arr_Arlon",
		"BE342":"Arr_Bastogne",
		"BE343":"Arr_Marche_en_Famenne",
		"BE344":"Arr_Neufchateau",
		"BE345":"Arr_Virton",
		"BE351":"Arr_Dinant",
		"BE352":"Arr_Namur",
		"BE353":"Arr_Philippeville",
		"BEZZZ":"Extra_Regio_NUTS_3_x2",
		"BG311":"Vidin",
		"BG312":"Montana",
		"BG313":"Vratsa",
		"BG314":"Pleven",
		"BG315":"Lovech",
		"BG321":"Veliko_Tarnovo",
		"BG322":"Gabrovo",
		"BG323":"Ruse",
		"BG324":"Razgrad",
		"BG325":"Silistra",
		"BG331":"Varna",
		"BG332":"Dobrich",
		"BG333":"Shumen",
		"BG334":"Targovishte",
		"BG341":"Burgas",
		"BG342":"Sliven",
		"BG343":"Yambol",
		"BG344":"Stara_Zagora",
		"BG411":"Sofia_stolitsa",
		"BG412":"Sofia",
		"BG413":"Blagoevgrad",
		"BG414":"Pernik",
		"BG415":"Kyustendil",
		"BG421":"Plovdiv",
		"BG422":"Haskovo",
		"BG423":"Pazardzhik",
		"BG424":"Smolyan",
		"BG425":"Kardzhali",
		"BGZZZ":"Extra_Regio_NUTS_3_x3",
		"CY000":"Kypros",
		"CYZZZ":"Extra_Regio_NUTS_3_x4",
		"CZ010":"Hlavni_Mesto_Praha",
		"CZ020":"Stredocesky_Kraj",
		"CZ031":"Jihocesky_Kraj",
		"CZ032":"Plzensky_Kraj",
		"CZ041":"Karlovarsky_kraj",
		"CZ042":"Ustecky_kraj",
		"CZ051":"Liberecky_kraj",
		"CZ052":"Kralovehradecky_kraj",
		"CZ053":"Pardubicky_kraj",
		"CZ063":"Kraj_Vysocina",
		"CZ064":"Jihomoravsky_kraj",
		"CZ071":"Olomoucky_kraj",
		"CZ072":"Zlinsky_kraj",
		"CZ080":"Moravskoslezsky_kraj",
		"CZZZZ":"Extra_Regio_NUTS_3_x5",
		"DE111":"Stuttgart_Stadtkreis",
		"DE112":"Boblingen",
		"DE113":"Esslingen",
		"DE114":"Goppingen",
		"DE115":"Ludwigsburg",
		"DE116":"Rems_Murr_Kreis",
		"DE117":"Heilbronn_Stadtkreis",
		"DE118":"Heilbronn_Landkreis",
		"DE119":"Hohenlohekreis",
		"DE11A":"Schwabisch_Hall",
		"DE11B":"Main_Tauber_Kreis",
		"DE11C":"Heidenheim",
		"DE11D":"Ostalbkreis",
		"DE121":"Baden_Baden_Stadtkreis",
		"DE122":"Karlsruhe_Stadtkreis",
		"DE123":"Karlsruhe_Landkreis",
		"DE124":"Rastatt",
		"DE125":"Heidelberg_Stadtkreis",
		"DE126":"Mannheim_Stadtkreis",
		"DE127":"Neckar_Odenwald_Kreis",
		"DE128":"Rhein_Neckar_Kreis",
		"DE129":"Pforzheim_Stadtkreis",
		"DE12A":"Calw",
		"DE12B":"Enzkreis",
		"DE12C":"Freudenstadt",
		"DE131":"Freiburg_im_Breisgau_Stadtkreis",
		"DE132":"Breisgau_Hochschwarzwald",
		"DE133":"Emmendingen",
		"DE134":"Ortenaukreis",
		"DE135":"Rottweil",
		"DE136":"Schwarzwald_Baar_Kreis",
		"DE137":"Tuttlingen",
		"DE138":"Konstanz",
		"DE139":"Lorrach",
		"DE13A":"Waldshut",
		"DE141":"Reutlingen",
		"DE142":"Tubingen_Landkreis",
		"DE143":"Zollernalbkreis",
		"DE144":"Ulm_Stadtkreis",
		"DE145":"Alb_Donau_Kreis",
		"DE146":"Biberach",
		"DE147":"Bodenseekreis",
		"DE148":"Ravensburg",
		"DE149":"Sigmaringen",
		"DE211":"Ingolstadt_Kreisfreie_Stadt",
		"DE212":"Munchen_Kreisfreie_Stadt",
		"DE213":"Rosenheim_Kreisfreie_Stadt",
		"DE214":"Altotting",
		"DE215":"Berchtesgadener_Land",
		"DE216":"Bad_Tolz_Wolfratshausen",
		"DE217":"Dachau",
		"DE218":"Ebersberg",
		"DE219":"Eichstatt",
		"DE21A":"Erding",
		"DE21B":"Freising",
		"DE21C":"Furstenfeldbruck",
		"DE21D":"Garmisch_Partenkirchen",
		"DE21E":"Landsberg_am_Lech",
		"DE21F":"Miesbach",
		"DE21G":"Muhldorf_a_Inn",
		"DE21H":"Munchen_Landkreis",
		"DE21I":"Neuburg_Schrobenhausen",
		"DE21J":"Pfaffenhofen_a_d_Ilm",
		"DE21K":"Rosenheim_Landkreis",
		"DE21L":"Starnberg",
		"DE21M":"Traunstein",
		"DE21N":"Weilheim_Schongau",
		"DE221":"Landshut_Kreisfreie_Stadt",
		"DE222":"Passau_Kreisfreie_Stadt",
		"DE223":"Straubing_Kreisfreie_Stadt",
		"DE224":"Deggendorf",
		"DE225":"Freyung_Grafenau",
		"DE226":"Kelheim",
		"DE227":"Landshut_Landkreis",
		"DE228":"Passau_Landkreis",
		"DE229":"Regen",
		"DE22A":"Rottal_Inn",
		"DE22B":"Straubing_Bogen",
		"DE22C":"Dingolfing_Landau",
		"DE231":"Amberg_Kreisfreie_Stadt",
		"DE232":"Regensburg_Kreisfreie_Stadt",
		"DE233":"Weiden_i_d_Opf_Kreisfreie_Stadt",
		"DE234":"Amberg_Sulzbach",
		"DE235":"Cham",
		"DE236":"Neumarkt_i_d_OPf",
		"DE237":"Neustadt_a_d_Waldnaab",
		"DE238":"Regensburg_Landkreis",
		"DE239":"Schwandorf",
		"DE23A":"Tirschenreuth",
		"DE241":"Bamberg_Kreisfreie_Stadt",
		"DE242":"Bayreuth_Kreisfreie_Stadt",
		"DE243":"Coburg_Kreisfreie_Stadt",
		"DE244":"Hof_Kreisfreie_Stadt",
		"DE245":"Bamberg_Landkreis",
		"DE246":"Bayreuth_Landkreis",
		"DE247":"Coburg_Landkreis",
		"DE248":"Forchheim",
		"DE249":"Hof_Landkreis",
		"DE24A":"Kronach",
		"DE24B":"Kulmbach",
		"DE24C":"Lichtenfels",
		"DE24D":"Wunsiedel_i_Fichtelgebirge",
		"DE251":"Ansbach_Kreisfreie_Stadt",
		"DE252":"Erlangen_Kreisfreie_Stadt",
		"DE253":"Furth_Kreisfreie_Stadt",
		"DE254":"Nurnberg_Kreisfreie_Stadt",
		"DE255":"Schwabach_Kreisfreie_Stadt",
		"DE256":"Ansbach_Landkreis",
		"DE257":"Erlangen_Hochstadt",
		"DE258":"Furth_Landkreis",
		"DE259":"Nurnberger_Land",
		"DE25A":"Neustadt_a_d_Aisch_Bad_Windsheim",
		"DE25B":"Roth",
		"DE25C":"Weissenburg_Gunzenhausen",
		"DE261":"Aschaffenburg_Kreisfreie_Stadt",
		"DE262":"Schweinfurt_Kreisfreie_Stadt",
		"DE263":"Wurzburg_Kreisfreie_Stadt",
		"DE264":"Aschaffenburg_Landkreis",
		"DE265":"Bad_Kissingen",
		"DE266":"Rhon_Grabfeld",
		"DE267":"Hassberge",
		"DE268":"Kitzingen",
		"DE269":"Miltenberg",
		"DE26A":"Main_Spessart",
		"DE26B":"Schweinfurt_Landkreis",
		"DE26C":"Wurzburg_Landkreis",
		"DE271":"Augsburg_Kreisfreie_Stadt",
		"DE272":"Kaufbeuren_Kreisfreie_Stadt",
		"DE273":"Kempten_Allgau_Kreisfreie_Stadt",
		"DE274":"Memmingen_Kreisfreie_Stadt",
		"DE275":"Aichach_Friedberg",
		"DE276":"Augsburg_Landkreis",
		"DE277":"Dillingen_a_d_Donau",
		"DE278":"Gunzburg",
		"DE279":"Neu_Ulm",
		"DE27A":"Lindau_Bodensee",
		"DE27B":"Ostallgau",
		"DE27C":"Unterallgau",
		"DE27D":"Donau_Ries",
		"DE27E":"Oberallgau",
		"DE300":"Berlin",
		"DE401":"Brandenburg_an_der_Havel_Kreisfreie_Stadt",
		"DE402":"Cottbus_Kreisfreie_Stadt",
		"DE403":"Frankfurt_Oder_Kreisfreie_Stadt",
		"DE404":"Potsdam_Kreisfreie_Stadt",
		"DE405":"Barnim",
		"DE406":"Dahme_Spreewald",
		"DE407":"Elbe_Elster",
		"DE408":"Havelland",
		"DE409":"Markisch_Oderland",
		"DE40A":"Oberhavel",
		"DE40B":"Oberspreewald_Lausitz",
		"DE40C":"Oder_Spree",
		"DE40D":"Ostprignitz_Ruppin",
		"DE40E":"Potsdam_Mittelmark",
		"DE40F":"Prignitz",
		"DE40G":"Spree_Neisse",
		"DE40H":"Teltow_Flaming",
		"DE40I":"Uckermark",
		"DE501":"Bremen_Kreisfreie_Stadt",
		"DE502":"Bremerhaven_Kreisfreie_Stadt",
		"DE600":"Hamburg",
		"DE711":"Darmstadt_Kreisfreie_Stadt",
		"DE712":"Frankfurt_am_Main_Kreisfreie_Stadt",
		"DE713":"Offenbach_am_Main_Kreisfreie_Stadt",
		"DE714":"Wiesbaden_Kreisfreie_Stadt",
		"DE715":"Bergstrasse",
		"DE716":"Darmstadt_Dieburg",
		"DE717":"Gross_Gerau",
		"DE718":"Hochtaunuskreis",
		"DE719":"Main_Kinzig_Kreis",
		"DE71A":"Main_Taunus_Kreis",
		"DE71B":"Odenwaldkreis",
		"DE71C":"Offenbach_Landkreis",
		"DE71D":"Rheingau_Taunus_Kreis",
		"DE71E":"Wetteraukreis",
		"DE721":"Giessen_Landkreis",
		"DE722":"Lahn_Dill_Kreis",
		"DE723":"Limburg_Weilburg",
		"DE724":"Marburg_Biedenkopf",
		"DE725":"Vogelsbergkreis",
		"DE731":"Kassel_Kreisfreie_Stadt",
		"DE732":"Fulda",
		"DE733":"Hersfeld_Rotenburg",
		"DE734":"Kassel_Landkreis",
		"DE735":"Schwalm_Eder_Kreis",
		"DE736":"Waldeck_Frankenberg",
		"DE737":"Werra_Meissner_Kreis",
		"DE803":"Rostock_Kreisfreie_Stadt",
		"DE804":"Schwerin_Kreisfreie_Stadt",
		"DE80J":"Mecklenburgische_Seenplatte",
		"DE80K":"Landkreis_Rostock",
		"DE80L":"Vorpommern_Rugen",
		"DE80M":"Nordwestmecklenburg",
		"DE80N":"Vorpommern_Greifswald",
		"DE80O":"Ludwigslust_Parchim",
		"DE911":"Braunschweig_Kreisfreie_Stadt",
		"DE912":"Salzgitter_Kreisfreie_Stadt",
		"DE913":"Wolfsburg_Kreisfreie_Stadt",
		"DE914":"Gifhorn",
		"DE916":"Goslar",
		"DE917":"Helmstedt",
		"DE918":"Northeim",
		"DE91A":"Peine",
		"DE91B":"Wolfenbuttel",
		"DE91C":"Gottingen",
		"DE922":"Diepholz",
		"DE923":"Hameln_Pyrmont",
		"DE925":"Hildesheim",
		"DE926":"Holzminden",
		"DE927":"Nienburg_Weser",
		"DE928":"Schaumburg",
		"DE929":"Region_Hannover",
		"DE931":"Celle",
		"DE932":"Cuxhaven",
		"DE933":"Harburg",
		"DE934":"Luchow_Dannenberg",
		"DE935":"Luneburg_Landkreis",
		"DE936":"Osterholz",
		"DE937":"Rotenburg_Wumme",
		"DE938":"Soltau_Fallingbostel",
		"DE939":"Stade",
		"DE93A":"Uelzen",
		"DE93B":"Verden",
		"DE941":"Delmenhorst_Kreisfreie_Stadt",
		"DE942":"Emden_Kreisfreie_Stadt",
		"DE943":"Oldenburg_Oldenburg_Kreisfreie_Stadt",
		"DE944":"Osnabruck_Kreisfreie_Stadt",
		"DE945":"Wilhelmshaven_Kreisfreie_Stadt",
		"DE946":"Ammerland",
		"DE947":"Aurich",
		"DE948":"Cloppenburg",
		"DE949":"Emsland",
		"DE94A":"Friesland_DE",
		"DE94B":"Grafschaft_Bentheim",
		"DE94C":"Leer",
		"DE94D":"Oldenburg_Landkreis",
		"DE94E":"Osnabruck_Landkreis",
		"DE94F":"Vechta",
		"DE94G":"Wesermarsch",
		"DE94H":"Wittmund",
		"DEA11":"Dusseldorf_Kreisfreie_Stadt",
		"DEA12":"Duisburg_Kreisfreie_Stadt",
		"DEA13":"Essen_Kreisfreie_Stadt",
		"DEA14":"Krefeld_Kreisfreie_Stadt",
		"DEA15":"Monchengladbach_Kreisfreie_Stadt",
		"DEA16":"Mulheim_an_der_Ruhr_Kreisfreie_Stadt",
		"DEA17":"Oberhausen_Kreisfreie_Stadt",
		"DEA18":"Remscheid_Kreisfreie_Stadt",
		"DEA19":"Solingen_Kreisfreie_Stadt",
		"DEA1A":"Wuppertal_Kreisfreie_Stadt",
		"DEA1B":"Kleve",
		"DEA1C":"Mettmann",
		"DEA1D":"Rhein_Kreis_Neuss",
		"DEA1E":"Viersen",
		"DEA1F":"Wesel",
		"DEA22":"Bonn_Kreisfreie_Stadt",
		"DEA23":"Koln_Kreisfreie_Stadt",
		"DEA24":"Leverkusen_Kreisfreie_Stadt",
		"DEA26":"Duren",
		"DEA27":"Rhein_Erft_Kreis",
		"DEA28":"Euskirchen",
		"DEA29":"Heinsberg",
		"DEA2A":"Oberbergischer_Kreis",
		"DEA2B":"Rheinisch_Bergischer_Kreis",
		"DEA2C":"Rhein_Sieg_Kreis",
		"DEA2D":"Stadteregion_Aachen",
		"DEA31":"Bottrop_Kreisfreie_Stadt",
		"DEA32":"Gelsenkirchen_Kreisfreie_Stadt",
		"DEA33":"Munster_Kreisfreie_Stadt",
		"DEA34":"Borken",
		"DEA35":"Coesfeld",
		"DEA36":"Recklinghausen",
		"DEA37":"Steinfurt",
		"DEA38":"Warendorf",
		"DEA41":"Bielefeld_Kreisfreie_Stadt",
		"DEA42":"Gutersloh",
		"DEA43":"Herford",
		"DEA44":"Hoxter",
		"DEA45":"Lippe",
		"DEA46":"Minden_Lubbecke",
		"DEA47":"Paderborn",
		"DEA51":"Bochum_Kreisfreie_Stadt",
		"DEA52":"Dortmund_Kreisfreie_Stadt",
		"DEA53":"Hagen_Kreisfreie_Stadt",
		"DEA54":"Hamm_Kreisfreie_Stadt",
		"DEA55":"Herne_Kreisfreie_Stadt",
		"DEA56":"Ennepe_Ruhr_Kreis",
		"DEA57":"Hochsauerlandkreis",
		"DEA58":"Markischer_Kreis",
		"DEA59":"Olpe",
		"DEA5A":"Siegen_Wittgenstein",
		"DEA5B":"Soest",
		"DEA5C":"Unna",
		"DEB11":"Koblenz_Kreisfreie_Stadt",
		"DEB12":"Ahrweiler",
		"DEB13":"Altenkirchen_Westerwald",
		"DEB14":"Bad_Kreuznach",
		"DEB15":"Birkenfeld",
		"DEB17":"Mayen_Koblenz",
		"DEB18":"Neuwied",
		"DEB1A":"Rhein_Lahn_Kreis",
		"DEB1B":"Westerwaldkreis",
		"DEB1C":"Cochem_Zell",
		"DEB1D":"Rhein_Hunsruck_Kreis",
		"DEB21":"Trier_Kreisfreie_Stadt",
		"DEB22":"Bernkastel_Wittlich",
		"DEB23":"Eifelkreis_Bitburg_Prum",
		"DEB24":"Vulkaneifel",
		"DEB25":"Trier_Saarburg",
		"DEB31":"Frankenthal_Pfalz_Kreisfreie_Stadt",
		"DEB32":"Kaiserslautern_Kreisfreie_Stadt",
		"DEB33":"Landau_in_der_Pfalz_Kreisfreie_Stadt",
		"DEB34":"Ludwigshafen_am_Rhein_Kreisfreie_Stadt",
		"DEB35":"Mainz_Kreisfreie_Stadt",
		"DEB36":"Neustadt_an_der_Weinstrasse_Kreisfreie_Stadt",
		"DEB37":"Pirmasens_Kreisfreie_Stadt",
		"DEB38":"Speyer_Kreisfreie_Stadt",
		"DEB39":"Worms_Kreisfreie_Stadt",
		"DEB3A":"Zweibrucken_Kreisfreie_Stadt",
		"DEB3B":"Alzey_Worms",
		"DEB3C":"Bad_Durkheim",
		"DEB3D":"Donnersbergkreis",
		"DEB3E":"Germersheim",
		"DEB3F":"Kaiserslautern_Landkreis",
		"DEB3G":"Kusel",
		"DEB3H":"Sudliche_Weinstrasse",
		"DEB3I":"Rhein_Pfalz_Kreis",
		"DEB3J":"Mainz_Bingen",
		"DEB3K":"Sudwestpfalz",
		"DEC01":"Regionalverband_Saarbrucken",
		"DEC02":"Merzig_Wadern",
		"DEC03":"Neunkirchen",
		"DEC04":"Saarlouis",
		"DEC05":"Saarpfalz_Kreis",
		"DEC06":"St_Wendel",
		"DED21":"Dresden_Kreisfreie_Stadt",
		"DED2C":"Bautzen",
		"DED2D":"Gorlitz",
		"DED2E":"Meissen",
		"DED2F":"Sachsische_Schweiz_Osterzgebirge",
		"DED41":"Chemnitz_Kreisfreie_Stadt",
		"DED42":"Erzgebirgskreis",
		"DED43":"Mittelsachsen",
		"DED44":"Vogtlandkreis",
		"DED45":"Zwichau",
		"DED51":"Leipzig_Kreisfreie_Stadt",
		"DED52":"Leipzig",
		"DED53":"Nordsachsen",
		"DEE01":"Dessau_Rosslau_Kreisfreie_Stadt",
		"DEE02":"Halle_Saale_Kreisfreie_Stadt",
		"DEE03":"Magdeburg_Kreisfreie_Stadt",
		"DEE04":"Altmarkkreis_Salzwedel",
		"DEE05":"Anhalt_Bitterfeld",
		"DEE06":"Jerichower_Land",
		"DEE07":"Borde",
		"DEE08":"Burgenland_DE",
		"DEE09":"Harz",
		"DEE0A":"Mansfeld_Sudharz",
		"DEE0B":"Saalekreis",
		"DEE0C":"Salzlandkreis",
		"DEE0D":"Stendal",
		"DEE0E":"Wittenberg",
		"DEF01":"Flensburg_Kreisfreie_Stadt",
		"DEF02":"Kiel_Kreisfreie_Stadt",
		"DEF03":"Lubeck_Kreisfreie_Stadt",
		"DEF04":"Neumunster_Kreisfreie_Stadt",
		"DEF05":"Dithmarschen",
		"DEF06":"Herzogtum_Lauenburg",
		"DEF07":"Nordfriesland",
		"DEF08":"Ostholstein",
		"DEF09":"Pinneberg",
		"DEF0A":"Plon",
		"DEF0B":"Rendsburg_Eckernforde",
		"DEF0C":"Schleswig_Flensburg",
		"DEF0D":"Segeberg",
		"DEF0E":"Steinburg",
		"DEF0F":"Stormarn",
		"DEG01":"Erfurt_Kreisfreie_Stadt",
		"DEG02":"Gera_Kreisfreie_Stadt",
		"DEG03":"Jena_Kreisfreie_Stadt",
		"DEG04":"Suhl_Kreisfreie_Stadt",
		"DEG05":"Weimar_Kreisfreie_Stadt",
		"DEG06":"Eichsfeld",
		"DEG07":"Nordhausen",
		"DEG09":"Unstrut_Hainich_Kreis",
		"DEG0A":"Kyffhauserkreis",
		"DEG0B":"Schmalkalden_Meiningen",
		"DEG0C":"Gotha",
		"DEG0D":"Sommerda",
		"DEG0E":"Hildburghausen",
		"DEG0F":"Ilm_Kreis",
		"DEG0G":"Weimarer_Land",
		"DEG0H":"Sonneberg",
		"DEG0I":"Saalfeld_Rudolstadt",
		"DEG0J":"Saale_Holzland_Kreis",
		"DEG0K":"Saale_Orla_Kreis",
		"DEG0L":"Greiz",
		"DEG0M":"Altenburger_Land",
		"DEG0N":"Eisenach_Kreisfreie_Stadt",
		"DEG0P":"Wartburgkreis",
		"DEZZZ":"Extra_Regio_NUTS_3_x6",
		"DK011":"Byen_Kobenhavn",
		"DK012":"Kobenhavns_omegn",
		"DK013":"Nordsjaelland",
		"DK014":"Bornholm",
		"DK021":"Ostsjaelland",
		"DK022":"Vest_og_Sydsjaelland",
		"DK031":"Fyn",
		"DK032":"Sydjylland",
		"DK041":"Vestjylland",
		"DK042":"Ostjylland",
		"DK050":"Nordjylland",
		"DKZZZ":"Extra_Regio_NUTS_3_x7",
		"EE001":"Pohja_Eesti",
		"EE004":"Laane_Eesti",
		"EE006":"Kesk_Eesti",
		"EE007":"Kirde_Eesti",
		"EE008":"Louna_Eesti",
		"EEZZZ":"Extra_Regio_NUTS_3_x8",
		"EL301":"Voreios_Tomeas_Athinon",
		"EL302":"Dytikos_Tomeas_Athinon",
		"EL303":"Kentrikos_Tomeas_Athinon",
		"EL304":"Notios_Tomeas_Athinon",
		"EL305":"Anatoliki_Attiki",
		"EL306":"Dytiki_Attiki",
		"EL307":"Peiraias_Nisoi",
		"EL411":"Lesvos",
		"EL412":"Samos",
		"EL413":"Chios",
		"EL421":"Dodekanisos",
		"EL422":"Kyklades",
		"EL431":"Irakleio",
		"EL432":"Lasithi",
		"EL433":"Rethymni",
		"EL434":"Chania",
		"EL511":"Evros",
		"EL512":"Xanthi",
		"EL513":"Rodopi",
		"EL514":"Drama",
		"EL515":"Thasos_Kavala",
		"EL521":"Imathia",
		"EL522":"Thessaloniki",
		"EL523":"Kilkis",
		"EL524":"Pella",
		"EL525":"Pieria",
		"EL526":"Serres",
		"EL527":"Chalkidiki",
		"EL531":"Grevena_Kozani",
		"EL532":"Kastoria",
		"EL533":"Florina",
		"EL541":"Arta_Preveza",
		"EL542":"Thesprotia",
		"EL543":"Ioannina",
		"EL611":"Karditsa_Trikala",
		"EL612":"Larisa",
		"EL613":"Magnisia_Sporades",
		"EL621":"Zakynthos",
		"EL622":"Kerkyra",
		"EL623":"Ithaki_Kefallinia",
		"EL624":"Lefkada",
		"EL631":"Aitoloakarnania",
		"EL632":"Achaia",
		"EL633":"Ileia",
		"EL641":"Voiotia",
		"EL642":"Evvoia",
		"EL643":"Evrytania",
		"EL644":"Fthiotida",
		"EL645":"Fokida",
		"EL651":"Argolida_Arkadia",
		"EL652":"Korinthia",
		"EL653":"lakonia_Messinia",
		"ELZZZ":"Extra_Regio_NUTS_3_x9",
		"ES111":"A_Coruna",
		"ES112":"Lugo",
		"ES113":"Ourense",
		"ES114":"Pontevedra",
		"ES120":"Asturias",
		"ES130":"Cantabria",
		"ES211":"Alava",
		"ES212":"Guipuzcoa",
		"ES213":"Vizcaya",
		"ES220":"Navarra",
		"ES230":"La_Rioja",
		"ES241":"Huesca",
		"ES242":"Teruel",
		"ES243":"Zaragoza",
		"ES300":"Madrid",
		"ES411":"Avila",
		"ES412":"Burgos",
		"ES413":"Leon",
		"ES414":"Palencia",
		"ES415":"Salamanca",
		"ES416":"Segovia",
		"ES417":"Soria",
		"ES418":"Valladolid",
		"ES419":"Zamora",
		"ES421":"Albacete",
		"ES422":"Ciudad_Real",
		"ES423":"Cuenca",
		"ES424":"Guadalajara",
		"ES425":"Toledo",
		"ES431":"Badajoz",
		"ES432":"Caceres",
		"ES511":"Barcelona",
		"ES512":"Girona",
		"ES513":"Lleida",
		"ES514":"Tarragona",
		"ES521":"Alicante_Alacant",
		"ES522":"Castellon_Castello",
		"ES523":"Valencia_Valencia",
		"ES531":"Eivissa_y_Formentera",
		"ES532":"Mallorca",
		"ES533":"Menorca",
		"ES611":"Almeria",
		"ES612":"Cadiz",
		"ES613":"Cordoba",
		"ES614":"Granada",
		"ES615":"Huelva",
		"ES616":"Jaen",
		"ES617":"Malaga",
		"ES618":"Sevilla",
		"ES620":"Murcia",
		"ES630":"Ceuta",
		"ES640":"Melilla",
		"ES703":"El_Hierro",
		"ES704":"Fuerteventura",
		"ES705":"Gran_Canaria",
		"ES706":"La_Gomera",
		"ES707":"La_Palma",
		"ES708":"Lanzarote",
		"ES709":"Tenerife",
		"ESZZZ":"Extra_Regio_NUTS_3_x10",
		"FI193":"Keski_Suomi",
		"FI194":"Etela_Pohjanmaa",
		"FI195":"Pohjanmaa",
		"FI196":"Satakunta",
		"FI197":"Pirkanmaa",
		"FI1B1":"Helsinki_Uusimaa",
		"FI1C1":"Varsinais_Suomi",
		"FI1C2":"Kanta_Hame",
		"FI1C3":"Paijat_Hame",
		"FI1C4":"Kymenlaakso",
		"FI1C5":"Etela_Karjala",
		"FI1D1":"Etela_Savo",
		"FI1D2":"Pohjois_Savo",
		"FI1D3":"Pohjois_Karjala",
		"FI1D5":"Keski_Pohjanmaa",
		"FI1D7":"Lappi",
		"FI1D8":"Kainuu",
		"FI1D9":"Pohjois_Pohjanmaa",
		"FI200":"Aland",
		"FIZZZ":"Extra_Regio_NUTS_3_x11",
		"FR101":"Paris",
		"FR102":"Seine_et_Marne",
		"FR103":"Yvelines",
		"FR104":"Essonne",
		"FR105":"Hauts_de_Seine",
		"FR106":"Seine_Saint_Denis",
		"FR107":"Val_de_Marne",
		"FR108":"Val_d_Oise",
		"FRB01":"Cher",
		"FRB02":"Eure_et_Loir",
		"FRB03":"Indre",
		"FRB04":"Indre_et_Loire",
		"FRB05":"Loir_et_Cher",
		"FRB06":"Loiret",
		"FRC11":"Cote_d_Or",
		"FRC12":"Nievre",
		"FRC13":"Saone_et_Loire",
		"FRC14":"Yonne",
		"FRC21":"Doubs",
		"FRC22":"Jura",
		"FRC23":"Haute_Saone",
		"FRC24":"Territoire_de_Belfort",
		"FRD11":"Calvados",
		"FRD12":"Manche",
		"FRD13":"Orne",
		"FRD21":"Eure",
		"FRD22":"Seine_Maritime",
		"FRE11":"Nord",
		"FRE12":"Pas_de_Calais",
		"FRE21":"Aisne",
		"FRE22":"Oise",
		"FRE23":"Somme",
		"FRF11":"Bas_Rhin",
		"FRF12":"Haut_Rhin",
		"FRF21":"Ardennes",
		"FRF22":"Aube",
		"FRF23":"Marne",
		"FRF24":"Haute_Marne",
		"FRF31":"Meurthe_et_Moselle",
		"FRF32":"Meuse",
		"FRF33":"Moselle",
		"FRF34":"Vosges",
		"FRG01":"Loire_Atlantique",
		"FRG02":"Maine_et_Loire",
		"FRG03":"Mayenne",
		"FRG04":"Sarthe",
		"FRG05":"Vendee",
		"FRH01":"Cotes_d_Armor",
		"FRH02":"Finistere",
		"FRH03":"Ille_et_Vilaine",
		"FRH04":"Morbihan",
		"FRI11":"Dordogne",
		"FRI12":"Gironde",
		"FRI13":"Landes",
		"FRI14":"Lot_et_Garonne",
		"FRI15":"Pyrenees_Atlantiques",
		"FRI21":"Correze",
		"FRI22":"Creuse",
		"FRI23":"Haute_Vienne",
		"FRI31":"Charente",
		"FRI32":"Charente_Maritime",
		"FRI33":"Deux_Sevres",
		"FRI34":"Vienne",
		"FRJ11":"Aude",
		"FRJ12":"Gard",
		"FRJ13":"Herault",
		"FRJ14":"Lozere",
		"FRJ15":"Pyrenees_Orientales",
		"FRJ21":"Ariege",
		"FRJ22":"Aveyron",
		"FRJ23":"Haute_Garonne",
		"FRJ24":"Gers",
		"FRJ25":"Lot",
		"FRJ26":"Hautes_Pyrenees",
		"FRJ27":"Tarn",
		"FRJ28":"Tarn_et_Garonne",
		"FRK11":"Allier",
		"FRK12":"Cantal",
		"FRK13":"Haute_Loire",
		"FRK14":"Puy_de_Dome",
		"FRK21":"Ain",
		"FRK22":"Ardeche",
		"FRK23":"Drome",
		"FRK24":"Isere",
		"FRK25":"Loire",
		"FRK26":"Rhone",
		"FRK27":"Savoie",
		"FRK28":"Haute_Savoie",
		"FRL01":"Alpes_de_Haute_Provence",
		"FRL02":"Hautes_Alpes",
		"FRL03":"Alpes_Maritimes",
		"FRL04":"Bouches_du_Rhone",
		"FRL05":"Var",
		"FRL06":"Vaucluse",
		"FRM01":"Corse_du_Sud",
		"FRM02":"Haute_Corse",
		"FRY10":"Guadeloupe",
		"FRY20":"Martinique",
		"FRY30":"Guyane",
		"FRY40":"La_Reunion",
		"FRY50":"Mayotte",
		"FRZZZ":"Extra_Regio_NUTS_3_x12",
		"HR031":"Primorsko_goranska_zupanija",
		"HR032":"Licko_senjska_Zupanija",
		"HR033":"Zadarska_zupanija",
		"HR034":"Sibensko_kninska_zupanija",
		"HR035":"Splitsko_dalmatinska_zupanija",
		"HR036":"Istarska_zupanija",
		"HR037":"Dubrovacko_neretvanska_Zupanija",
		"HR041":"Grad_Zagreb",
		"HR042":"Zagrebacka_Zupanija",
		"HR043":"Krapinsko_zagorska_zupanija",
		"HR044":"Varazdinska_zupanija",
		"HR045":"Koprivnicko_krizevacka_Zupanija",
		"HR046":"Medimurska_Zupanija",
		"HR047":"Bjelovarsko_bilogorska_zupanija",
		"HR048":"Viroviticko_podravska_Zupanija",
		"HR049":"Pozesko_slavonska_zupanija",
		"HR04A":"Brodsko_posavska_zupanija",
		"HR04B":"Osjecko_baranjska_Zupanija",
		"HR04C":"Vukovarsko_srijemska_zupanija",
		"HR04D":"Karlovacka_Zupanija",
		"HR04E":"Sisacko_moslavacka_Zupanija",
		"HRZZZ":"Extra_Regio_NUTS_3_x13",
		"HU110":"Budapest",
		"HU120":"Pest",
		"HU211":"Fejer",
		"HU212":"Komarom_Esztergom",
		"HU213":"Veszprem",
		"HU221":"Gyor_moson_sopron",
		"HU222":"Vas",
		"HU223":"Zala",
		"HU231":"Baranya",
		"HU232":"Somogy",
		"HU233":"Tolna",
		"HU311":"Borsod_Abauj_Zemplen",
		"HU312":"Heves",
		"HU313":"Nograd",
		"HU321":"Hajdu_Bihar",
		"HU322":"Jasz_Nagykun_Szolnok",
		"HU323":"Szabolcs_Szatmar_Bereg",
		"HU331":"Bacs_Kiskun",
		"HU332":"Bekes",
		"HU333":"Csongrad",
		"HUZZZ":"Extra_Regio_NUTS_3_x14",
		"IE041":"Border",
		"IE042":"West",
		"IE051":"Mid_West",
		"IE052":"South_East",
		"IE053":"South_West",
		"IE061":"Dublin",
		"IE062":"Mid_East",
		"IE063":"Midland",
		"IEZZZ":"Extra_Regio_NUTS_3_x15",
		"ITC11":"Torino",
		"ITC12":"Vercelli",
		"ITC13":"Biella",
		"ITC14":"Verbano_Cusio_Ossola",
		"ITC15":"Novara",
		"ITC16":"Cuneo",
		"ITC17":"Asti",
		"ITC18":"Alessandria",
		"ITC20":"Valle_d_Aosta_Vallee_d_Aoste",
		"ITC31":"Imperia",
		"ITC32":"Savona",
		"ITC33":"Genova",
		"ITC34":"La_Spezia",
		"ITC41":"Varese",
		"ITC42":"Como",
		"ITC43":"Lecco",
		"ITC44":"Sondrio",
		"ITC46":"Bergamo",
		"ITC47":"Brescia",
		"ITC48":"Pavia",
		"ITC49":"Lodi",
		"ITC4A":"Cremona",
		"ITC4B":"Mantova",
		"ITC4C":"Milano",
		"ITC4D":"Monza_e_della_Brianza",
		"ITF11":"L_Aquila",
		"ITF12":"Teramo",
		"ITF13":"Pescara",
		"ITF14":"Chieti",
		"ITF21":"Isernia",
		"ITF22":"Campobasso",
		"ITF31":"Caserta",
		"ITF32":"Benevento",
		"ITF33":"Napoli",
		"ITF34":"Avellino",
		"ITF35":"Salerno",
		"ITF43":"Taranto",
		"ITF44":"Brindisi",
		"ITF45":"Lecce",
		"ITF46":"Foggia",
		"ITF47":"Bari",
		"ITF48":"Barletta_Andria_Trani",
		"ITF51":"Potenza",
		"ITF52":"Matera",
		"ITF61":"Cosenza",
		"ITF62":"Crotone",
		"ITF63":"Catanzaro",
		"ITF64":"Vibo_Valentia",
		"ITF65":"Reggio_di_Calabria",
		"ITG11":"Trapani",
		"ITG12":"Palermo",
		"ITG13":"Messina",
		"ITG14":"Agrigento",
		"ITG15":"Caltanissetta",
		"ITG16":"Enna",
		"ITG17":"Catania",
		"ITG18":"Ragusa",
		"ITG19":"Siracusa",
		"ITG25":"Sassari",
		"ITG26":"Nuoro",
		"ITG27":"Cagliari",
		"ITG28":"Oristano",
		"ITG29":"Olbia_Tempio",
		"ITG2A":"Ogliastra",
		"ITG2B":"Medio_Campidano",
		"ITG2C":"Carbonia_Iglesias",
		"ITH10":"Bolzano_Bozen",
		"ITH20":"Trento",
		"ITH31":"Verona",
		"ITH32":"Vicenza",
		"ITH33":"Belluno",
		"ITH34":"Treviso",
		"ITH35":"Venezia",
		"ITH36":"Padova",
		"ITH37":"Rovigo",
		"ITH41":"Pordenone",
		"ITH42":"Udine",
		"ITH43":"Gorizia",
		"ITH44":"Trieste",
		"ITH51":"Piacenza",
		"ITH52":"Parma",
		"ITH53":"Reggio_nell_Emilia",
		"ITH54":"Modena",
		"ITH55":"Bologna",
		"ITH56":"Ferrara",
		"ITH57":"Ravenna",
		"ITH58":"Forli_Cesena",
		"ITH59":"Rimini",
		"ITI11":"Massa_Carrara",
		"ITI12":"Lucca",
		"ITI13":"Pistoia",
		"ITI14":"Firenze",
		"ITI15":"Prato",
		"ITI16":"Livorno",
		"ITI17":"Pisa",
		"ITI18":"Arezzo",
		"ITI19":"Siena",
		"ITI1A":"Grosseto",
		"ITI21":"Perugia",
		"ITI22":"Terni",
		"ITI31":"Pesaro_e_Urbino",
		"ITI32":"Ancona",
		"ITI33":"Macerata",
		"ITI34":"Ascoli_Piceno",
		"ITI35":"Fermo",
		"ITI41":"Viterbo",
		"ITI42":"Rieti",
		"ITI43":"Roma",
		"ITI44":"Latina",
		"ITI45":"Frosinone",
		"ITZZZ":"Extra_Regio_NUTS_3_x16",
		"LT011":"Vilniaus_apskritis",
		"LT021":"Alytaus_apskritis",
		"LT022":"Kauno_apskritis",
		"LT023":"Klaip_dos_apskritis",
		"LT024":"Marijampol_s_apskritis",
		"LT025":"Panev_zio_apskritis",
		"LT026":"Siauli_apskritis",
		"LT027":"Taurag_s_apskritis",
		"LT028":"Telsi_apskritis",
		"LT029":"Utenos_apskritis",
		"LTZZZ":"Extra_Regio_NUTS_3_x17",
		"LU000":"Luxembourg",
		"LUZZZ":"Extra_Regio_NUTS_3_x18",
		"LV003":"Kurzeme",
		"LV005":"Latgale",
		"LV006":"Riga",
		"LV007":"Pieriga",
		"LV008":"Vidzeme",
		"LV009":"Zemgale",
		"LVZZZ":"Extra_Regio_NUTS_3_x19",
		"MT001":"Malta",
		"MT002":"Gozo_And_CominoGhawdex_U_Kemmuna",
		"MTZZZ":"Extra_Regio_NUTS_3_x20",
		"NL111":"Oost_Groningen",
		"NL112":"Delfzijl_en_omgeving",
		"NL113":"Overig_Groningen",
		"NL124":"Noord_Friesland",
		"NL125":"Zuidwest_Friesland",
		"NL126":"Zuidoost_Friesland",
		"NL131":"Noord_Drenthe",
		"NL132":"Zuidoost_Drenthe",
		"NL133":"Zuidwest_Drenthe",
		"NL211":"Noord_Overijssel",
		"NL212":"Zuidwest_Overijssel",
		"NL213":"Twente",
		"NL221":"Veluwe",
		"NL224":"Zuidwest_Gelderland",
		"NL225":"Achterhoek",
		"NL226":"Arnhem_Nijmegen",
		"NL230":"Flevoland",
		"NL310":"Utrecht",
		"NL321":"Kop_van_Noord_Holland",
		"NL323":"IJmond",
		"NL324":"Agglomeratie_Haarlem",
		"NL325":"Zaanstreek",
		"NL327":"Het_Gooi_en_Vechtstreek",
		"NL328":"Alkmaar_en_omgeving",
		"NL329":"Groot_Amsterdam",
		"NL332":"Agglomeratie_s_Gravenhage",
		"NL333":"Delft_en_Westland",
		"NL337":"Agglomeratie_Leiden_en_Bollenstreek",
		"NL33A":"Zuidoost_Zuid_Holland",
		"NL33B":"Oost_Zuid_Holland",
		"NL33C":"Groot_Rijnmond",
		"NL341":"Zeeuwsch_Vlaanderen",
		"NL342":"Overig_Zeeland",
		"NL411":"West_Noord_Brabant",
		"NL412":"Midden_Noord_Brabant",
		"NL413":"Noordoost_Noord_Brabant",
		"NL414":"Zuidoost_Noord_Brabant",
		"NL421":"Noord_Limburg",
		"NL422":"Midden_Limburg",
		"NL423":"Zuid_Limburg",
		"NLZZZ":"Extra_Regio_NUTS_3_x21",
		"PL213":"Miasto_Krakow",
		"PL214":"Krakowski",
		"PL217":"Tarnowski",
		"PL218":"Nowosadecki",
		"PL219":"Nowotarski",
		"PL21A":"Oswiecimski",
		"PL224":"Czestochowski",
		"PL225":"Bielski",
		"PL227":"Rybnicki",
		"PL228":"Bytomski",
		"PL229":"Gliwicki",
		"PL22A":"Katowicki",
		"PL22B":"Sosnowiecki",
		"PL22C":"Tyski",
		"PL411":"Pilski",
		"PL414":"Koninski",
		"PL415":"Miasto_Poznan",
		"PL416":"Kaliski",
		"PL417":"Leszczynski",
		"PL418":"Poznanski",
		"PL424":"Miasto_Szczecin",
		"PL426":"Koszalinski",
		"PL427":"Szczecinecko_pyrzycki",
		"PL428":"Szczecinski",
		"PL431":"Gorzowski",
		"PL432":"Zielonogorski",
		"PL514":"Miasto_Wroclaw",
		"PL515":"Jeleniogorski",
		"PL516":"Legnicko_glogowski",
		"PL517":"Walbrzyski",
		"PL518":"Wroclawski",
		"PL523":"Nyski",
		"PL524":"Opolski",
		"PL613":"Bydgosko_torunski",
		"PL616":"Grudziadzki",
		"PL617":"Inowroclawski",
		"PL618":"Swiecki",
		"PL619":"Wloclawski",
		"PL621":"Elblaski",
		"PL622":"Olsztynski",
		"PL623":"Elcki",
		"PL633":"Trojmiejski",
		"PL634":"Gdanski",
		"PL636":"Slupski",
		"PL637":"Chojnicki",
		"PL638":"Starogardzki",
		"PL711":"Miasto_od",
		"PL712":"_odzki",
		"PL713":"Piotrkowski",
		"PL714":"Sieradzki",
		"PL715":"Skierniewicki",
		"PL721":"Kielecki",
		"PL722":"Sandomiersko_j_drzejowski",
		"PL811":"Bialski",
		"PL812":"Che_msko_zamojski",
		"PL814":"Lubelski",
		"PL815":"Pu_awski",
		"PL821":"Kro_nie_ski",
		"PL822":"Przemyski",
		"PL823":"Rzeszowski",
		"PL824":"Tarnobrzeski",
		"PL841":"Bia_ostocki",
		"PL842":"_om_y_ski",
		"PL843":"Suwalski",
		"PL911":"Miasto_Warszawa",
		"PL912":"Warszawski_wschodni",
		"PL913":"Warszawski_zachodni",
		"PL921":"Radomski",
		"PL922":"Ciechanowski",
		"PL923":"P_ocki",
		"PL924":"Ostro_cki",
		"PL925":"Siedlecki",
		"PL926":"_yrardowski",
		"PLZZZ":"Extra_Regio_NUTS_3_x22",
		"PT111":"Minho_Lima",
		"PT112":"Cavado",
		"PT119":"Ave",
		"PT11A":"Area_Metropolitana_do_Porto",
		"PT11B":"Alto_Tamega",
		"PT11C":"Tamega_e_Sousa",
		"PT11D":"Douro",
		"PT11E":"Terras_de_Tras_os_Montes",
		"PT150":"Algarve",
		"PT16B":"Oeste",
		"PT16D":"Regiao_de_Aveiro",
		"PT16E":"Regiao_de_Coimbra",
		"PT16F":"Regiao_de_Leiria",
		"PT16G":"Viseu_Dao_Lafoes",
		"PT16H":"Beira_Baixa",
		"PT16I":"Medio_Tejo",
		"PT16J":"Beiras_e_Serra_da_Estrela",
		"PT170":"Area_Metropolitana_de_Lisboa",
		"PT181":"Alentejo_Litoral",
		"PT184":"Baixo_Alentejo",
		"PT185":"Leziria_do_Tejo",
		"PT186":"Alto_Alentejo",
		"PT187":"Alentejo_Central",
		"PT200":"Regiao_Autonoma_dos_Acores",
		"PT300":"Regiao_Autonoma_da_Madeira",
		"PTZZZ":"Extra_Regio_NUTS_3_x23",
		"RO111":"Bihor",
		"RO112":"Bistrita_nasaud",
		"RO113":"Cluj",
		"RO114":"Maramures",
		"RO115":"Satu_Mare",
		"RO116":"Salaj",
		"RO121":"Alba",
		"RO122":"Brasov",
		"RO123":"Covasna",
		"RO124":"Harghita",
		"RO125":"Mures",
		"RO126":"Sibiu",
		"RO211":"Bacau",
		"RO212":"Botosani",
		"RO213":"Iasi",
		"RO214":"Neamt",
		"RO215":"Suceava",
		"RO216":"Vaslui",
		"RO221":"Braila",
		"RO222":"Buzau",
		"RO223":"Constanta",
		"RO224":"Galati",
		"RO225":"Tulcea",
		"RO226":"Vrancea",
		"RO311":"Arges",
		"RO312":"Calarasi",
		"RO313":"Dambovita",
		"RO314":"Giurgiu",
		"RO315":"Ialomita",
		"RO316":"Prahova",
		"RO317":"Teleorman",
		"RO321":"Bucuresti",
		"RO322":"Ilfov",
		"RO411":"Dolj",
		"RO412":"Gorj",
		"RO413":"Mehedinti",
		"RO414":"Olt",
		"RO415":"Valcea",
		"RO421":"Arad",
		"RO422":"Caras_severin",
		"RO423":"Hunedoara",
		"RO424":"Timis",
		"ROZZZ":"Extra_Regio_NUTS_3_x24",
		"SE110":"Stockholms_lan",
		"SE121":"Uppsala_lan",
		"SE122":"Sodermanlands_lan",
		"SE123":"Ostergotlands_lan",
		"SE124":"Orebro_lan",
		"SE125":"Vastmanlands_lan",
		"SE211":"Jonkopings_lan",
		"SE212":"Kronobergs_lan",
		"SE213":"Kalmar_lan",
		"SE214":"Gotlands_lan",
		"SE221":"Blekinge_lan",
		"SE224":"Skane_lan",
		"SE231":"Hallands_lan",
		"SE232":"Vastra_Gotalands_lan",
		"SE311":"Varmlands_lan",
		"SE312":"Dalarnas_lan",
		"SE313":"Gavleborgs_lan",
		"SE321":"Vasternorrlands_lan",
		"SE322":"Jamtlands_lan",
		"SE331":"Vasterbottens_lan",
		"SE332":"Norrbottens_lan",
		"SEZZZ":"Extra_Regio_NUTS_3_x25",
		"SI031":"Pomurska",
		"SI032":"Podravska",
		"SI033":"Koroska",
		"SI034":"Savinjska",
		"SI035":"Zasavska",
		"SI036":"Posavska",
		"SI037":"Jugovzhodna_Slovenija",
		"SI038":"Primorsko_notranjska",
		"SI041":"Osrednjeslovenska",
		"SI042":"Gorenjska",
		"SI043":"Goriska",
		"SI044":"Obalno_kraska",
		"SIZZZ":"Extra_Regio_NUTS_3_x26",
		"SK010":"Bratislavsky_kraj",
		"SK021":"Trnavsky_kraj",
		"SK022":"Trenciansky_Kraj",
		"SK023":"Nitriansky_kraj",
		"SK031":"Zilinsky_kraj",
		"SK032":"Banskobystricky_kraj",
		"SK041":"Presovsky_kraj",
		"SK042":"Kosicky_kraj",
		"SKZZZ":"Extra_Regio_NUTS_3_x27",
		"UKC11":"Hartlepool_and_Stockton_on_Tees",
		"UKC12":"South_Teesside",
		"UKC13":"Darlington",
		"UKC14":"Durham_CC",
		"UKC21":"Northumberland",
		"UKC22":"Tyneside",
		"UKC23":"Sunderland",
		"UKD11":"West_Cumbria",
		"UKD12":"East_Cumbria",
		"UKD33":"Manchester",
		"UKD34":"Greater_Manchester_South_West",
		"UKD35":"Greater_Manchester_South_East",
		"UKD36":"Greater_Manchester_North_West",
		"UKD37":"Greater_Manchester_North_East",
		"UKD41":"Blackburn_with_Darwen",
		"UKD42":"Blackpool",
		"UKD44":"Lancaster_and_Wyre",
		"UKD45":"Mid_Lancashire",
		"UKD46":"East_Lancashire",
		"UKD47":"Chorley_and_West_Lancashire",
		"UKD61":"Warrington",
		"UKD62":"Cheshire_East",
		"UKD63":"Cheshire_West_and_Chester",
		"UKD71":"East_Merseyside",
		"UKD72":"Liverpool",
		"UKD73":"Sefton",
		"UKD74":"Wirral",
		"UKE11":"Kingston_upon_Hull_City_of",
		"UKE12":"East_Riding_of_Yorkshire",
		"UKE13":"North_and_North_East_Lincolnshire",
		"UKE21":"York",
		"UKE22":"North_Yorkshire_CC",
		"UKE31":"Barnsley_Doncaster_and_Rotherham",
		"UKE32":"Sheffield",
		"UKE41":"Bradford",
		"UKE42":"Leeds",
		"UKE44":"Calderdale_and_Kirklees",
		"UKE45":"Wakefield",
		"UKF11":"Derby",
		"UKF12":"East_Derbyshire",
		"UKF13":"South_and_West_Derbyshire",
		"UKF14":"Nottingham",
		"UKF15":"North_Nottinghamshire",
		"UKF16":"South_Nottinghamshire",
		"UKF21":"Leicester",
		"UKF22":"Leicestershire_CC_and_Rutland",
		"UKF24":"West_Northamptonshire",
		"UKF25":"North_Northamptonshire",
		"UKF30":"Lincolnshire",
		"UKG11":"Herefordshire_County_of",
		"UKG12":"Worcestershire",
		"UKG13":"Warwickshire",
		"UKG21":"Telford_and_Wrekin",
		"UKG22":"Shropshire_CC",
		"UKG23":"Stoke_on_Trent",
		"UKG24":"Staffordshire_CC",
		"UKG31":"Birmingham",
		"UKG32":"Solihull",
		"UKG33":"Coventry",
		"UKG36":"Dudley",
		"UKG37":"Sandwell",
		"UKG38":"Walsall",
		"UKG39":"Wolverhampton",
		"UKH11":"Peterborough",
		"UKH12":"Cambridgeshire_CC",
		"UKH14":"Suffolk",
		"UKH15":"Norwich_and_East_Norfolk",
		"UKH16":"North_and_West_Norfolk",
		"UKH17":"Breckland_and_South_Norfolk",
		"UKH21":"Luton",
		"UKH23":"Hertfordshire",
		"UKH24":"Bedford",
		"UKH25":"Central_Bedfordshire",
		"UKH31":"Southend_on_Sea",
		"UKH32":"Thurrock",
		"UKH34":"Essex_Haven_Gateway",
		"UKH35":"West_Essex",
		"UKH36":"Heart_of_Essex",
		"UKH37":"Essex_Thames_Gateway",
		"UKI31":"Camden_and_City_of_London",
		"UKI32":"Westminster",
		"UKI33":"Kensington_Chelsea_and_Hammersmith_Fulham",
		"UKI34":"Wandsworth",
		"UKI41":"Hackney_and_Newham",
		"UKI42":"Tower_Hamlets",
		"UKI43":"Haringey_and_Islington",
		"UKI44":"Lewisham_and_Southwark",
		"UKI45":"Lambeth",
		"UKI51":"Bexley_and_Greenwich",
		"UKI52":"Barking_Dagenham_and_Havering",
		"UKI53":"Redbridge_and_Waltham_Forest",
		"UKI54":"Enfield",
		"UKI61":"Bromley",
		"UKI62":"Croydon",
		"UKI63":"Merton_Kingston_upon_Thames_and_Sutton",
		"UKI71":"Barnet",
		"UKI72":"Brent",
		"UKI73":"Ealing",
		"UKI74":"Harrow_and_Hillingdon",
		"UKI75":"Hounslow_and_Richmond_upon_Thames",
		"UKJ11":"Berkshire",
		"UKJ12":"Milton_Keynes",
		"UKJ13":"Buckinghamshire_CC",
		"UKJ14":"Oxfordshire",
		"UKJ21":"Brighton_and_Hove",
		"UKJ22":"East_Sussex_CC",
		"UKJ25":"West_Surrey",
		"UKJ26":"East_Surrey",
		"UKJ27":"West_Sussex_South_West",
		"UKJ28":"West_Sussex_North_East",
		"UKJ31":"Portsmouth",
		"UKJ32":"Southampton",
		"UKJ34":"Isle_of_Wight",
		"UKJ35":"South_Hampshire",
		"UKJ36":"Central_Hampshire",
		"UKJ37":"North_Hampshire",
		"UKJ41":"Medway",
		"UKJ43":"Kent_Thames_Gateway",
		"UKJ44":"East_Kent",
		"UKJ45":"Mid_Kent",
		"UKJ46":"West_Kent",
		"UKK11":"Bristol_City_of",
		"UKK12":"Bath_and_North_East_Somerset_North_Somerset_and_South_Gloucestershire",
		"UKK13":"Gloucestershire",
		"UKK14":"Swindon",
		"UKK15":"Wiltshire_CC",
		"UKK21":"Bournemouth_and_Poole",
		"UKK22":"Dorset_CC",
		"UKK23":"Somerset",
		"UKK30":"Cornwall_and_Isles_of_Scilly",
		"UKK41":"Plymouth",
		"UKK42":"Torbay",
		"UKK43":"Devon_CC",
		"UKL11":"Isle_of_Anglesey",
		"UKL12":"Gwynedd",
		"UKL13":"Conwy_and_Denbighshire",
		"UKL14":"South_West_Wales",
		"UKL15":"Central_Valleys",
		"UKL16":"Gwent_Valleys",
		"UKL17":"Bridgend_and_Neath_Port_Talbot",
		"UKL18":"Swansea",
		"UKL21":"Monmouthshire_and_Newport",
		"UKL22":"Cardiff_and_Vale_of_Glamorgan",
		"UKL23":"Flintshire_and_Wrexham",
		"UKL24":"Powys",
		"UKM50":"Aberdeen_City_and_Aberdeenshire",
		"UKM61":"Caithness_Sutherland_and_Ross_Cromarty",
		"UKM62":"Inverness_Nairn_and_Moray_Badenoch_Strathspey",
		"UKM63":"Lochaber_Skye_Lochalsh_Arran_Cumbrae_and_Argyll_Bute",
		"UKM64":"Eilean_Siar_Western_Isles",
		"UKM65":"Orkney_Islands",
		"UKM66":"Shetland_Islands",
		"UKM71":"Angus_and_Dundee_City",
		"UKM72":"Clackmannanshire_and_Fife",
		"UKM73":"East_Lothian_and_Midlothian",
		"UKM75":"Edinburgh_City_of",
		"UKM76":"Falkirk",
		"UKM77":"Perth_Kinross_and_Stirling",
		"UKM78":"West_Lothian",
		"UKM81":"East_Dunbartonshire_West_Dunbartonshire_and_Helensburgh_Lomond",
		"UKM82":"Glasgow_City",
		"UKM83":"Inverclyde_East_Renfrewshire_and_Renfrewshire",
		"UKM84":"North_Lanarkshire",
		"UKM91":"Scottish_Borders",
		"UKM92":"Dumfries_Galloway",
		"UKM93":"East_Ayrshire_and_North_Ayrshire_mainland",
		"UKM94":"South_Ayrshire",
		"UKM95":"South_Lanarkshire",
		"UKN05":"West_and_South_of_Northern_Ireland",
		"UKN06":"Belfast",
		"UKN07":"Armagh_City_Banbridge_and_Craigavon",
		"UKN08":"Newry_Mourne_and_Down",
		"UKN09":"Ards_and_North_Down",
		"UKN10":"Derry_City_and_Strabane",
		"UKN11":"Mid_Ulster",
		"UKN12":"Causeway_Coast_and_Glens",
		"UKN13":"Antrim_and_Newtownabbey",
		"UKN14":"Lisburn_and_Castlereagh",
		"UKN15":"Mid_and_East_Antrim",
		"UKN16":"Fermanagh_and_Omagh",
		"UKZZZ":"Extra_Regio_NUTS_3_x28",
}

	TRRTRL_UNT = models.CharField("TRRTRL_UNT",max_length=255, choices=NUTS3_INPT_domain,default=None, blank=True, null=True, db_comment="NUTS3_INPT_domain")

	TYP_CLLTRL_INPT_domain = {		"10":"Commercial_real_estate_collateral",
		"106":"Offices_and_commercial_premises_not_related_to_land_collateral",
		"107":"Land_excluding_agriculture",
		"108":"Land_including_agriculture",
		"110":"Software_collateral",
		"111":"Other_immaterial_rights_collateral",
		"12":"Securities",
		"13":"Gold",
		"17":"Trade_receivables",
		"2":"Life_insurance_policies_pledged",
		"66":"Exchange_tradable_derivative_collateral",
		"72":"Other_financial_protection",
		"77":"Currency",
		"8":"Residential_real_estate_collateral",
		"81":"Aircraft_collateral",
		"83":"Ship_collateral",
		"84":"Rolling_stock_collateral",
		"85":"Machinery_and_equiptment_collateral",
		"86":"Inventory_collateral",
		"88":"Other_non_registered_collateral",
		"89":"Other_commodity_collateral",
}

	TYP_CLLTRL = models.CharField("TYP_CLLTRL",max_length=255, choices=TYP_CLLTRL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_CLLTRL_INPT_domain")

	TYP_PRTCTN_VLTN_APPRCH_INPT_domain = {		"0":"Not_applicable",
		"1":"Counterparty_estimation_Valuation_method_whereby_the_valuation_is_carried_out_by_the_provider_of_the_protection",
		"2":"Creditor_valuation_Valuation_method_whereby_the_valuation_is_carried_out_by_the_creditor_valuation_undertaken_by_an_external_or_staff_appraiser_who_possesses_the_necessary_qualifications_ability_and_experience_to_execute_a_valuation_and_who_is_not_independent_from_the_credit_decision_process",
		"3":"Mark_to_market_Valuation_method_whereby_the_protection_value_is_based_on_unadjusted_quoted_prices_for_identical_assets_and_liabilities_in_an_active_market",
		"4":"Other_type_of_valuation_Other_type_of_valuation_not_included_in_any_other_valuation_categories",
		"5":"Third_party_valuation_Valuation_method_in_which_the_valuation_is_provided_by_an_appraiser_who_is_independent_from_the_credit_decision_process",
}

	TYP_PRTCTN_VL_APPRCH = models.CharField("TYP_PRTCTN_VL_APPRCH",max_length=255, choices=TYP_PRTCTN_VLTN_APPRCH_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTCTN_VLTN_APPRCH_INPT_domain")

	UNDR_CNSTRCT_DVLPMNT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Under_construction_or_development",
		"2":"Not_under_construction_or_development",
}

	UNDR_CNSTRCTN_INDCTR = models.CharField("UNDR_CNSTRCTN_INDCTR",max_length=255, choices=UNDR_CNSTRCT_DVLPMNT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="UNDR_CNSTRCT_DVLPMNT_INDCTR_INPT_domain")

	thePRTCTN_ARRNGMNT = models.ForeignKey("PRTCTN_ARRNGMNT", models.SET_NULL,blank=True,null=True,related_name="CLLTRL_to_thePRTCTN_ARRNGMNTs")

	theSCRTY_EXCHNG_TRDBL_DRVTV = models.ForeignKey("SCRTY_EXCHNG_TRDBL_DRVTV", models.SET_NULL,blank=True,null=True,related_name="CLLTRL_to_theSCRTY_EXCHNG_TRDBL_DRVTVs")

	class Meta:

		verbose_name = 'CLLTRL'

		verbose_name_plural = 'CLLTRLs'

class CLLTRL_GVN_INSTRMNT_DBT_SCRTY_ISSD_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CLLTRL_GVN_INSTRMNT_DBT_SCRTY_ISSD_ASSGNMNT_uniqueID = models.CharField("CLLTRL_GVN_INSTRMNT_DBT_SCRTY_ISSD_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CLSSFCTN_LBLTS_domain = {		"21":"IFRS_Financial_liabilities_measured_at_amortised_cost_Financial_liabilities_measured_at_amortised_cost_in_accordance_with_IFRS",
		"23":"IFRS_Financial_liabilities_held_for_trading_Financial_liabilities_held_for_trading_in_accordance_with_IFRS",
		"25":"IFRS_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		"31":"nGAAP_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_accordance_with_national_GAAP_based_on_BAD",
		"33":"nGAAP_Trading_financial_liabilities_Trading_financial_liabilities_in_accordance_with_national_GAAP_based_on_BAD",
		"35":"nGAAP_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_nationa_GAAP_based_on_BAD",
		"85":"nGAAP_Accounting_portfolios_for_trading_financial_instruments_Cost_based_method_or_LOCOM",
}

	ACCNTNG_CLSSFCTN = models.CharField("ACCNTNG_CLSSFCTN",max_length=255, choices=ACCNTNG_CLSSFCTN_LBLTS_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CLSSFCTN_LBLTS_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"12":"Non_balance_sheet_recognised_financial_liability_instrument",
		"34":"Balance_sheet_recognised_financial_asset_instrument_according_to_national_general_accepted_accounting_principles_nGAAP",
		"35":"Balance_sheet_recognised_financial_asset_instrument_according_to_International_Financial_Reporting_Standard_IFRS",
		"37":"Non_fair_valued_balance_sheet_recognised_financial_liability_instrument",
		"38":"Over_the_counter_OTC_Credit_default_swap_received_as_collateral_instrument",
		"39":"Other_collateral_received_instrument",
		"46":"Fair_valued_Balance_sheet_recognised_financial_liability_instrument_according_to_International_Financial_Reporting_Standard_IFRS",
		"47":"Fair_valued_balance_sheet_recognised_financial_liability_instrument_according_to_national_general_accepted_accounting_principles_nGAAP",
		"501":"Forborne_off_balance_sheet_item_given_instrument",
		"502":"Non_Forborne_off_balance_sheet_item_given_instrument",
		"6":"Off_balance_sheet_item_received_instrument",
		"8":"Collateral_given_instrument",
}

	TYP_INSTRMNT_RL = models.CharField("TYP_INSTRMNT_RL",max_length=255, choices=INSTRMNT_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="INSTRMNT_RL_TYP_INPT_domain")

	PRTCTN_ALLCTD_VL = models.BigIntegerField("PRTCTN_ALLCTD_VL",default=None, blank=True, null=True)

	theDBT_SCRTY_ISSD = models.ForeignKey("DBT_SCRTY_ISSD", models.SET_NULL,blank=True,null=True,related_name="CLLTRL_GVN_INSTRMNT_DBT_SCRTY_ISSD_ASSGNMNT_to_theDBT_SCRTY_ISSDs")

	theINSTRMNT_RL = models.ForeignKey("INSTRMNT_RL", models.SET_NULL,blank=True,null=True,related_name="CLLTRL_GVN_INSTRMNT_DBT_SCRTY_ISSD_ASSGNMNT_to_theINSTRMNT_RLs")

	class Meta:

		verbose_name = 'CLLTRL_GVN_INSTRMNT_DBT_SCRTY_ISSD_ASSGNMNT'

		verbose_name_plural = 'CLLTRL_GVN_INSTRMNT_DBT_SCRTY_ISSD_ASSGNMNTs'

class CLLTRL_NN_FNNCL_ASST_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CLLTRL_NN_FNNCL_ASST_ASSGNMNT_uniqueID = models.CharField("CLLTRL_NN_FNNCL_ASST_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	HLD_SL_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Held_for_sale_The_member_indicates_that_the_instrument_is_held_for_sale",
		"2":"Not_held_for_sale_The_member_indicates_that_the_instrument_is_not_held_for_sale",
}

	HLD_SL_INDCTR = models.CharField("HLD_SL_INDCTR",max_length=255, choices=HLD_SL_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="HLD_SL_INDCTR_INPT_domain")

	MSRMNT_MTHD_INPT_domain = {		"0":"Not_applicable",
		"1":"Cost_model_IAS_17_49_IAS_16_30_73_a_d",
		"3":"Revaluation_model_IAS_17_49_IAS_16_31_73_a_d",
}

	MSRMNT_MTHD = models.CharField("MSRMNT_MTHD",max_length=255, choices=MSRMNT_MTHD_INPT_domain,default=None, blank=True, null=True, db_comment="MSRMNT_MTHD_INPT_domain")

	NN_FNNCL_ASST_ID = models.CharField("NN_FNNCL_ASST_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SBJCT_OPRTNG_LS_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Subject_to_operating_lease_The_asset_is_subject_to_operating_lease",
		"2":"Not_Subject_to_operating_lease_The_asset_is_not_subject_to_operating_lease",
}

	SBJCT_OPRTNG_LS_INDCTR = models.CharField("SBJCT_OPRTNG_LS_INDCTR",max_length=255, choices=SBJCT_OPRTNG_LS_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="SBJCT_OPRTNG_LS_INDCTR_INPT_domain")

	SFTWR_ASST_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Software_assets",
		"2":"Not_software_assets",
}

	SFTWR_ASST_INDCTR = models.CharField("SFTWR_ASST_INDCTR",max_length=255, choices=SFTWR_ASST_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="SFTWR_ASST_INDCTR_INPT_domain")

	TM_SNC_INTL_RCGNTN_INPT_domain = {		"0":"Not_Applicable",
		"27":"_lt_eq_2_years",
		"29":"_gt_2_years_lt_eq_5_years",
		"37":"_gt_5_years",
}

	TM_SNC_INTL_RCGNTN = models.CharField("TM_SNC_INTL_RCGNTN",max_length=255, choices=TM_SNC_INTL_RCGNTN_INPT_domain,default=None, blank=True, null=True, db_comment="TM_SNC_INTL_RCGNTN_INPT_domain")

	TYP_NN_FNNCL_ASST_INPT_domain = {		"14":"Other_intangible_asset_not_taken_into_possession",
		"15":"Other_intangible_asset_taken_into_possession",
		"413":"Tangible_assets_Investment_property",
		"420":"Intangible_assets_Goodwill",
		"440":"Current_tax_assets",
		"450":"Deferred_tax_assets",
		"46":"Other_non_financial_asset_not_taken_into_possession",
		"48":"Other_non_financial_asset_taken_into_possession_before_the_period",
		"49":"Other_non_financial_asset_taken_into_possession_during_the_period",
		"6301":"Software_property_plant_and_equipment_not_taken_into_possession",
		"6302":"Non_software_property_plant_and_equipment_not_taken_into_possession",
		"66":"Software_property_plant_and_equipment_taken_into_possession",
		"67":"Non_software_property_plant_and_equipment_taken_into_possession",
}

	TYP_NN_FNNCL_ASST = models.CharField("TYP_NN_FNNCL_ASST",max_length=255, choices=TYP_NN_FNNCL_ASST_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_NN_FNNCL_ASST_INPT_domain")

	CLLTRL_NN_FNNCL_ASST_ASSGNMNT_TYP_domain = {		"1":"Physical_collateral_Investment_property_assignment",
		"2":"Immaterial_rights_as_collateral_Other_intangible_asset_not_taken_into_possession_assignment",
		"3":"Immaterial_rights_as_collateral_Other_intangible_asset_taken_into_possession_assignment",
		"4":"Software_collateral_Software_property_plant_and_equipment_not_taken_into_possession_assignment",
		"5":"Physical_collateral_Non_software_property_plant_and_equipment_not_taken_into_possession_assignment",
		"6":"Software_collateral_Software_property_plant_and_equipment_taken_into_possession_assignment",
		"7":"Physical_collateral_Non_software_property_plant_and_equipment_taken_into_possession_assignment",
}

	CLLTRL_NN_FNNCL_ASST_ASSGNMNT_TYP = models.CharField("CLLTRL_NN_FNNCL_ASST_ASSGNMNT_TYP",max_length=255, choices=CLLTRL_NN_FNNCL_ASST_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="CLLTRL_NN_FNNCL_ASST_ASSGNMNT_TYP_domain")

	theCLLTRL = models.ForeignKey("CLLTRL", models.SET_NULL,blank=True,null=True,related_name="CLLTRL_NN_FNNCL_ASST_ASSGNMNT_to_theCLLTRLs")

	theNN_FNNCL_ASST = models.ForeignKey("NN_FNNCL_ASST", models.SET_NULL,blank=True,null=True,related_name="CLLTRL_NN_FNNCL_ASST_ASSGNMNT_to_theNN_FNNCL_ASSTs")

	class Meta:

		verbose_name = 'CLLTRL_NN_FNNCL_ASST_ASSGNMNT'

		verbose_name_plural = 'CLLTRL_NN_FNNCL_ASST_ASSGNMNTs'

class CLLTRL_RL(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CLLTRL_RL_uniqueID = models.CharField("CLLTRL_RL_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	CLLTRL_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"1":"Collateral_received",
		"2":"Collateral_given",
}

	CLLTRL_RL_TYP = models.CharField("CLLTRL_RL_TYP",max_length=255, choices=CLLTRL_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="CLLTRL_RL_TYP_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	AVLBL_ENCMBRNC_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Available_for_encumbrance",
		"2":"Not_available_for_encumbrance",
}

	AVLBL_ENCMBRNC_INDCTR = models.CharField("AVLBL_ENCMBRNC_INDCTR",max_length=255, choices=AVLBL_ENCMBRNC_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="AVLBL_ENCMBRNC_INDCTR_INPT_domain")

	theCLLTRL = models.ForeignKey("CLLTRL", models.SET_NULL,blank=True,null=True,related_name="CLLTRL_RL_to_theCLLTRLs")

	class Meta:

		verbose_name = 'CLLTRL_RL'

		verbose_name_plural = 'CLLTRL_RLs'

class CRDT_FCLTY(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CRDT_FCLTY_uniqueID = models.CharField("CRDT_FCLTY_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CRDT_FCLTY_ID = models.CharField("CRDT_FCLTY_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ACCMLTD_CHNGS_FV = models.BigIntegerField("ACCMLTD_CHNGS_FV",default=None, blank=True, null=True)

	ACCMLTD_CHNGS_FV_CR = models.BigIntegerField("ACCMLTD_CHNGS_FV_CR",default=None, blank=True, null=True)

	ACCMLTD_NGTV_VL_ADJSTMNT_CR = models.BigIntegerField("ACCMLTD_NGTV_VL_ADJSTMNT_CR",default=None, blank=True, null=True)

	ACCMLTD_NGTV_VL_ADJSTMNT_MR = models.BigIntegerField("ACCMLTD_NGTV_VL_ADJSTMNT_MR",default=None, blank=True, null=True)

	OFF_BLNC_SHT_ACCNTNG_CLSSFCTN_domain = {		"90":"Under_IFRS_9_impairment_Off_balance_sheet_accounting_classification_under_IFRS_9_impairment",
		"911":"Measured_under_IAS_37_Off_balance_sheet_accounting_classification_measured_under_IAS_37",
		"912":"Measured_under_IFRS_4_Off_balance_sheet_accounting_classification_measured_under_IFRS_4",
		"92":"Measured_at_fair_value_through_profit_or_loss_Off_balance_sheet_accounting_classification_IFRS_9_fair_valued_commitments_and_financial_guarantees",
		"93":"Under_nGAAP_Off_balance_sheet_accounting_classification_measured_under_nGAAP_based_on_BAD",
}

	ACCNTNG_CLSSFCTN = models.CharField("ACCNTNG_CLSSFCTN",max_length=255, choices=OFF_BLNC_SHT_ACCNTNG_CLSSFCTN_domain,default=None, blank=True, null=True, db_comment="OFF_BLNC_SHT_ACCNTNG_CLSSFCTN_domain")

	ANNLSD_AGRD_RT = models.FloatField("ANNLSD_AGRD_RT",default=None, blank=True, null=True)

	APPRCH_CRDT_QLTY_STTS_domain = {		"1":"Debtor_based_Total_obligations_of_a_borrower",
		"2":"Transaction_based_Individual_credit_facility",
}

	APPRCH_CRDT_QLTY_STTS = models.CharField("APPRCH_CRDT_QLTY_STTS",max_length=255, choices=APPRCH_CRDT_QLTY_STTS_domain,default=None, blank=True, null=True, db_comment="APPRCH_CRDT_QLTY_STTS_domain")

	ISO4217_domain = {		"AED":"UAE_Dirham",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"ARS":"Argentine_Peso",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYN":"Belarussian_Ruble",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHE":"WIR_Euro",
		"CHF":"Swiss_franc",
		"CHW":"WIR_Franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CZK":"Czech_koruna",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GTQ":"Quetzal",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"ILS":"New_Israeli_Sheqel",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MRU":"Ouguiya_x2",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDG":"Sudanese_Pound",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SRD":"Surinam_Dollar",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"STN":"Dobra_x2",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJS":"Somoni",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"USN":"US_Dollar_Next_day",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UYW":"Unidad_Previsional",
		"UZS":"Uzbekistan_Sum",
		"VEF":"Bolivar",
		"VES":"Bolivar_Soberano",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XAG":"Silver_one_Troy_ounce",
		"XAU":"Gold_one_Troy_ounce",
		"XBA":"Bond_Markets_Unit_European_Composite_Unit_EURCO",
		"XBB":"Bond_Markets_Unit_European_Monetary_Unit_E_M_U_6",
		"XBC":"Bond_Markets_Unit_European_Unit_of_Account_9_E_U_A_9",
		"XBD":"Bond_Markets_Unit_European_Unit_of_Account_17_E_U_A_17",
		"XCD":"East_Caribbean_Dollar",
		"XDR":"Special_Drawing_Rights_SDR",
		"XOF":"CFA_Franc_BCEAO",
		"XPD":"Palladium_one_Troy_ounce",
		"XPF":"CFP_Franc",
		"XPT":"Platinum_one_Troy_ounce",
		"XSU":"Sucre",
		"XTS":"Codes_specifically_reserved_for_testing_purposes",
		"XUA":"ADB_Unit_of_Account",
		"XXX":"Code_assigned_for_transactions_where_no_currency_is_involved",
		"YER":"Yemeni_Rial",
		"ZAR":"South_African_Rand",
		"ZMW":"Zambian_Kwacha",
		"ZWL":"Zimbabwe_Dollar",
}

	CRRNCY = models.CharField("CRRNCY",max_length=255, choices=ISO4217_domain,default=None, blank=True, null=True, db_comment="ISO4217_domain")

	DFLT_STTS_domain = {		"14":"Not_in_default",
		"18":"Default_because_both_unlikely_to_pay_and_more_than_90_180_days_past_due",
		"19":"Default_because_unlikely_to_pay",
		"20":"Default_because_more_than_90_180_days_past_due",
}

	DFLT_STTS = models.CharField("DFLT_STTS",max_length=255, choices=DFLT_STTS_domain,default=None, blank=True, null=True, db_comment="DFLT_STTS_domain")

	DRVD_DFLT_STTS_domain = {		"14":"Not_in_default",
		"6":"Default",
}

	DFLT_STTS_DRVD = models.CharField("DFLT_STTS_DRVD",max_length=255, choices=DRVD_DFLT_STTS_domain,default=None, blank=True, null=True, db_comment="DRVD_DFLT_STTS_domain")

	DT_DFLT_STTS = models.DateTimeField("DT_DFLT_STTS",default=None, blank=True, null=True)

	DT_FRBRNC_MSRS = models.DateTimeField("DT_FRBRNC_MSRS",default=None, blank=True, null=True)

	DT_FRBRNC_STTS = models.DateTimeField("DT_FRBRNC_STTS",default=None, blank=True, null=True)

	DT_INCPTN = models.DateTimeField("DT_INCPTN",default=None, blank=True, null=True)

	DT_LGL_FNL_MTRTY = models.DateTimeField("DT_LGL_FNL_MTRTY",default=None, blank=True, null=True)

	DT_PRFRMNG_STTS = models.DateTimeField("DT_PRFRMNG_STTS",default=None, blank=True, null=True)

	DT_PST_D = models.DateTimeField("DT_PST_D",default=None, blank=True, null=True)

	DT_STTLMNT = models.DateTimeField("DT_STTLMNT",default=None, blank=True, null=True)

	ENCMBRD_ASST_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Not_encumbered_asset",
		"100":"Encumbered_asset",
}

	ENCMBRD_ASST_INDCTR = models.CharField("ENCMBRD_ASST_INDCTR",max_length=255, choices=ENCMBRD_ASST_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="ENCMBRD_ASST_INDCTR_INPT_domain")

	FRBRNC_MSR_TYP_domain = {		"0":"Not_applicable",
		"1":"Grace_period_payment_moratorium",
		"10":"Forborne_instruments_with_modified_interest_rate_below_market_conditions",
		"11":"Forborne_instruments_with_modified_interest_rate_not_below_market_conditions",
		"3":"Extension_of_maturity_term",
		"4":"Rescheduled_payments",
		"5":"Debt_forgiveness",
		"6":"Debt_asset_swaps",
		"7":"Other_forbearance_measures",
		"8":"Forborne_Refinanced_debt",
		"9":"Forborne_instruments_with_other_modified_terms_and_conditions",
}

	FRBRNC_MSR_TYP = models.CharField("FRBRNC_MSR_TYP",max_length=255, choices=FRBRNC_MSR_TYP_domain,default=None, blank=True, null=True, db_comment="FRBRNC_MSR_TYP_domain")

	FRZNG_PRD_DYS = models.BigIntegerField("FRZNG_PRD_DYS",default=None, blank=True, null=True)

	FV = models.BigIntegerField("FV",default=None, blank=True, null=True)

	GNRL_ALLWNCS_BNK_RSK = models.BigIntegerField("GNRL_ALLWNCS_BNK_RSK",default=None, blank=True, null=True)

	GNRL_ALLWNCS_CRDT_RSK = models.BigIntegerField("GNRL_ALLWNCS_CRDT_RSK",default=None, blank=True, null=True)

	IMPRMNT_STTS_domain = {		"211":"General_allowances_for_credit_risk_GAAP",
		"212":"General_allowances_for_banking_risk_GAAP",
		"23":"Stage_1_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_12_month_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"24":"Stage_2_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"25":"Stage_3_IFRS_To_be_used_if_the_instrument_is_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"26":"Specific_allowances_GAAP_To_be_used_if_the_instrument_is_subject_to_impairment_in_accordance_with_an_applied_accounting_standard_other_than_IFRS_9_and_specific_loss_allowances_are_raised_irrespective_of_whether_these_allowances_are_individually_or_collectively_assessed_impaired",
		"27":"Purchased_or_originated_credit_impaired_instruments_POCI_IFRS",
}

	IMPRMNT_STTS = models.CharField("IMPRMNT_STTS",max_length=255, choices=IMPRMNT_STTS_domain,default=None, blank=True, null=True, db_comment="IMPRMNT_STTS_domain")

	NMNL_AMNT = models.BigIntegerField("NMNL_AMNT",default=None, blank=True, null=True)

	NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain = {		"1":"Non_performing_prior_to_forbearance",
		"2":"Not_non_performing_prior_to_forbearance",
}

	NN_PRFRMNG_PRR_FRBRNC_INDCTR = models.CharField("NN_PRFRMNG_PRR_FRBRNC_INDCTR",max_length=255, choices=NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain,default=None, blank=True, null=True, db_comment="NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain")

	NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain = {		"1":"Non_performing_prior_to_forbearance",
		"2":"Not_non_performing_prior_to_forbearance",
}

	PRFRMNG_FRBRN_EXPSR_UNDR_PRBTN_RCLSSFD_NN_PRFRMNG_INDCTR = models.CharField("PRFRMNG_FRBRN_EXPSR_UNDR_PRBTN_RCLSSFD_NN_PRFRMNG_INDCTR",max_length=255, choices=NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain,default=None, blank=True, null=True, db_comment="NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain")

	PRFRMNG_STTS_domain = {		"1":"Non_performing",
		"11":"Performing",
}

	PRFRMNG_STTS = models.CharField("PRFRMNG_STTS",max_length=255, choices=PRFRMNG_STTS_domain,default=None, blank=True, null=True, db_comment="PRFRMNG_STTS_domain")

	PRFRMNG_STTS_RSN_domain = {		"1":"Failed_reclassification_to_performing_at_end_of_probation_period",
		"2":"Exited_from_Non_performing_exposure_NPE_in_the_last_12_months",
}

	PRFRMNG_STTS_RSN = models.CharField("PRFRMNG_STTS_RSN",max_length=255, choices=PRFRMNG_STTS_RSN_domain,default=None, blank=True, null=True, db_comment="PRFRMNG_STTS_RSN_domain")

	PRVSNS_OFF_BLNC_SHT = models.BigIntegerField("PRVSNS_OFF_BLNC_SHT",default=None, blank=True, null=True)

	RNGTTN_STTS_domain = {		"1":"Renegotiated_instrument_with_forbearance_measures",
		"9":"Renegotiated_instrument_without_forbearance_measures",
}

	RNGTTN_STTS = models.CharField("RNGTTN_STTS",max_length=255, choices=RNGTTN_STTS_domain,default=None, blank=True, null=True, db_comment="RNGTTN_STTS_domain")

	RTL_EXPSR_ACCRDNG_CRR_INDCTR_domain = {		"1":"Retail_exposure_accordign_to_CRR_Article_123_b",
		"2":"Not_retail_exposure_accordign_to_CRR_Article_123_b",
}

	RTL_EXPSR_ACCRDNG_CRR_INDCTR = models.CharField("RTL_EXPSR_ACCRDNG_CRR_INDCTR",max_length=255, choices=RTL_EXPSR_ACCRDNG_CRR_INDCTR_domain,default=None, blank=True, null=True, db_comment="RTL_EXPSR_ACCRDNG_CRR_INDCTR_domain")

	RVCBL_INDCTR_domain = {		"1":"Revocable",
		"2":"Not_revocable",
}

	RVCBL_INDCTR = models.CharField("RVCBL_INDCTR",max_length=255, choices=RVCBL_INDCTR_domain,default=None, blank=True, null=True, db_comment="RVCBL_INDCTR_domain")

	TM_PST_DU_BND_domain = {		"1002":"_0_days",
		"12":"_gt_3_months_lt_eq_6_months",
		"16":"_gt_6_months_lt_eq_12_months",
		"21":"_gt_1_year_lt_eq_2_years",
		"29":"_gt_2_years_lt_eq_5_years",
		"75":"_gt_eq_1_day_lt_eq_30_days",
		"84":"_gt_5_year_lt_eq_7_years",
		"85":"_gt_7_years",
		"9":"_gt_30_days_lt_eq_90_days",
}

	TM_PST_DU_BND = models.CharField("TM_PST_DU_BND",max_length=255, choices=TM_PST_DU_BND_domain,default=None, blank=True, null=True, db_comment="TM_PST_DU_BND_domain")

	TYP_CRDT_FCLTY_domain = {		"12":"To_lend_or_to_provide_acceptance_facilities_at_a_below_market_interest_rate",
		"13":"To_lend_or_to_provide_acceptance_facilities_under_pre_specified_terms_and_conditions_other_than_those_at_a_below_market_interest_rate",
		"14":"To_lend_or_to_provide_acceptance_facilities_where_the_terms_and_conditions_are_not_under_pre_specified",
		"15":"To_provide_guarantees",
		"16":"To_purchase_securities",
		"17":"For_tender_and_performance_guarantees",
		"18":"Other_Credit_Facilities_Other",
}

	TYP_CRDT_FCLTY = models.CharField("TYP_CRDT_FCLTY",max_length=255, choices=TYP_CRDT_FCLTY_domain,default=None, blank=True, null=True, db_comment="TYP_CRDT_FCLTY_domain")

	theFNNCL_CNTRCT = models.ForeignKey("FNNCL_CNTRCT", models.SET_NULL,blank=True,null=True,related_name="CRDT_FCLTY_to_theFNNCL_CNTRCTs")

	class Meta:

		verbose_name = 'CRDT_FCLTY'

		verbose_name_plural = 'CRDT_FCLTYs'

class CRDT_FCLTY_CLLTRL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CRDT_FCLTY_CLLTRL_ASSGNMNT_uniqueID = models.CharField("CRDT_FCLTY_CLLTRL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	CLLTRL_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"1":"Collateral_received",
		"2":"Collateral_given",
}

	CLLTRL_RL_TYP = models.CharField("CLLTRL_RL_TYP",max_length=255, choices=CLLTRL_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="CLLTRL_RL_TYP_INPT_domain")

	CRDT_FCLTY_ID = models.CharField("CRDT_FCLTY_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	theCLLTRL_RL = models.ForeignKey("CLLTRL_RL", models.SET_NULL,blank=True,null=True,related_name="CRDT_FCLTY_CLLTRL_ASSGNMNT_to_theCLLTRL_RLs")

	theCRDT_FCLTY = models.ForeignKey("CRDT_FCLTY", models.SET_NULL,blank=True,null=True,related_name="CRDT_FCLTY_CLLTRL_ASSGNMNT_to_theCRDT_FCLTYs")

	class Meta:

		verbose_name = 'CRDT_FCLTY_CLLTRL_ASSGNMNT'

		verbose_name_plural = 'CRDT_FCLTY_CLLTRL_ASSGNMNTs'

class CRDT_FCLTY_CLLTRL_RCVD_INSTRMNT_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CRDT_FCLTY_CLLTRL_RCVD_INSTRMNT_ASSGNMNT_uniqueID = models.CharField("CRDT_FCLTY_CLLTRL_RCVD_INSTRMNT_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CRDT_FCLTY_ID = models.CharField("CRDT_FCLTY_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"12":"Non_balance_sheet_recognised_financial_liability_instrument",
		"34":"Balance_sheet_recognised_financial_asset_instrument_according_to_national_general_accepted_accounting_principles_nGAAP",
		"35":"Balance_sheet_recognised_financial_asset_instrument_according_to_International_Financial_Reporting_Standard_IFRS",
		"37":"Non_fair_valued_balance_sheet_recognised_financial_liability_instrument",
		"38":"Over_the_counter_OTC_Credit_default_swap_received_as_collateral_instrument",
		"39":"Other_collateral_received_instrument",
		"46":"Fair_valued_Balance_sheet_recognised_financial_liability_instrument_according_to_International_Financial_Reporting_Standard_IFRS",
		"47":"Fair_valued_balance_sheet_recognised_financial_liability_instrument_according_to_national_general_accepted_accounting_principles_nGAAP",
		"501":"Forborne_off_balance_sheet_item_given_instrument",
		"502":"Non_Forborne_off_balance_sheet_item_given_instrument",
		"6":"Off_balance_sheet_item_received_instrument",
		"8":"Collateral_given_instrument",
}

	TYP_INSTRMNT_RL = models.CharField("TYP_INSTRMNT_RL",max_length=255, choices=INSTRMNT_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="INSTRMNT_RL_TYP_INPT_domain")

	PRTCTN_ALLCTD_VL = models.BigIntegerField("PRTCTN_ALLCTD_VL",default=None, blank=True, null=True)

	theCRDT_FCLTY = models.ForeignKey("CRDT_FCLTY", models.SET_NULL,blank=True,null=True,related_name="CRDT_FCLTY_CLLTRL_RCVD_INSTRMNT_ASSGNMNT_to_theCRDT_FCLTYs")

	theINSTRMNT_RL = models.ForeignKey("INSTRMNT_RL", models.SET_NULL,blank=True,null=True,related_name="CRDT_FCLTY_CLLTRL_RCVD_INSTRMNT_ASSGNMNT_to_theINSTRMNT_RLs")

	class Meta:

		verbose_name = 'CRDT_FCLTY_CLLTRL_RCVD_INSTRMNT_ASSGNMNT'

		verbose_name_plural = 'CRDT_FCLTY_CLLTRL_RCVD_INSTRMNT_ASSGNMNTs'

class CRDT_FCLTY_ENTTY_RL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CRDT_FCLTY_ENTTY_RL_ASSGNMNT_uniqueID = models.CharField("CRDT_FCLTY_ENTTY_RL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CRDT_FCLTY_ID = models.CharField("CRDT_FCLTY_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	PRTY_RL_TYP = models.CharField("PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	CRDT_FCLTY_ENTTY_RL_ASSGNMNT_TYP_domain = {		"1":"Credit_facility_Creditor_assignment",
		"2":"Credit_facility_Debtor_assignment",
		"3":"Credit_facility_Servicer_assignment",
}

	CRDT_FCLTY_ENTTY_RL_ASSGNMNT_TYP = models.CharField("CRDT_FCLTY_ENTTY_RL_ASSGNMNT_TYP",max_length=255, choices=CRDT_FCLTY_ENTTY_RL_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="CRDT_FCLTY_ENTTY_RL_ASSGNMNT_TYP_domain")

	theCRDT_FCLTY = models.ForeignKey("CRDT_FCLTY", models.SET_NULL,blank=True,null=True,related_name="CRDT_FCLTY_ENTTY_RL_ASSGNMNT_to_theCRDT_FCLTYs")

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="CRDT_FCLTY_ENTTY_RL_ASSGNMNT_to_theENTTY_RLs")

	class Meta:

		verbose_name = 'CRDT_FCLTY_ENTTY_RL_ASSGNMNT'

		verbose_name_plural = 'CRDT_FCLTY_ENTTY_RL_ASSGNMNTs'

class CRDT_RSK_MTGTN_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CRDT_RSK_MTGTN_ASSGNMNT_uniqueID = models.CharField("CRDT_RSK_MTGTN_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTCTN_ID = models.CharField("PRTCTN_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	theCLLTRL = models.ForeignKey("CLLTRL", models.SET_NULL,blank=True,null=True,related_name="CRDT_RSK_MTGTN_ASSGNMNT_to_theCLLTRLs")

	thePRTCTN_ARRNGMNT = models.ForeignKey("PRTCTN_ARRNGMNT", models.SET_NULL,blank=True,null=True,related_name="CRDT_RSK_MTGTN_ASSGNMNT_to_thePRTCTN_ARRNGMNTs")

	class Meta:

		verbose_name = 'CRDT_RSK_MTGTN_ASSGNMNT'

		verbose_name_plural = 'CRDT_RSK_MTGTN_ASSGNMNTs'

class CRDT_TRNSFR_OTHR_SCRTSTN_CVRD_BND_PRGRM(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CRDT_TRNSFR_OTHR_SCRTSTN_CVRD_BND_PRGRM_uniqueID = models.CharField("CRDT_TRNSFR_OTHR_SCRTSTN_CVRD_BND_PRGRM_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CRDT_TRNSFR_OTHR_SCRTSTN_CVRD_BND_PRGRM_ID = models.CharField("CRDT_TRNSFR_OTHR_SCRTSTN_CVRD_BND_PRGRM_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSN_OTHR_CRDT_TRNSFR_TYP_domain = {		"5":"Covered_bond_programme",
		"6":"Credit_transfer_other_than_securitisation_and_covered_bond_program",
		"7":"Securitisation",
}

	SCRTSN_OTHR_CRDT_TRNSFR_TYP = models.CharField("SCRTSN_OTHR_CRDT_TRNSFR_TYP",max_length=255, choices=SCRTSN_OTHR_CRDT_TRNSFR_TYP_domain,default=None, blank=True, null=True, db_comment="SCRTSN_OTHR_CRDT_TRNSFR_TYP_domain")

	theASST_PL = models.ForeignKey("ASST_PL", models.SET_NULL,blank=True,null=True,related_name="CRDT_TRNSFR_OTHR_SCRTSTN_CVRD_BND_PRGRM_to_theASST_PLs")

	class Meta:

		verbose_name = 'CRDT_TRNSFR_OTHR_SCRTSTN_CVRD_BND_PRGRM'

		verbose_name_plural = 'CRDT_TRNSFR_OTHR_SCRTSTN_CVRD_BND_PRGRMs'

class CSH_HND(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CSH_HND_uniqueID = models.CharField("CSH_HND_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	ACCNTNG_FRMWRK_domain = {		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_domain")

	ISO4217_domain = {		"AED":"UAE_Dirham",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"ARS":"Argentine_Peso",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYN":"Belarussian_Ruble",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHE":"WIR_Euro",
		"CHF":"Swiss_franc",
		"CHW":"WIR_Franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CZK":"Czech_koruna",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GTQ":"Quetzal",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"ILS":"New_Israeli_Sheqel",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MRU":"Ouguiya_x2",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDG":"Sudanese_Pound",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SRD":"Surinam_Dollar",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"STN":"Dobra_x2",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJS":"Somoni",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"USN":"US_Dollar_Next_day",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UYW":"Unidad_Previsional",
		"UZS":"Uzbekistan_Sum",
		"VEF":"Bolivar",
		"VES":"Bolivar_Soberano",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XAG":"Silver_one_Troy_ounce",
		"XAU":"Gold_one_Troy_ounce",
		"XBA":"Bond_Markets_Unit_European_Composite_Unit_EURCO",
		"XBB":"Bond_Markets_Unit_European_Monetary_Unit_E_M_U_6",
		"XBC":"Bond_Markets_Unit_European_Unit_of_Account_9_E_U_A_9",
		"XBD":"Bond_Markets_Unit_European_Unit_of_Account_17_E_U_A_17",
		"XCD":"East_Caribbean_Dollar",
		"XDR":"Special_Drawing_Rights_SDR",
		"XOF":"CFA_Franc_BCEAO",
		"XPD":"Palladium_one_Troy_ounce",
		"XPF":"CFP_Franc",
		"XPT":"Platinum_one_Troy_ounce",
		"XSU":"Sucre",
		"XTS":"Codes_specifically_reserved_for_testing_purposes",
		"XUA":"ADB_Unit_of_Account",
		"XXX":"Code_assigned_for_transactions_where_no_currency_is_involved",
		"YER":"Yemeni_Rial",
		"ZAR":"South_African_Rand",
		"ZMW":"Zambian_Kwacha",
		"ZWL":"Zimbabwe_Dollar",
}

	CRRNCY = models.CharField("CRRNCY",max_length=255, choices=ISO4217_domain,default=None, blank=True, null=True, db_comment="ISO4217_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	ENCMBRD_ASST_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Not_encumbered_asset",
		"100":"Encumbered_asset",
}

	ENCMBRD_ASST_INDCTR = models.CharField("ENCMBRD_ASST_INDCTR",max_length=255, choices=ENCMBRD_ASST_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="ENCMBRD_ASST_INDCTR_INPT_domain")

	HLD_SL_INDCTR_domain = {		"1":"Held_for_sale_The_member_indicates_that_the_instrument_is_held_for_sale",
		"2":"Not_held_for_sale_The_member_indicates_that_the_instrument_is_not_held_for_sale",
}

	HLD_SL_INDCTR = models.CharField("HLD_SL_INDCTR",max_length=255, choices=HLD_SL_INDCTR_domain,default=None, blank=True, null=True, db_comment="HLD_SL_INDCTR_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	CRRYNG_AMNT = models.BigIntegerField("CRRYNG_AMNT",default=None, blank=True, null=True)

	class Meta:

		verbose_name = 'CSH_HND'

		verbose_name_plural = 'CSH_HNDs'

class CVRD_BND_ISSNC(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CVRD_BND_ISSNC_uniqueID = models.CharField("CVRD_BND_ISSNC_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CVRD_BND_PRGRM_ID = models.CharField("CVRD_BND_PRGRM_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	theCVRD_BND_PRGRM = models.ForeignKey("CVRD_BND_PRGRM", models.SET_NULL,blank=True,null=True,related_name="CVRD_BND_ISSNC_to_theCVRD_BND_PRGRMs")

	theSCRTY_EXCHNG_TRDBL_DRVTV = models.ForeignKey("SCRTY_EXCHNG_TRDBL_DRVTV", models.SET_NULL,blank=True,null=True,related_name="CVRD_BND_ISSNC_to_theSCRTY_EXCHNG_TRDBL_DRVTVs")

	class Meta:

		verbose_name = 'CVRD_BND_ISSNC'

		verbose_name_plural = 'CVRD_BND_ISSNCs'

class CVRD_BND_PRGRM(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CVRD_BND_PRGRM_uniqueID = models.CharField("CVRD_BND_PRGRM_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CVRD_BND_PRGRM_ID = models.CharField("CVRD_BND_PRGRM_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSN_OTHR_CRDT_TRNSFR_TYP = models.CharField("SCRTSN_OTHR_CRDT_TRNSFR_TYP",max_length=255,default=None, blank=True, null=True)

	theASST_PL = models.ForeignKey("ASST_PL", models.SET_NULL,blank=True,null=True,related_name="CVRD_BND_PRGRM_to_theASST_PLs")

	class Meta:

		verbose_name = 'CVRD_BND_PRGRM'

		verbose_name_plural = 'CVRD_BND_PRGRMs'

class CVRD_BND_PRGRMM_RLVNT_RGM_EXCSS(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	CVRD_BND_PRGRMM_RLVNT_RGM_EXCSS_uniqueID = models.CharField("CVRD_BND_PRGRMM_RLVNT_RGM_EXCSS_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CVRD_BND_PRGRM_ID = models.CharField("CVRD_BND_PRGRM_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	EXCSS_CVRG_ASST_SPCFC_VL = models.BigIntegerField("EXCSS_CVRG_ASST_SPCFC_VL",default=None, blank=True, null=True)

	EXCSS_CVRG_NML_AMNT = models.BigIntegerField("EXCSS_CVRG_NML_AMNT",default=None, blank=True, null=True)

	EXCSS_CVRG_PRSNT_VL_MRKT_VL = models.BigIntegerField("EXCSS_CVRG_PRSNT_VL_MRKT_VL",default=None, blank=True, null=True)

	theCVRD_BND_PRGRM = models.ForeignKey("CVRD_BND_PRGRM", models.SET_NULL,blank=True,null=True,related_name="CVRD_BND_PRGRMM_RLVNT_RGM_EXCSS_to_theCVRD_BND_PRGRMs")

	class Meta:

		verbose_name = 'CVRD_BND_PRGRMM_RLVNT_RGM_EXCSS'

		verbose_name_plural = 'CVRD_BND_PRGRMM_RLVNT_RGM_EXCSSs'

class DBT_SCRTY_ISSD(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_uniqueID = models.CharField("DBT_SCRTY_ISSD_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CLSSFCTN_LBLTS_domain = {		"21":"IFRS_Financial_liabilities_measured_at_amortised_cost_Financial_liabilities_measured_at_amortised_cost_in_accordance_with_IFRS",
		"23":"IFRS_Financial_liabilities_held_for_trading_Financial_liabilities_held_for_trading_in_accordance_with_IFRS",
		"25":"IFRS_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		"31":"nGAAP_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_accordance_with_national_GAAP_based_on_BAD",
		"33":"nGAAP_Trading_financial_liabilities_Trading_financial_liabilities_in_accordance_with_national_GAAP_based_on_BAD",
		"35":"nGAAP_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_nationa_GAAP_based_on_BAD",
		"85":"nGAAP_Accounting_portfolios_for_trading_financial_instruments_Cost_based_method_or_LOCOM",
}

	ACCNTNG_CLSSFCTN = models.CharField("ACCNTNG_CLSSFCTN",max_length=255, choices=ACCNTNG_CLSSFCTN_LBLTS_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CLSSFCTN_LBLTS_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	ACCMLTD_CHNGS_FV = models.BigIntegerField("ACCMLTD_CHNGS_FV",default=None, blank=True, null=True)

	ACCMLTD_CHNGS_FV_CR = models.BigIntegerField("ACCMLTD_CHNGS_FV_CR",default=None, blank=True, null=True)

	RSDL_MTRTY_BND_domain = {		"12":"_3m_6m",
		"16":"_6m_12m",
		"21":"_1y_2y",
		"28":"_2y_3y",
		"3":"_1d_1w",
		"31":"_3y_5y",
		"36":"_5y_10y",
		"40":"Over_10_years",
		"64":"_0d_1d",
		"81":"_gt_7_days_lt_eq_14_days",
		"82":"_gt_2_weeks_lt_eq_1_month",
		"9":"_1m_3m",
		"999":"Open_maturity",
}

	ASST_ENCMBRNC_RSDL_MTRTY_BND = models.CharField("ASST_ENCMBRNC_RSDL_MTRTY_BND",max_length=255, choices=RSDL_MTRTY_BND_domain,default=None, blank=True, null=True, db_comment="RSDL_MTRTY_BND_domain")

	ASST_ENCMBRNC_SRC_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Asset_encumbrance_source",
		"2":"Not_an_asset_encumbrance_source",
}

	ASST_ENCMBRNC_SRC_INDCTR = models.CharField("ASST_ENCMBRNC_SRC_INDCTR",max_length=255, choices=ASST_ENCMBRNC_SRC_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="ASST_ENCMBRNC_SRC_INDCTR_INPT_domain")

	CRRYNG_AMNT = models.BigIntegerField("CRRYNG_AMNT",default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_PRDNTL_PRTFL_TYP_INPT_domain = {		"22":"Issued_debt_security_in_the_banking_book",
		"23":"Issued_debt_security_in_the_trading_book_International_Financial_Reporting_Standard_IFRS",
		"24":"Issued_debt_security_in_the_trading_book_national_general_accepted_accounting_principles_nGAAP",
}

	DBT_SCRTY_ISSD_PRDNTL_PRTFL_TYP = models.CharField("DBT_SCRTY_ISSD_PRDNTL_PRTFL_TYP",max_length=255, choices=DBT_SCRTY_ISSD_PRDNTL_PRTFL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="DBT_SCRTY_ISSD_PRDNTL_PRTFL_TYP_INPT_domain")

	FV = models.BigIntegerField("FV",default=None, blank=True, null=True)

	FV_CHNG = models.BigIntegerField("FV_CHNG",default=None, blank=True, null=True)

	FV_HRRCHY_INPT_domain = {		"0":"Not_applicable",
		"1":"Level_1_Level_1_inputs_used_for_the_measurement_of_fair_value_Level_1_inputs_are_quoted_prices_in_active_markets_for_identical_assets_or_liabilities_that_the_entity_can_access_at_the_measurement_date",
		"2":"Level_2_Level_2_inputs_used_for_the_measurment_of_fair_value_Level_2_inputs_are_inputs_other_than_quoted_prices_included_within_Level_1_that_are_observable_for_the_asset_or_liability_either_directly_or_indirectly",
		"3":"Level_3_Level_3_inputs_used_for_the_measurment_of_fair_value_Level_3_inputs_are_unobservable_inputs_for_the_asset_or_liability",
}

	FV_HRRCHY = models.CharField("FV_HRRCHY",max_length=255, choices=FV_HRRCHY_INPT_domain,default=None, blank=True, null=True, db_comment="FV_HRRCHY_INPT_domain")

	FVO_DSGNTN_INPT_domain = {		"0":"Not_applicable",
		"2":"Management_on_a_fair_value_basis",
		"5":"Management_of_credit_risk_Upon_designation",
		"6":"Management_of_credit_risk_After_the_designation",
}

	FVO_DSGNTN = models.CharField("FVO_DSGNTN",max_length=255, choices=FVO_DSGNTN_INPT_domain,default=None, blank=True, null=True, db_comment="FVO_DSGNTN_INPT_domain")

	HLD_SL_INDCTR_domain = {		"1":"Held_for_sale_The_member_indicates_that_the_instrument_is_held_for_sale",
		"2":"Not_held_for_sale_The_member_indicates_that_the_instrument_is_not_held_for_sale",
}

	HLD_SL_INDCTR = models.CharField("HLD_SL_INDCTR",max_length=255, choices=HLD_SL_INDCTR_domain,default=None, blank=True, null=True, db_comment="HLD_SL_INDCTR_domain")

	HRCTS_TRDNG_PSTNS_FV = models.BigIntegerField("HRCTS_TRDNG_PSTNS_FV",default=None, blank=True, null=True)

	NMNL_AMNT = models.BigIntegerField("NMNL_AMNT",default=None, blank=True, null=True)

	NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain = {		"1":"Non_performing_prior_to_forbearance",
		"2":"Not_non_performing_prior_to_forbearance",
}

	NN_PRFRMNG_PRR_FRBRNC_INDCTR = models.CharField("NN_PRFRMNG_PRR_FRBRNC_INDCTR",max_length=255, choices=NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain,default=None, blank=True, null=True, db_comment="NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain")

	PRSNT_VL = models.BigIntegerField("PRSNT_VL",default=None, blank=True, null=True)

	STRT_DT_PRD = models.DateTimeField("STRT_DT_PRD",default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_TYP_domain = {		"15":"Fair_valued_debt_security_issued",
		"16":"Non_fair_valued_debt_security_issued",
}

	TYP_DBT_SCRTY_ISSD = models.CharField("TYP_DBT_SCRTY_ISSD",max_length=255, choices=DBT_SCRTY_ISSD_TYP_domain,default=None, blank=True, null=True, db_comment="DBT_SCRTY_ISSD_TYP_domain")

	TYP_PRDCT_DBT_SCRTS_ISSD_domain = {		"610":"Certificates_of_deposits",
		"620":"Asset_backed_securities",
		"630":"Covered_bonds",
		"640":"Hybrid_contracts",
		"650":"Other_debt_securities_issued",
		"651":"Other_debt_securities_issued_convertible_compound_financial_instruments",
		"652":"Other_debt_securities_issued_non_convertible",
}

	TYP_PRDCT = models.CharField("TYP_PRDCT",max_length=255, choices=TYP_PRDCT_DBT_SCRTS_ISSD_domain,default=None, blank=True, null=True, db_comment="TYP_PRDCT_DBT_SCRTS_ISSD_domain")

	theSCRTY_EXCHNG_TRDBL_DRVTV = models.ForeignKey("SCRTY_EXCHNG_TRDBL_DRVTV", models.SET_NULL,blank=True,null=True,related_name="DBT_SCRTY_ISSD_to_theSCRTY_EXCHNG_TRDBL_DRVTVs")

	class Meta:

		verbose_name = 'DBT_SCRTY_ISSD'

		verbose_name_plural = 'DBT_SCRTY_ISSDs'

class DBT_SCRTY_ISSD_HDG(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_HDG_uniqueID = models.CharField("DBT_SCRTY_ISSD_HDG_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CLSSFCTN_LBLTS_domain = {		"21":"IFRS_Financial_liabilities_measured_at_amortised_cost_Financial_liabilities_measured_at_amortised_cost_in_accordance_with_IFRS",
		"23":"IFRS_Financial_liabilities_held_for_trading_Financial_liabilities_held_for_trading_in_accordance_with_IFRS",
		"25":"IFRS_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		"31":"nGAAP_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_accordance_with_national_GAAP_based_on_BAD",
		"33":"nGAAP_Trading_financial_liabilities_Trading_financial_liabilities_in_accordance_with_national_GAAP_based_on_BAD",
		"35":"nGAAP_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_nationa_GAAP_based_on_BAD",
		"85":"nGAAP_Accounting_portfolios_for_trading_financial_instruments_Cost_based_method_or_LOCOM",
}

	ACCNTNG_CLSSFCTN = models.CharField("ACCNTNG_CLSSFCTN",max_length=255, choices=ACCNTNG_CLSSFCTN_LBLTS_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CLSSFCTN_LBLTS_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	ACCNTNG_HDG_INDCTR_domain = {		"1":"Accounting_hedge",
}

	ACCNTNG_HDG_INDCTR = models.CharField("ACCNTNG_HDG_INDCTR",max_length=255, choices=ACCNTNG_HDG_INDCTR_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_HDG_INDCTR_domain")

	TYP_HDG_BIRD_domain = {		"1":"Fair_value_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_a",
		"11":"Hedges_other_than_cash_flow_hedge_and_hedge_of_net_investment_in_a_foreign_operation_Economic_hedge",
		"12":"Economic_hedge_With_use_of_fair_value_option",
		"13":"Economic_hedge_Other",
		"2":"Cash_flow_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_b",
		"3":"Hedge_of_a_net_investment_in_a_foreign_operation_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_c",
		"4":"Portfolio_fair_value_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"5":"Portfolio_cash_flow_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"6":"Cost_price_hedge_Hedging_relationship_as_defined_in_Reg_680_2014_Annex_V_part_2_114_This_hedging_relationship_is_applicable_only_under_nGAAP_based_on_BAD",
		"7":"Other_than_Fair_value_hedge_Cash_flow_hedge_Hedge_of_a_net_investment_in_a_foreign_operation_Portfolio_fair_value_hedges_of_interest_rate_risk_Portfolio_cash_flow_hedges_of_interest_rate_risk_Cost_price_hedge_Other_applicable_hedging_relationship_for_nGAAP_based_on_BAD_reporters",
}

	TYP_HDG = models.CharField("TYP_HDG",max_length=255, choices=TYP_HDG_BIRD_domain,default=None, blank=True, null=True, db_comment="TYP_HDG_BIRD_domain")

	theDBT_SCRTY_ISSD = models.ForeignKey("DBT_SCRTY_ISSD", models.SET_NULL,blank=True,null=True,related_name="DBT_SCRTY_ISSD_HDG_to_theDBT_SCRTY_ISSDs")

	class Meta:

		verbose_name = 'DBT_SCRTY_ISSD_HDG'

		verbose_name_plural = 'DBT_SCRTY_ISSD_HDGs'

class DBT_SCRTY_ISSD_PRTCN_ARRNGMNT_GVN_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_PRTCN_ARRNGMNT_GVN_ASSGNMNT_uniqueID = models.CharField("DBT_SCRTY_ISSD_PRTCN_ARRNGMNT_GVN_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CLSSFCTN_LBLTS_domain = {		"21":"IFRS_Financial_liabilities_measured_at_amortised_cost_Financial_liabilities_measured_at_amortised_cost_in_accordance_with_IFRS",
		"23":"IFRS_Financial_liabilities_held_for_trading_Financial_liabilities_held_for_trading_in_accordance_with_IFRS",
		"25":"IFRS_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		"31":"nGAAP_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_accordance_with_national_GAAP_based_on_BAD",
		"33":"nGAAP_Trading_financial_liabilities_Trading_financial_liabilities_in_accordance_with_national_GAAP_based_on_BAD",
		"35":"nGAAP_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_nationa_GAAP_based_on_BAD",
		"85":"nGAAP_Accounting_portfolios_for_trading_financial_instruments_Cost_based_method_or_LOCOM",
}

	ACCNTNG_CLSSFCTN = models.CharField("ACCNTNG_CLSSFCTN",max_length=255, choices=ACCNTNG_CLSSFCTN_LBLTS_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CLSSFCTN_LBLTS_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTCTN_ARRNGMNT_ID = models.CharField("PRTCTN_ARRNGMNT_ID",max_length=255,default=None, blank=True, null=True)

	PRTCTN_ARRNGMNT_RL_TYP_domain = {		"0":"Not_applicable",
		"1":"Protection_arrangement_received",
		"2":"Protection_arrangement_given",
}

	PRTCTN_ARRNGMNT_RL_TYP = models.CharField("PRTCTN_ARRNGMNT_RL_TYP",max_length=255, choices=PRTCTN_ARRNGMNT_RL_TYP_domain,default=None, blank=True, null=True, db_comment="PRTCTN_ARRNGMNT_RL_TYP_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	ALLCTD_UNSD_CLLTRL_VL = models.FloatField("ALLCTD_UNSD_CLLTRL_VL",default=None, blank=True, null=True)

	PRTCTN_ALLCTD_VL = models.BigIntegerField("PRTCTN_ALLCTD_VL",default=None, blank=True, null=True)

	theDBT_SCRTY_ISSD = models.ForeignKey("DBT_SCRTY_ISSD", models.SET_NULL,blank=True,null=True,related_name="DBT_SCRTY_ISSD_PRTCN_ARRNGMNT_GVN_ASSGNMNT_to_theDBT_SCRTY_ISSDs")

	thePRTCTN_ARRNGMNT_RL = models.ForeignKey("PRTCTN_ARRNGMNT_RL", models.SET_NULL,blank=True,null=True,related_name="DBT_SCRTY_ISSD_PRTCN_ARRNGMNT_GVN_ASSGNMNT_to_thePRTCTN_ARRNGMNT_RLs")

	class Meta:

		verbose_name = 'DBT_SCRTY_ISSD_PRTCN_ARRNGMNT_GVN_ASSGNMNT'

		verbose_name_plural = 'DBT_SCRTY_ISSD_PRTCN_ARRNGMNT_GVN_ASSGNMNTs'

class DBT_SCRTY_ISSD_TRDTNL_SCRTSTN_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_TRDTNL_SCRTSTN_ASSGNMNT_uniqueID = models.CharField("DBT_SCRTY_ISSD_TRDTNL_SCRTSTN_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CLSSFCTN_LBLTS_domain = {		"21":"IFRS_Financial_liabilities_measured_at_amortised_cost_Financial_liabilities_measured_at_amortised_cost_in_accordance_with_IFRS",
		"23":"IFRS_Financial_liabilities_held_for_trading_Financial_liabilities_held_for_trading_in_accordance_with_IFRS",
		"25":"IFRS_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		"31":"nGAAP_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_accordance_with_national_GAAP_based_on_BAD",
		"33":"nGAAP_Trading_financial_liabilities_Trading_financial_liabilities_in_accordance_with_national_GAAP_based_on_BAD",
		"35":"nGAAP_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_nationa_GAAP_based_on_BAD",
		"85":"nGAAP_Accounting_portfolios_for_trading_financial_instruments_Cost_based_method_or_LOCOM",
}

	ACCNTNG_CLSSFCTN = models.CharField("ACCNTNG_CLSSFCTN",max_length=255, choices=ACCNTNG_CLSSFCTN_LBLTS_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CLSSFCTN_LBLTS_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSTN_ID = models.CharField("SCRTSTN_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	theDBT_SCRTY_ISSD = models.ForeignKey("DBT_SCRTY_ISSD", models.SET_NULL,blank=True,null=True,related_name="DBT_SCRTY_ISSD_TRDTNL_SCRTSTN_ASSGNMNT_to_theDBT_SCRTY_ISSDs")

	theTRDTNL_SCRTSTN = models.ForeignKey("TRDTNL_SCRTSTN", models.SET_NULL,blank=True,null=True,related_name="DBT_SCRTY_ISSD_TRDTNL_SCRTSTN_ASSGNMNT_to_theTRDTNL_SCRTSTNs")

	class Meta:

		verbose_name = 'DBT_SCRTY_ISSD_TRDTNL_SCRTSTN_ASSGNMNT'

		verbose_name_plural = 'DBT_SCRTY_ISSD_TRDTNL_SCRTSTN_ASSGNMNTs'

class ENTTY_RL(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	ENTTY_RL_uniqueID = models.CharField("ENTTY_RL_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	PRTY_RL_TYP = models.CharField("PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ENTTY_GRP_RL_TYP_domain = {		"29":"Central_bank_and_private_sector_company_role",
		"40":"Natural_person_group_role",
}

	ENTTY_GRP_RL_TYP = models.CharField("ENTTY_GRP_RL_TYP",max_length=255, choices=ENTTY_GRP_RL_TYP_domain,default=None, blank=True, null=True, db_comment="ENTTY_GRP_RL_TYP_domain")

	ENTTY_RL_TYP_domain = {		"37":"Entity_group_role",
		"38":"Entity_transaction_role",
}

	ENTTY_RL_TYP = models.CharField("ENTTY_RL_TYP",max_length=255, choices=ENTTY_RL_TYP_domain,default=None, blank=True, null=True, db_comment="ENTTY_RL_TYP_domain")

	ENTTY_TRNSCTN_RL_TYP_domain = {		"1":"Legal_person_role",
		"2":"Organisation_role",
		"3":"Party_role",
}

	ENTTY_TRNSCTN_RL_TYP = models.CharField("ENTTY_TRNSCTN_RL_TYP",max_length=255, choices=ENTTY_TRNSCTN_RL_TYP_domain,default=None, blank=True, null=True, db_comment="ENTTY_TRNSCTN_RL_TYP_domain")

	EQTY = models.BigIntegerField("EQTY",default=None, blank=True, null=True)

	PRFT_LSS = models.BigIntegerField("PRFT_LSS",default=None, blank=True, null=True)

	SHR_CPTL = models.BigIntegerField("SHR_CPTL",default=None, blank=True, null=True)

	TTL_ASSTS = models.BigIntegerField("TTL_ASSTS",default=None, blank=True, null=True)

	thePRTY = models.ForeignKey("PRTY", models.SET_NULL,blank=True,null=True,related_name="ENTTY_RL_to_thePRTYs")

	class Meta:

		verbose_name = 'ENTTY_RL'

		verbose_name_plural = 'ENTTY_RLs'

class EQT_INSTRMNT_NT_SCRT_HDG(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	EQT_INSTRMNT_NT_SCRT_HDG_uniqueID = models.CharField("EQT_INSTRMNT_NT_SCRT_HDG_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ACCNTNG_HDG_INDCTR_domain = {		"1":"Accounting_hedge",
}

	ACCNTNG_HDG_INDCTR = models.CharField("ACCNTNG_HDG_INDCTR",max_length=255, choices=ACCNTNG_HDG_INDCTR_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_HDG_INDCTR_domain")

	TYP_HDG_BIRD_domain = {		"1":"Fair_value_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_a",
		"11":"Hedges_other_than_cash_flow_hedge_and_hedge_of_net_investment_in_a_foreign_operation_Economic_hedge",
		"12":"Economic_hedge_With_use_of_fair_value_option",
		"13":"Economic_hedge_Other",
		"2":"Cash_flow_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_b",
		"3":"Hedge_of_a_net_investment_in_a_foreign_operation_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_c",
		"4":"Portfolio_fair_value_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"5":"Portfolio_cash_flow_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"6":"Cost_price_hedge_Hedging_relationship_as_defined_in_Reg_680_2014_Annex_V_part_2_114_This_hedging_relationship_is_applicable_only_under_nGAAP_based_on_BAD",
		"7":"Other_than_Fair_value_hedge_Cash_flow_hedge_Hedge_of_a_net_investment_in_a_foreign_operation_Portfolio_fair_value_hedges_of_interest_rate_risk_Portfolio_cash_flow_hedges_of_interest_rate_risk_Cost_price_hedge_Other_applicable_hedging_relationship_for_nGAAP_based_on_BAD_reporters",
}

	TYP_HDG = models.CharField("TYP_HDG",max_length=255, choices=TYP_HDG_BIRD_domain,default=None, blank=True, null=True, db_comment="TYP_HDG_BIRD_domain")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="EQT_INSTRMNT_NT_SCRT_HDG_to_theINSTRMNTs")

	class Meta:

		verbose_name = 'EQT_INSTRMNT_NT_SCRT_HDG'

		verbose_name_plural = 'EQT_INSTRMNT_NT_SCRT_HDGs'

class ETD_LBLTY_PSTN_SNTHTC_SCRTSTN_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	ETD_LBLTY_PSTN_SNTHTC_SCRTSTN_ASSGNMNT_uniqueID = models.CharField("ETD_LBLTY_PSTN_SNTHTC_SCRTSTN_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	BYR_PRTY_ID = models.CharField("BYR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	BYR_PRTY_RL_TYP = models.CharField("BYR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	EXCHNG_TRDBL_DRVT_SCRTY_ID = models.CharField("EXCHNG_TRDBL_DRVT_SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSTN_ID = models.CharField("SCRTSTN_ID",max_length=255,default=None, blank=True, null=True)

	SLLR_PRTY_ID = models.CharField("SLLR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	SLLR_PRTY_RL_TYP = models.CharField("SLLR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	EXCHNG_TRDBL_DRVTV_PSTN_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"10":"Non_fair_valued_balance_sheet_recognised_exchange_tradable_derivative_asset_position",
		"12":"Non_balance_sheet_recognised_exchange_tradable_derivative_asset_position",
		"41":"Exchange_tradable_derivative_position_as_a_hedge_according_to_International_Financial_Reporting_Standard_IFRS",
		"42":"Exchange_tradable_derivative_position_as_a_hedge_according_to_national_general_accepted_accounting_principles_nGAAP",
		"6":"Non_balance_sheet_recognised_exchange_tradable_derivative_liability_position",
		"7":"Fair_valued_balance_sheet_recognised_exchange_tradable_derivative_liability_position",
		"8":"Non_fair_valued_balance_sheet_recognised_exchange_tradable_derivative_liability_position",
		"9":"Fair_valued_balance_sheet_recognised_exchange_tradable_derivative_asset_position",
}

	TYP_EXCHNG_TRDBL_DRVTV_PSTN_RL = models.CharField("TYP_EXCHNG_TRDBL_DRVTV_PSTN_RL",max_length=255, choices=EXCHNG_TRDBL_DRVTV_PSTN_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="EXCHNG_TRDBL_DRVTV_PSTN_RL_TYP_INPT_domain")

	theEXCHNG_TRDBL_DRVTV_PSTN_RL = models.ForeignKey("EXCHNG_TRDBL_DRVTV_PSTN_RL", models.SET_NULL,blank=True,null=True,related_name="ETD_LBLTY_PSTN_SNTHTC_SCRTSTN_ASSGNMNT_to_theEXCHNG_TRDBL_DRVTV_PSTN_RLs")

	theSNTHTC_SCRTSTN = models.ForeignKey("SNTHTC_SCRTSTN", models.SET_NULL,blank=True,null=True,related_name="ETD_LBLTY_PSTN_SNTHTC_SCRTSTN_ASSGNMNT_to_theSNTHTC_SCRTSTNs")

	class Meta:

		verbose_name = 'ETD_LBLTY_PSTN_SNTHTC_SCRTSTN_ASSGNMNT'

		verbose_name_plural = 'ETD_LBLTY_PSTN_SNTHTC_SCRTSTN_ASSGNMNTs'

class EXCHNG_TRDBL_DRVTV_PSTN(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	EXCHNG_TRDBL_DRVTV_PSTN_uniqueID = models.CharField("EXCHNG_TRDBL_DRVTV_PSTN_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	BYR_PRTY_ID = models.CharField("BYR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	BYR_PRTY_RL_TYP = models.CharField("BYR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	EXCHNG_TRDBL_DRVT_SCRTY_ID = models.CharField("EXCHNG_TRDBL_DRVT_SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SLLR_PRTY_ID = models.CharField("SLLR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	SLLR_PRTY_RL_TYP = models.CharField("SLLR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	HLD_SL_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Held_for_sale_The_member_indicates_that_the_instrument_is_held_for_sale",
		"2":"Not_held_for_sale_The_member_indicates_that_the_instrument_is_not_held_for_sale",
}

	HLD_SL_INDCTR = models.CharField("HLD_SL_INDCTR",max_length=255, choices=HLD_SL_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="HLD_SL_INDCTR_INPT_domain")

	NTNL_AMNT = models.BigIntegerField("NTNL_AMNT",default=None, blank=True, null=True)

	SCRTY_EXCHNG_TRDBL_DRVTV_PSTN_TYP = models.CharField("SCRTY_EXCHNG_TRDBL_DRVTV_PSTN_TYP",max_length=255,default=None, blank=True, null=True)

	TYP_RSK_INPT_domain = {		"0":"Not_Applicable",
		"1":"Interest_rate_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_a",
		"2":"Equity_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_b",
		"3":"Foreign_exchange_and_gold_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_c",
		"4":"Credit_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_d",
		"5":"Commodities_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_e",
		"6":"Risk_other_than_Interest_rate_risk_Equity_risk_Foreign_exchange_and_gold_risk_Credit_risk_Commodities_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_f",
}

	TYP_RSK = models.CharField("TYP_RSK",max_length=255, choices=TYP_RSK_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_RSK_INPT_domain")

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="EXCHNG_TRDBL_DRVTV_PSTN_to_theENTTY_RLs")

	theENTTY_RL1 = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="EXCHNG_TRDBL_DRVTV_PSTN_to_theENTTY_RL1s")

	theSCRTY_EXCHNG_TRDBL_DRVTV = models.ForeignKey("SCRTY_EXCHNG_TRDBL_DRVTV", models.SET_NULL,blank=True,null=True,related_name="EXCHNG_TRDBL_DRVTV_PSTN_to_theSCRTY_EXCHNG_TRDBL_DRVTVs")

	class Meta:

		verbose_name = 'EXCHNG_TRDBL_DRVTV_PSTN'

		verbose_name_plural = 'EXCHNG_TRDBL_DRVTV_PSTNs'

class EXCHNG_TRDBL_DRVTV_PSTN_PRTCN_ARRNGMNT_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	EXCHNG_TRDBL_DRVTV_PSTN_PRTCN_ARRNGMNT_ASSGNMNT_uniqueID = models.CharField("EXCHNG_TRDBL_DRVTV_PSTN_PRTCN_ARRNGMNT_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	BYR_PRTY_ID = models.CharField("BYR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	BYR_PRTY_RL_TYP = models.CharField("BYR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	EXCHNG_TRDBL_DRVTV_SCRTY_ID = models.CharField("EXCHNG_TRDBL_DRVTV_SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	PRTCTN_ARRNGMNT_RL_TYP_domain = {		"0":"Not_applicable",
		"1":"Protection_arrangement_received",
		"2":"Protection_arrangement_given",
}

	PRTCTN_ARRNGMNT_RL_TYP = models.CharField("PRTCTN_ARRNGMNT_RL_TYP",max_length=255, choices=PRTCTN_ARRNGMNT_RL_TYP_domain,default=None, blank=True, null=True, db_comment="PRTCTN_ARRNGMNT_RL_TYP_domain")

	PRTCTN_ID = models.CharField("PRTCTN_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SLLR_PRTY_ID = models.CharField("SLLR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	SLLR_PRTY_RL_TYP = models.CharField("SLLR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	ALLCTD_UNSD_CLLTRL_VL = models.FloatField("ALLCTD_UNSD_CLLTRL_VL",default=None, blank=True, null=True)

	EXCHNG_TRDBL_DRVTV_PRTCN_ARRNGMNT_ASSGNMNT_TYP_domain = {		"1":"Exchange_tradable_derivative_position_Protection_arrangement_received_assignment",
		"2":"Protection_arrangement_given_Exchange_tradable_derivative_position_assignment",
}

	EXCHNG_TRDBL_DRVTV_PRTCN_ARRNGMNT_ASSGNMNT_TYP = models.CharField("EXCHNG_TRDBL_DRVTV_PRTCN_ARRNGMNT_ASSGNMNT_TYP",max_length=255, choices=EXCHNG_TRDBL_DRVTV_PRTCN_ARRNGMNT_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="EXCHNG_TRDBL_DRVTV_PRTCN_ARRNGMNT_ASSGNMNT_TYP_domain")

	PRTCTN_ALLCTD_VL = models.BigIntegerField("PRTCTN_ALLCTD_VL",default=None, blank=True, null=True)

	theEXCHNG_TRDBL_DRVTV_PSTN = models.ForeignKey("EXCHNG_TRDBL_DRVTV_PSTN", models.SET_NULL,blank=True,null=True,related_name="EXCHNG_TRDBL_DRVTV_PSTN_PRTCN_ARRNGMNT_ASSGNMNT_to_theEXCHNG_TRDBL_DRVTV_PSTNs")

	thePRTCTN_ARRNGMNT_RL = models.ForeignKey("PRTCTN_ARRNGMNT_RL", models.SET_NULL,blank=True,null=True,related_name="EXCHNG_TRDBL_DRVTV_PSTN_PRTCN_ARRNGMNT_ASSGNMNT_to_thePRTCTN_ARRNGMNT_RLs")

	class Meta:

		verbose_name = 'EXCHNG_TRDBL_DRVTV_PSTN_PRTCN_ARRNGMNT_ASSGNMNT'

		verbose_name_plural = 'EXCHNG_TRDBL_DRVTV_PSTN_PRTCN_ARRNGMNT_ASSGNMNTs'

class EXCHNG_TRDBL_DRVTV_PSTN_RL(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	EXCHNG_TRDBL_DRVTV_PSTN_RL_uniqueID = models.CharField("EXCHNG_TRDBL_DRVTV_PSTN_RL_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	BYR_PRTY_ID = models.CharField("BYR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	BYR_PRTY_RL_TYP = models.CharField("BYR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	EXCHNG_TRDBL_DRVTV_SCRTY_ID = models.CharField("EXCHNG_TRDBL_DRVTV_SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SLLR_PRTY_ID = models.CharField("SLLR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	SLLR_PRTY_RL_TYP = models.CharField("SLLR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	EXCHNG_TRDBL_DRVTV_PSTN_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"10":"Non_fair_valued_balance_sheet_recognised_exchange_tradable_derivative_asset_position",
		"12":"Non_balance_sheet_recognised_exchange_tradable_derivative_asset_position",
		"41":"Exchange_tradable_derivative_position_as_a_hedge_according_to_International_Financial_Reporting_Standard_IFRS",
		"42":"Exchange_tradable_derivative_position_as_a_hedge_according_to_national_general_accepted_accounting_principles_nGAAP",
		"6":"Non_balance_sheet_recognised_exchange_tradable_derivative_liability_position",
		"7":"Fair_valued_balance_sheet_recognised_exchange_tradable_derivative_liability_position",
		"8":"Non_fair_valued_balance_sheet_recognised_exchange_tradable_derivative_liability_position",
		"9":"Fair_valued_balance_sheet_recognised_exchange_tradable_derivative_asset_position",
}

	TYP_EXCHNG_TRDBL_DRVTV_PSTN_RL = models.CharField("TYP_EXCHNG_TRDBL_DRVTV_PSTN_RL",max_length=255, choices=EXCHNG_TRDBL_DRVTV_PSTN_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="EXCHNG_TRDBL_DRVTV_PSTN_RL_TYP_INPT_domain")

	ACCMLTD_CHNGS_FV = models.BigIntegerField("ACCMLTD_CHNGS_FV",default=None, blank=True, null=True)

	ACCNTNG_CLSSFCTN_ETD_INPT_domain = {		"0":"Not_applicable",
		"14":"IFRS_Cash_balances_at_central_banks_and_other_demand_deposits_Cash_balances_at_central_banks_and_other_demand_deposits_in_accordance_with_IFRS",
		"2":"IFRS_Financial_assets_held_for_trading_Financial_assets_held_for_trading_in_accordance_with_IFRS",
		"21":"IFRS_Financial_liabilities_measured_at_amortised_cost_Financial_liabilities_measured_at_amortised_cost_in_accordance_with_IFRS",
		"23":"IFRS_Financial_liabilities_held_for_trading_Financial_liabilities_held_for_trading_in_accordance_with_IFRS",
		"25":"IFRS_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		"3":"nGAAP_Trading_Financial_assets_Trading_financial_assets_in_accordance_with_national_GAAP",
		"31":"nGAAP_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_accordance_with_national_GAAP_based_on_BAD",
		"33":"nGAAP_Trading_financial_liabilities_Trading_financial_liabilities_in_accordance_with_national_GAAP_based_on_BAD",
		"35":"nGAAP_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_nationa_GAAP_based_on_BAD",
		"4":"IFRS_Financial_assets_designated_at_fair_value_through_profit_or_loss_Financial_assets_measured_at_fair_value_through_profit_and_loss_and_designated_as_such_upon_initial_recognition_or_subsequently_in_accordance_with_IFRS_except_those_classified_as_financial_assets_held_for_trading",
		"41":"IFRS_Non_trading_financial_assets_mandatorily_at_fair_value_through_profit_or_loss_Non_trading_financial_assets_mandatorily_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		"45":"nGAAP_Cash_balances_at_central_banks_and_other_demand_deposits_Cash_balances_at_central_banks_and_other_demand_deposits_in_accordance_with_national_GAAP",
		"47":"nGAAP_Financial_assets_designated_at_fair_value_through_profit_or_loss_Financial_assets_designated_at_fair_value_through_profit_or_loss_in_accordance_with_national_GAAP",
		"6":"IFRS_Financial_assets_at_amortised_cost_Financial_assets_measured_at_amortised_cost_in_accordance_with_IFRS",
		"64":"nGAAP_financial_assets_at_fair_value_or_strict_LOCOM",
		"7":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_fair_value_through_profit_or_loss_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_in_accordance_with_national_GAAP",
		"711":"Accounting_portfolios_for_financial_assets_other_than_classified_as_held_for_sale_excluding_financial_assets_held_for_trading_trading_financial_assets_and_cash_and_cash_balances_at_central_banks_and_other_demand_deposits",
		"73":"nGAAP_Other_non_trading_non_derivative_financial_assets_LOCOM_nGAAP_Other_non_trading_non_derivative_financial_assets_at_LOCOM",
		"74":"nGAAP_Other_non_trading_non_derivative_financial_assets_Other_than_LOCOM",
		"76":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_LOCOM_nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_at_LOCOM",
		"77":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_Other_than_LOCOM",
		"8":"IFRS_Financial_assets_at_fair_value_through_other_comprehensive_income_Financial_assets_measured_at_fair_value_through_other_comprehensive_income_due_to_business_model_and_cash_flows_characteristics_in_accordance_with_IFRS",
		"83":"Investments_in_subsidiaries_joint_ventures_and_associates",
		"85":"nGAAP_Accounting_portfolios_for_trading_financial_instruments_Cost_based_method_or_LOCOM",
		"9":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_in_accordance_with_national_GAAP",
}

	ACCNTNG_CLSSFCTN = models.CharField("ACCNTNG_CLSSFCTN",max_length=255, choices=ACCNTNG_CLSSFCTN_ETD_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CLSSFCTN_ETD_INPT_domain")

	ASST_ENCMBRNC_SRC_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Asset_encumbrance_source",
		"2":"Not_an_asset_encumbrance_source",
}

	ASST_ENCMBRNC_SRC_INDCTR = models.CharField("ASST_ENCMBRNC_SRC_INDCTR",max_length=255, choices=ASST_ENCMBRNC_SRC_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="ASST_ENCMBRNC_SRC_INDCTR_INPT_domain")

	BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN_BY_ACCNTNG_STNDRD = models.BooleanField("BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN_BY_ACCNTNG_STNDRD",default=None, blank=True, null=True)

	CRRYNG_AMNT = models.BigIntegerField("CRRYNG_AMNT",default=None, blank=True, null=True)

	CST_BSD_MTHD_LCM_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"At_cost_based_method_or_Lower_of_cost_or_market_LOCOM",
		"2":"Not_at_cost_based_method_or_Lower_of_cost_or_market_LOCOM",
}

	CST_BSD_MTHD_LCM_INDCTR = models.CharField("CST_BSD_MTHD_LCM_INDCTR",max_length=255, choices=CST_BSD_MTHD_LCM_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="CST_BSD_MTHD_LCM_INDCTR_INPT_domain")

	ENCMBRD_ASST_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Not_encumbered_asset",
		"100":"Encumbered_asset",
}

	ENCMBRD_ASST_INDCTR = models.CharField("ENCMBRD_ASST_INDCTR",max_length=255, choices=ENCMBRD_ASST_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="ENCMBRD_ASST_INDCTR_INPT_domain")

	FDCRY_INSTRMNT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Fiduciary_asset",
		"2":"Non_fiduciary_asset",
}

	FDCRY = models.CharField("FDCRY",max_length=255, choices=FDCRY_INSTRMNT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="FDCRY_INSTRMNT_INDCTR_INPT_domain")

	FV = models.BigIntegerField("FV",default=None, blank=True, null=True)

	FV_CHNG = models.BigIntegerField("FV_CHNG",default=None, blank=True, null=True)

	FV_HRRCHY_INPT_domain = {		"0":"Not_applicable",
		"1":"Level_1_Level_1_inputs_used_for_the_measurement_of_fair_value_Level_1_inputs_are_quoted_prices_in_active_markets_for_identical_assets_or_liabilities_that_the_entity_can_access_at_the_measurement_date",
		"2":"Level_2_Level_2_inputs_used_for_the_measurment_of_fair_value_Level_2_inputs_are_inputs_other_than_quoted_prices_included_within_Level_1_that_are_observable_for_the_asset_or_liability_either_directly_or_indirectly",
		"3":"Level_3_Level_3_inputs_used_for_the_measurment_of_fair_value_Level_3_inputs_are_unobservable_inputs_for_the_asset_or_liability",
}

	FV_HRRCHY = models.CharField("FV_HRRCHY",max_length=255, choices=FV_HRRCHY_INPT_domain,default=None, blank=True, null=True, db_comment="FV_HRRCHY_INPT_domain")

	GRSS_CRRYNG_AMNT = models.BigIntegerField("GRSS_CRRYNG_AMNT",default=None, blank=True, null=True)

	PRDNTL_PRTFL_domain = {		"1":"Trading_book",
		"2":"Non_trading_book",
}

	PRDNTL_PRTFL_TYP = models.CharField("PRDNTL_PRTFL_TYP",max_length=255, choices=PRDNTL_PRTFL_domain,default=None, blank=True, null=True, db_comment="PRDNTL_PRTFL_domain")

	TYP_HDG_INPT_domain = {		"0":"Not_applicable",
		"1":"Fair_value_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_a",
		"11":"Hedges_other_than_cash_flow_hedge_and_hedge_of_net_investment_in_a_foreign_operation_Economic_hedge",
		"12":"Economic_hedge_With_use_of_fair_value_option",
		"13":"Economic_hedge_Other",
		"2":"Cash_flow_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_b",
		"3":"Hedge_of_a_net_investment_in_a_foreign_operation_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_c",
		"4":"Portfolio_fair_value_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"5":"Portfolio_cash_flow_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"6":"Cost_price_hedge_Hedging_relationship_as_defined_in_Reg_680_2014_Annex_V_part_2_114_This_hedging_relationship_is_applicable_only_under_nGAAP_based_on_BAD",
		"7":"Other_than_Fair_value_hedge_Cash_flow_hedge_Hedge_of_a_net_investment_in_a_foreign_operation_Portfolio_fair_value_hedges_of_interest_rate_risk_Portfolio_cash_flow_hedges_of_interest_rate_risk_Cost_price_hedge_Other_applicable_hedging_relationship_for_nGAAP_based_on_BAD_reporters",
}

	TYP_HDG = models.CharField("TYP_HDG",max_length=255, choices=TYP_HDG_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_HDG_INPT_domain")

	theEXCHNG_TRDBL_DRVTV_PSTN = models.ForeignKey("EXCHNG_TRDBL_DRVTV_PSTN", models.SET_NULL,blank=True,null=True,related_name="EXCHNG_TRDBL_DRVTV_PSTN_RL_to_theEXCHNG_TRDBL_DRVTV_PSTNs")

	class Meta:

		verbose_name = 'EXCHNG_TRDBL_DRVTV_PSTN_RL'

		verbose_name_plural = 'EXCHNG_TRDBL_DRVTV_PSTN_RLs'

class FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ETD_PSTNS(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ETD_PSTNS_uniqueID = models.CharField("FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ETD_PSTNS_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ID = models.CharField("FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ISO4217_INPT_domain = {		"0":"Not_applicable",
		"AED":"UAE_Dirham",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"ARS":"Argentine_Peso",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYN":"Belarussian_Ruble",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHE":"WIR_Euro",
		"CHF":"Swiss_franc",
		"CHW":"WIR_Franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CZK":"Czech_koruna",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GTQ":"Quetzal",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"ILS":"New_Israeli_Sheqel",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MRU":"Ouguiya_x2",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDG":"Sudanese_Pound",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SRD":"Surinam_Dollar",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"STN":"Dobra_x2",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJS":"Somoni",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"USN":"US_Dollar_Next_day",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UYW":"Unidad_Previsional",
		"UZS":"Uzbekistan_Sum",
		"VEF":"Bolivar",
		"VES":"Bolivar_Soberano",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XAG":"Silver_one_Troy_ounce",
		"XAU":"Gold_one_Troy_ounce",
		"XBA":"Bond_Markets_Unit_European_Composite_Unit_EURCO",
		"XBB":"Bond_Markets_Unit_European_Monetary_Unit_E_M_U_6",
		"XBC":"Bond_Markets_Unit_European_Unit_of_Account_9_E_U_A_9",
		"XBD":"Bond_Markets_Unit_European_Unit_of_Account_17_E_U_A_17",
		"XCD":"East_Caribbean_Dollar",
		"XDR":"Special_Drawing_Rights_SDR",
		"XOF":"CFA_Franc_BCEAO",
		"XPD":"Palladium_one_Troy_ounce",
		"XPF":"CFP_Franc",
		"XPT":"Platinum_one_Troy_ounce",
		"XSU":"Sucre",
		"XTS":"Codes_specifically_reserved_for_testing_purposes",
		"XUA":"ADB_Unit_of_Account",
		"XXX":"Code_assigned_for_transactions_where_no_currency_is_involved",
		"YER":"Yemeni_Rial",
		"ZAR":"South_African_Rand",
		"ZMW":"Zambian_Kwacha",
		"ZWL":"Zimbabwe_Dollar",
}

	CRRNCY_RCRD = models.CharField("CRRNCY_RCRD",max_length=255, choices=ISO4217_INPT_domain,default=None, blank=True, null=True, db_comment="ISO4217_INPT_domain")

	CRVTR_RSK_WGHT = models.FloatField("CRVTR_RSK_WGHT",default=None, blank=True, null=True)

	CRVTR_VLTN_DFFRNC = models.FloatField("CRVTR_VLTN_DFFRNC",default=None, blank=True, null=True)

	DLT_SNSTVTY = models.FloatField("DLT_SNSTVTY",default=None, blank=True, null=True)

	OPTN_MTRTY = models.FloatField("OPTN_MTRTY",default=None, blank=True, null=True)

	FRTB_RSK_MSR_TYP_domain = {		"4":"Delta_sensitivity",
		"5":"Vega_sensitivity",
		"6":"Curvature",
}

	RSK_MSR_TYP = models.CharField("RSK_MSR_TYP",max_length=255, choices=FRTB_RSK_MSR_TYP_domain,default=None, blank=True, null=True, db_comment="FRTB_RSK_MSR_TYP_domain")

	RSK_MSR_TYP_PSTN_domain = {		"1":"Fundamental_review_of_the_trading_book_standard_approach_risk_measure_for_OTC_positions",
		"2":"Fundamental_review_of_the_trading_book_standard_approach_risk_measure_for_ETD_positions",
		"3":"Fundamental_review_of_the_trading_book_standard_approach_risk_measure_for_security_positions",
}

	RSK_MSR_TYP_PSTN = models.CharField("RSK_MSR_TYP_PSTN",max_length=255, choices=RSK_MSR_TYP_PSTN_domain,default=None, blank=True, null=True, db_comment="RSK_MSR_TYP_PSTN_domain")

	SHCK_DRCTN_domain = {		"0":"Not_applicable",
		"1":"Up",
		"2":"Down",
}

	SHCK_DRCTN = models.CharField("SHCK_DRCTN",max_length=255, choices=SHCK_DRCTN_domain,default=None, blank=True, null=True, db_comment="SHCK_DRCTN_domain")

	TNR = models.FloatField("TNR",default=None, blank=True, null=True)

	UNDRLYNG_RSDL_MTRTY = models.FloatField("UNDRLYNG_RSDL_MTRTY",default=None, blank=True, null=True)

	VG_SNSTVTY = models.FloatField("VG_SNSTVTY",default=None, blank=True, null=True)

	theEXCHNG_TRDBL_DRVTV_PSTN = models.ForeignKey("EXCHNG_TRDBL_DRVTV_PSTN", models.SET_NULL,blank=True,null=True,related_name="FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ETD_PSTNS_to_theEXCHNG_TRDBL_DRVTV_PSTNs")

	theRSK_FAC_SA = models.ForeignKey("RSK_FAC_SA", models.SET_NULL,blank=True,null=True,related_name="FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ETD_PSTNS_to_theRSK_FAC_SAs")

	class Meta:

		verbose_name = 'FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ETD_PSTNS'

		verbose_name_plural = 'FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ETD_PSTNSs'

class FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_FR_SCRTY_PSTNS(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_FR_SCRTY_PSTNS_uniqueID = models.CharField("FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_FR_SCRTY_PSTNS_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ID = models.CharField("FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ISO4217_INPT_domain = {		"0":"Not_applicable",
		"AED":"UAE_Dirham",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"ARS":"Argentine_Peso",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYN":"Belarussian_Ruble",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHE":"WIR_Euro",
		"CHF":"Swiss_franc",
		"CHW":"WIR_Franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CZK":"Czech_koruna",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GTQ":"Quetzal",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"ILS":"New_Israeli_Sheqel",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MRU":"Ouguiya_x2",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDG":"Sudanese_Pound",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SRD":"Surinam_Dollar",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"STN":"Dobra_x2",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJS":"Somoni",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"USN":"US_Dollar_Next_day",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UYW":"Unidad_Previsional",
		"UZS":"Uzbekistan_Sum",
		"VEF":"Bolivar",
		"VES":"Bolivar_Soberano",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XAG":"Silver_one_Troy_ounce",
		"XAU":"Gold_one_Troy_ounce",
		"XBA":"Bond_Markets_Unit_European_Composite_Unit_EURCO",
		"XBB":"Bond_Markets_Unit_European_Monetary_Unit_E_M_U_6",
		"XBC":"Bond_Markets_Unit_European_Unit_of_Account_9_E_U_A_9",
		"XBD":"Bond_Markets_Unit_European_Unit_of_Account_17_E_U_A_17",
		"XCD":"East_Caribbean_Dollar",
		"XDR":"Special_Drawing_Rights_SDR",
		"XOF":"CFA_Franc_BCEAO",
		"XPD":"Palladium_one_Troy_ounce",
		"XPF":"CFP_Franc",
		"XPT":"Platinum_one_Troy_ounce",
		"XSU":"Sucre",
		"XTS":"Codes_specifically_reserved_for_testing_purposes",
		"XUA":"ADB_Unit_of_Account",
		"XXX":"Code_assigned_for_transactions_where_no_currency_is_involved",
		"YER":"Yemeni_Rial",
		"ZAR":"South_African_Rand",
		"ZMW":"Zambian_Kwacha",
		"ZWL":"Zimbabwe_Dollar",
}

	CRRNCY_RCRD = models.CharField("CRRNCY_RCRD",max_length=255, choices=ISO4217_INPT_domain,default=None, blank=True, null=True, db_comment="ISO4217_INPT_domain")

	CRVTR_RSK_WGHT = models.FloatField("CRVTR_RSK_WGHT",default=None, blank=True, null=True)

	CRVTR_VLTN_DFFRNC = models.FloatField("CRVTR_VLTN_DFFRNC",default=None, blank=True, null=True)

	DLT_SNSTVTY = models.FloatField("DLT_SNSTVTY",default=None, blank=True, null=True)

	OPTN_MTRTY = models.FloatField("OPTN_MTRTY",default=None, blank=True, null=True)

	FRTB_RSK_MSR_TYP_domain = {		"4":"Delta_sensitivity",
		"5":"Vega_sensitivity",
		"6":"Curvature",
}

	RSK_MSR_TYP = models.CharField("RSK_MSR_TYP",max_length=255, choices=FRTB_RSK_MSR_TYP_domain,default=None, blank=True, null=True, db_comment="FRTB_RSK_MSR_TYP_domain")

	RSK_MSR_TYP_PSTN_domain = {		"1":"Fundamental_review_of_the_trading_book_standard_approach_risk_measure_for_OTC_positions",
		"2":"Fundamental_review_of_the_trading_book_standard_approach_risk_measure_for_ETD_positions",
		"3":"Fundamental_review_of_the_trading_book_standard_approach_risk_measure_for_security_positions",
}

	RSK_MSR_TYP_PSTN = models.CharField("RSK_MSR_TYP_PSTN",max_length=255, choices=RSK_MSR_TYP_PSTN_domain,default=None, blank=True, null=True, db_comment="RSK_MSR_TYP_PSTN_domain")

	SHCK_DRCTN_domain = {		"0":"Not_applicable",
		"1":"Up",
		"2":"Down",
}

	SHCK_DRCTN = models.CharField("SHCK_DRCTN",max_length=255, choices=SHCK_DRCTN_domain,default=None, blank=True, null=True, db_comment="SHCK_DRCTN_domain")

	TNR = models.FloatField("TNR",default=None, blank=True, null=True)

	UNDRLYNG_RSDL_MTRTY = models.FloatField("UNDRLYNG_RSDL_MTRTY",default=None, blank=True, null=True)

	VG_SNSTVTY = models.FloatField("VG_SNSTVTY",default=None, blank=True, null=True)

	theRSK_FAC_SA = models.ForeignKey("RSK_FAC_SA", models.SET_NULL,blank=True,null=True,related_name="FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_FR_SCRTY_PSTNS_to_theRSK_FAC_SAs")

	theSCRTY_PSTN = models.ForeignKey("SCRTY_PSTN", models.SET_NULL,blank=True,null=True,related_name="FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_FR_SCRTY_PSTNS_to_theSCRTY_PSTNs")

	class Meta:

		verbose_name = 'FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_FR_SCRTY_PSTNS'

		verbose_name_plural = 'FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_FR_SCRTY_PSTNSs'

class FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_OTC_PSTNS(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_OTC_PSTNS_uniqueID = models.CharField("FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_OTC_PSTNS_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ID = models.CharField("FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ID",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ISO4217_INPT_domain = {		"0":"Not_applicable",
		"AED":"UAE_Dirham",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"ARS":"Argentine_Peso",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYN":"Belarussian_Ruble",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHE":"WIR_Euro",
		"CHF":"Swiss_franc",
		"CHW":"WIR_Franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CZK":"Czech_koruna",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GTQ":"Quetzal",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"ILS":"New_Israeli_Sheqel",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MRU":"Ouguiya_x2",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDG":"Sudanese_Pound",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SRD":"Surinam_Dollar",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"STN":"Dobra_x2",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJS":"Somoni",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"USN":"US_Dollar_Next_day",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UYW":"Unidad_Previsional",
		"UZS":"Uzbekistan_Sum",
		"VEF":"Bolivar",
		"VES":"Bolivar_Soberano",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XAG":"Silver_one_Troy_ounce",
		"XAU":"Gold_one_Troy_ounce",
		"XBA":"Bond_Markets_Unit_European_Composite_Unit_EURCO",
		"XBB":"Bond_Markets_Unit_European_Monetary_Unit_E_M_U_6",
		"XBC":"Bond_Markets_Unit_European_Unit_of_Account_9_E_U_A_9",
		"XBD":"Bond_Markets_Unit_European_Unit_of_Account_17_E_U_A_17",
		"XCD":"East_Caribbean_Dollar",
		"XDR":"Special_Drawing_Rights_SDR",
		"XOF":"CFA_Franc_BCEAO",
		"XPD":"Palladium_one_Troy_ounce",
		"XPF":"CFP_Franc",
		"XPT":"Platinum_one_Troy_ounce",
		"XSU":"Sucre",
		"XTS":"Codes_specifically_reserved_for_testing_purposes",
		"XUA":"ADB_Unit_of_Account",
		"XXX":"Code_assigned_for_transactions_where_no_currency_is_involved",
		"YER":"Yemeni_Rial",
		"ZAR":"South_African_Rand",
		"ZMW":"Zambian_Kwacha",
		"ZWL":"Zimbabwe_Dollar",
}

	CRRNCY_RCRD = models.CharField("CRRNCY_RCRD",max_length=255, choices=ISO4217_INPT_domain,default=None, blank=True, null=True, db_comment="ISO4217_INPT_domain")

	CRVTR_RSK_WGHT = models.FloatField("CRVTR_RSK_WGHT",default=None, blank=True, null=True)

	CRVTR_VLTN_DFFRNC = models.FloatField("CRVTR_VLTN_DFFRNC",default=None, blank=True, null=True)

	DLT_SNSTVTY = models.FloatField("DLT_SNSTVTY",default=None, blank=True, null=True)

	OPTN_MTRTY = models.FloatField("OPTN_MTRTY",default=None, blank=True, null=True)

	FRTB_RSK_MSR_TYP_domain = {		"4":"Delta_sensitivity",
		"5":"Vega_sensitivity",
		"6":"Curvature",
}

	RSK_MSR_TYP = models.CharField("RSK_MSR_TYP",max_length=255, choices=FRTB_RSK_MSR_TYP_domain,default=None, blank=True, null=True, db_comment="FRTB_RSK_MSR_TYP_domain")

	RSK_MSR_TYP_PSTN_domain = {		"1":"Fundamental_review_of_the_trading_book_standard_approach_risk_measure_for_OTC_positions",
		"2":"Fundamental_review_of_the_trading_book_standard_approach_risk_measure_for_ETD_positions",
		"3":"Fundamental_review_of_the_trading_book_standard_approach_risk_measure_for_security_positions",
}

	RSK_MSR_TYP_PSTN = models.CharField("RSK_MSR_TYP_PSTN",max_length=255, choices=RSK_MSR_TYP_PSTN_domain,default=None, blank=True, null=True, db_comment="RSK_MSR_TYP_PSTN_domain")

	SHCK_DRCTN_domain = {		"0":"Not_applicable",
		"1":"Up",
		"2":"Down",
}

	SHCK_DRCTN = models.CharField("SHCK_DRCTN",max_length=255, choices=SHCK_DRCTN_domain,default=None, blank=True, null=True, db_comment="SHCK_DRCTN_domain")

	TNR = models.FloatField("TNR",default=None, blank=True, null=True)

	UNDRLYNG_RSDL_MTRTY = models.FloatField("UNDRLYNG_RSDL_MTRTY",default=None, blank=True, null=True)

	VG_SNSTVTY = models.FloatField("VG_SNSTVTY",default=None, blank=True, null=True)

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_OTC_PSTNS_to_theINSTRMNTs")

	theRSK_FAC_SA = models.ForeignKey("RSK_FAC_SA", models.SET_NULL,blank=True,null=True,related_name="FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_OTC_PSTNS_to_theRSK_FAC_SAs")

	class Meta:

		verbose_name = 'FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_OTC_PSTNS'

		verbose_name_plural = 'FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_OTC_PSTNSs'

class FNNCL_CNTRCT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	FNNCL_CNTRCT_uniqueID = models.CharField("FNNCL_CNTRCT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	FNNCL_CNTRCT_ID = models.CharField("FNNCL_CNTRCT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	DT_INCPTN = models.DateTimeField("DT_INCPTN",default=None, blank=True, null=True)

	DT_LGL_FNL_MTRTY = models.DateTimeField("DT_LGL_FNL_MTRTY",default=None, blank=True, null=True)

	FNNCL_CNTRCT_TYP_domain = {		"1":"Single_financial_contract",
		"2":"Syndicated_financial_contract_member",
}

	FNNCL_CNTRCT_TYP = models.CharField("FNNCL_CNTRCT_TYP",max_length=255, choices=FNNCL_CNTRCT_TYP_domain,default=None, blank=True, null=True, db_comment="FNNCL_CNTRCT_TYP_domain")

	theSYNDCTD_CNTRCT = models.ForeignKey("SYNDCTD_CNTRCT", models.SET_NULL,blank=True,null=True,related_name="FNNCL_CNTRCT_to_theSYNDCTD_CNTRCTs")

	class Meta:

		verbose_name = 'FNNCL_CNTRCT'

		verbose_name_plural = 'FNNCL_CNTRCTs'

class FNNCL_GRNT_INSTRMNT_DBT_SCRT_DBT_SCRTY_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	FNNCL_GRNT_INSTRMNT_DBT_SCRT_DBT_SCRTY_ASSGNMNT_uniqueID = models.CharField("FNNCL_GRNT_INSTRMNT_DBT_SCRT_DBT_SCRTY_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	PRTCTN_ALLCTD_VL = models.BigIntegerField("PRTCTN_ALLCTD_VL",default=None, blank=True, null=True)

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="FNNCL_GRNT_INSTRMNT_DBT_SCRT_DBT_SCRTY_ASSGNMNT_to_theINSTRMNTs")

	theSCRTY_EXCHNG_TRDBL_DRVTV = models.ForeignKey("SCRTY_EXCHNG_TRDBL_DRVTV", models.SET_NULL,blank=True,null=True,related_name="FNNCL_GRNT_INSTRMNT_DBT_SCRT_DBT_SCRTY_ASSGNMNT_to_theSCRTY_EXCHNG_TRDBL_DRVTVs")

	class Meta:

		verbose_name = 'FNNCL_GRNT_INSTRMNT_DBT_SCRT_DBT_SCRTY_ASSGNMNT'

		verbose_name_plural = 'FNNCL_GRNT_INSTRMNT_DBT_SCRT_DBT_SCRTY_ASSGNMNTs'

class FR_VL_DCRS_CNTNGNT_ENCMBRNC(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	FR_VL_DCRS_CNTNGNT_ENCMBRNC_uniqueID = models.CharField("FR_VL_DCRS_CNTNGNT_ENCMBRNC_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	ACCNTNG_FRMWRK_domain = {		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	CLLTRLSD_DPSTS_OTHR_RPRCHS_AGRMNTS_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("CLLTRLSD_DPSTS_OTHR_RPRCHS_AGRMNTS_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	CLLTRLSD_DPSTS_OTHR_RPRCHS_AGRMNTS_CNTRL_BNKS_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("CLLTRLSD_DPSTS_OTHR_RPRCHS_AGRMNTS_CNTRL_BNKS_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("DBT_SCRTY_ISSD_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_CVRD_BNDS_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("DBT_SCRTY_ISSD_CVRD_BNDS_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_SCRTSTNS_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("DBT_SCRTY_ISSD_SCRTSTNS_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	DPSTS_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("DPSTS_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	DRVTVS_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("DRVTVS_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	OTC_DRVTV_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("OTC_DRVTV_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	OTHR_SRCS_ENCMBRNC_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("OTHR_SRCS_ENCMBRNC_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	RPRCHS_AGRMNT_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("RPRCHS_AGRMNT_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	RPRCHS_AGRMNT_CNTRL_BNK_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("RPRCHS_AGRMNT_CNTRL_BNK_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	SLCTD_FNNCL_LBLT_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("SLCTD_FNNCL_LBLT_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	TTL_SRCS_ENCMBRNC_ADDTNL_ENCMBRD_CRRYNG_AMNT = models.BigIntegerField("TTL_SRCS_ENCMBRNC_ADDTNL_ENCMBRD_CRRYNG_AMNT",default=None, blank=True, null=True)

	class Meta:

		verbose_name = 'FR_VL_DCRS_CNTNGNT_ENCMBRNC'

		verbose_name_plural = 'FR_VL_DCRS_CNTNGNT_ENCMBRNCs'

class GLD_CLLTRL_LG_GLD_CLLTRL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	GLD_CLLTRL_LG_GLD_CLLTRL_ASSGNMNT_uniqueID = models.CharField("GLD_CLLTRL_LG_GLD_CLLTRL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain = {		"3":"Security_leg",
		"4":"Loans_and_advances_leg",
		"5":"Equity_instrument_leg",
		"6":"Reverse_repurchase_agreement_cash_leg",
		"7":"Repurchase_agreement_cash_leg",
		"8":"Gold_collateral_leg",
}

	RPRCHS_AGRMNT_CMPNNT_TYP = models.CharField("RPRCHS_AGRMNT_CMPNNT_TYP",max_length=255, choices=RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain")

	RPRCHS_AGRMNT_INSTRMNT_ID = models.CharField("RPRCHS_AGRMNT_INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	theCLLTRL = models.ForeignKey("CLLTRL", models.SET_NULL,blank=True,null=True,related_name="GLD_CLLTRL_LG_GLD_CLLTRL_ASSGNMNT_to_theCLLTRLs")

	theRPRCHS_AGRMNT_CMPNNT = models.ForeignKey("RPRCHS_AGRMNT_CMPNNT", models.SET_NULL,blank=True,null=True,related_name="GLD_CLLTRL_LG_GLD_CLLTRL_ASSGNMNT_to_theRPRCHS_AGRMNT_CMPNNTs")

	class Meta:

		verbose_name = 'GLD_CLLTRL_LG_GLD_CLLTRL_ASSGNMNT'

		verbose_name_plural = 'GLD_CLLTRL_LG_GLD_CLLTRL_ASSGNMNTs'

class GRP(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	GRP_uniqueID = models.CharField("GRP_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	GRP_ID = models.CharField("GRP_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	TYP_GRP_INPT_domain = {		"13":"Group_of_consolidated_clients",
		"14":"Accounting_consolidation_group",
		"15":"Prudential_consolidation_group",
		"16":"Subsidiary_joint_venture_and_associate",
		"17":"Foreign_institutional_unit",
		"18":"Domestic_institutional_unit",
		"4":"Other_group_of_clients",
		"6":"Group_of_connected_clients",
}

	TYP_GRP = models.CharField("TYP_GRP",max_length=255, choices=TYP_GRP_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_GRP_INPT_domain")

	class Meta:

		verbose_name = 'GRP'

		verbose_name_plural = 'GRPs'

class GRP_KY_MNGMNT_PRSNLL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	GRP_KY_MNGMNT_PRSNLL_ASSGNMNT_uniqueID = models.CharField("GRP_KY_MNGMNT_PRSNLL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	GRP_ID = models.CharField("GRP_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	NTRL_PRSN_GRP_RL_TYP = models.CharField("NTRL_PRSN_GRP_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	GRP_KY_MNGMNT_PRSNNL_ASSGNMNT_TYP_domain = {		"0":"Internal_group_Key_management_personnel_assignment",
		"1":"Group_of_clients_Key_management_personnel_assignment",
}

	GRP_KY_MNGMNT_PRSNNL_ASSGNMNT_TYP = models.CharField("GRP_KY_MNGMNT_PRSNNL_ASSGNMNT_TYP",max_length=255, choices=GRP_KY_MNGMNT_PRSNNL_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="GRP_KY_MNGMNT_PRSNNL_ASSGNMNT_TYP_domain")

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="GRP_KY_MNGMNT_PRSNLL_ASSGNMNT_to_theENTTY_RLs")

	theGRP = models.ForeignKey("GRP", models.SET_NULL,blank=True,null=True,related_name="GRP_KY_MNGMNT_PRSNLL_ASSGNMNT_to_theGRPs")

	class Meta:

		verbose_name = 'GRP_KY_MNGMNT_PRSNLL_ASSGNMNT'

		verbose_name_plural = 'GRP_KY_MNGMNT_PRSNLL_ASSGNMNTs'

class IMMDT_PRNT_ENTRPRS_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	IMMDT_PRNT_ENTRPRS_ASSGNMNT_uniqueID = models.CharField("IMMDT_PRNT_ENTRPRS_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	IMMDT_PRNT_CNTRL_BNK_PRVT_SCTR_CMPNY_PRTY_ID = models.CharField("IMMDT_PRNT_CNTRL_BNK_PRVT_SCTR_CMPNY_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	IMMDT_PRNT_ENTRPRS_PRTY_ID = models.CharField("IMMDT_PRNT_ENTRPRS_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	IMMDT_PRNT_ENTRPRS_PRTY_RL_TYP = models.CharField("IMMDT_PRNT_ENTRPRS_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ACCMLTD_EQT_INTRST = models.FloatField("ACCMLTD_EQT_INTRST",default=None, blank=True, null=True)

	IMMDT_PRNT_ANCRDT_INDCTR_domain = {		"1":"Immediate_parent_according_to_AnaCredit",
		"2":"Not_immediate_parent_according_to_AnaCredit",
}

	IMMDT_PRNT_RGLTN_867_2016_INDCTR = models.CharField("IMMDT_PRNT_RGLTN_867_2016_INDCTR",max_length=255, choices=IMMDT_PRNT_ANCRDT_INDCTR_domain,default=None, blank=True, null=True, db_comment="IMMDT_PRNT_ANCRDT_INDCTR_domain")

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="IMMDT_PRNT_ENTRPRS_ASSGNMNT_to_theENTTY_RLs")

	thePRTY = models.ForeignKey("PRTY", models.SET_NULL,blank=True,null=True,related_name="IMMDT_PRNT_ENTRPRS_ASSGNMNT_to_thePRTYs")

	class Meta:

		verbose_name = 'IMMDT_PRNT_ENTRPRS_ASSGNMNT'

		verbose_name_plural = 'IMMDT_PRNT_ENTRPRS_ASSGNMNTs'

class INSTRMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_uniqueID = models.CharField("INSTRMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ACCMLTD_CVRG_RT = models.FloatField("ACCMLTD_CVRG_RT",default=None, blank=True, null=True)

	RSDL_MTRTY_BND_domain = {		"12":"_3m_6m",
		"16":"_6m_12m",
		"21":"_1y_2y",
		"28":"_2y_3y",
		"3":"_1d_1w",
		"31":"_3y_5y",
		"36":"_5y_10y",
		"40":"Over_10_years",
		"64":"_0d_1d",
		"81":"_gt_7_days_lt_eq_14_days",
		"82":"_gt_2_weeks_lt_eq_1_month",
		"9":"_1m_3m",
		"999":"Open_maturity",
}

	ASST_ENCMBRNC_RSDL_MTRTY_BND = models.CharField("ASST_ENCMBRNC_RSDL_MTRTY_BND",max_length=255, choices=RSDL_MTRTY_BND_domain,default=None, blank=True, null=True, db_comment="RSDL_MTRTY_BND_domain")

	CMMRCL_RL_ESTT_LN_INDCTR_domain = {		"1":"Commercial_real_estate_loan",
		"2":"Not_a_commercial_real_estate_loan",
}

	CMMRCL_RL_ESTT_LN_INDCTR = models.CharField("CMMRCL_RL_ESTT_LN_INDCTR",max_length=255, choices=CMMRCL_RL_ESTT_LN_INDCTR_domain,default=None, blank=True, null=True, db_comment="CMMRCL_RL_ESTT_LN_INDCTR_domain")

	ISO4217_INPT_domain = {		"0":"Not_applicable",
		"AED":"UAE_Dirham",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"ARS":"Argentine_Peso",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYN":"Belarussian_Ruble",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHE":"WIR_Euro",
		"CHF":"Swiss_franc",
		"CHW":"WIR_Franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CZK":"Czech_koruna",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GTQ":"Quetzal",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"ILS":"New_Israeli_Sheqel",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MRU":"Ouguiya_x2",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDG":"Sudanese_Pound",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SRD":"Surinam_Dollar",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"STN":"Dobra_x2",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJS":"Somoni",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"USN":"US_Dollar_Next_day",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UYW":"Unidad_Previsional",
		"UZS":"Uzbekistan_Sum",
		"VEF":"Bolivar",
		"VES":"Bolivar_Soberano",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XAG":"Silver_one_Troy_ounce",
		"XAU":"Gold_one_Troy_ounce",
		"XBA":"Bond_Markets_Unit_European_Composite_Unit_EURCO",
		"XBB":"Bond_Markets_Unit_European_Monetary_Unit_E_M_U_6",
		"XBC":"Bond_Markets_Unit_European_Unit_of_Account_9_E_U_A_9",
		"XBD":"Bond_Markets_Unit_European_Unit_of_Account_17_E_U_A_17",
		"XCD":"East_Caribbean_Dollar",
		"XDR":"Special_Drawing_Rights_SDR",
		"XOF":"CFA_Franc_BCEAO",
		"XPD":"Palladium_one_Troy_ounce",
		"XPF":"CFP_Franc",
		"XPT":"Platinum_one_Troy_ounce",
		"XSU":"Sucre",
		"XTS":"Codes_specifically_reserved_for_testing_purposes",
		"XUA":"ADB_Unit_of_Account",
		"XXX":"Code_assigned_for_transactions_where_no_currency_is_involved",
		"YER":"Yemeni_Rial",
		"ZAR":"South_African_Rand",
		"ZMW":"Zambian_Kwacha",
		"ZWL":"Zimbabwe_Dollar",
}

	CRRNCY = models.CharField("CRRNCY",max_length=255, choices=ISO4217_INPT_domain,default=None, blank=True, null=True, db_comment="ISO4217_INPT_domain")

	CRRNT_LTV_RT = models.FloatField("CRRNT_LTV_RT",default=None, blank=True, null=True)

	CSH_RSRV_AMNT = models.BigIntegerField("CSH_RSRV_AMNT",default=None, blank=True, null=True)

	DT_CSH_RSRV_MTRTY = models.DateTimeField("DT_CSH_RSRV_MTRTY",default=None, blank=True, null=True)

	DT_INCPTN = models.DateTimeField("DT_INCPTN",default=None, blank=True, null=True)

	DT_LGL_FNL_MTRTY = models.DateTimeField("DT_LGL_FNL_MTRTY",default=None, blank=True, null=True)

	DT_ORGNL_CSH_RSRV_AMNT = models.DateTimeField("DT_ORGNL_CSH_RSRV_AMNT",default=None, blank=True, null=True)

	DT_STTLMNT = models.DateTimeField("DT_STTLMNT",default=None, blank=True, null=True)

	ELGBL_CNTRL_BNK_FNDNG_INPT_domain = {		"0":"Not_applicable_To_be_used_if_central_bank_eligibility_does_not_apply",
		"1":"Eligible_for_central_bank_funding_Specifies_if_an_object_is_eligible_for_central_bank_funding_in_the_sense_that_it_might_be_exchanged_provided_as_collateral_for_funding",
		"2":"Not_elibible_for_central_bank_funding_Specifies_if_an_object_is_not_eligible_for_central_bank_funding",
}

	ELGBL_CNTRL_BNK_FNDNG_INDCTR = models.CharField("ELGBL_CNTRL_BNK_FNDNG_INDCTR",max_length=255, choices=ELGBL_CNTRL_BNK_FNDNG_INPT_domain,default=None, blank=True, null=True, db_comment="ELGBL_CNTRL_BNK_FNDNG_INPT_domain")

	HQLA_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"High_liquidity_and_credit_quality_HQLA",
		"2":"Not_high_liquidity_and_credit_quality_HQLA",
}

	HQLA_INDCTR = models.CharField("HQLA_INDCTR",max_length=255, choices=HQLA_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="HQLA_INDCTR_INPT_domain")

	INSTRMNT_TYP_ORGN_domain = {		"3":"Instrument_resulting_directly_from_a_Financial_contract",
		"4":"Instrument_resulting_from_a_Credit_facility",
}

	INSTRMNT_TYP_ORGN = models.CharField("INSTRMNT_TYP_ORGN",max_length=255, choices=INSTRMNT_TYP_ORGN_domain,default=None, blank=True, null=True, db_comment="INSTRMNT_TYP_ORGN_domain")

	LTGTN_STTS_INPT_domain = {		"0":"Not_applicable",
		"1":"In_pre_litigation",
		"2":"In_litigation",
		"3":"Not_in_litigation_pre_litigation",
}

	LTGTN_STTS = models.CharField("LTGTN_STTS",max_length=255, choices=LTGTN_STTS_INPT_domain,default=None, blank=True, null=True, db_comment="LTGTN_STTS_INPT_domain")

	MNMM_RSRV_AMNT = models.BigIntegerField("MNMM_RSRV_AMNT",default=None, blank=True, null=True)

	NMNL_AMNT = models.BigIntegerField("NMNL_AMNT",default=None, blank=True, null=True)

	NTNL_AMNT = models.BigIntegerField("NTNL_AMNT",default=None, blank=True, null=True)

	OFF_BLNC_SHT_AMNT = models.BigIntegerField("OFF_BLNC_SHT_AMNT",default=None, blank=True, null=True)

	ORGNL_CSH_RSRV_AMNT = models.BigIntegerField("ORGNL_CSH_RSRV_AMNT",default=None, blank=True, null=True)

	OVRDRFT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Overdraft_deposit",
		"2":"Deposit_not_in_overdraft",
}

	OVRDRFT_INDCTR = models.CharField("OVRDRFT_INDCTR",max_length=255, choices=OVRDRFT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="OVRDRFT_INDCTR_INPT_domain")

	RPYMNT_RGHTS_INPT_domain = {		"0":"Not_applicable",
		"1":"On_demand_or_short_notice_Instruments_which_are_repayable_on_demand_or_at_short_notice_at_the_request_of_the_creditor",
		"2":"Other_than_on_demand_or_short_notice_Instruments_subject_to_repayment_rights_other_than_on_demand_or_at_short_notice",
}

	RPYMNT_RGHTS = models.CharField("RPYMNT_RGHTS",max_length=255, choices=RPYMNT_RGHTS_INPT_domain,default=None, blank=True, null=True, db_comment="RPYMNT_RGHTS_INPT_domain")

	RVCBL_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Revocable",
		"2":"Not_revocable",
}

	RVCBL_INDCTR = models.CharField("RVCBL_INDCTR",max_length=255, choices=RVCBL_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="RVCBL_INDCTR_INPT_domain")

	RVLVNG_LN_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Revolving_loan",
		"2":"Not_revolving_loan",
}

	RVLVNG_LN_INDCTR = models.CharField("RVLVNG_LN_INDCTR",max_length=255, choices=RVLVNG_LN_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="RVLVNG_LN_INDCTR_INPT_domain")

	SGNFCNT_ASST_CLSS_INPT_domain = {		"0":"Not_applicable",
		"1":"Interest_rate",
		"2":"Equity",
		"3":"Credit",
		"4":"Commodity",
		"5":"Other",
}

	SGNFCNT_ASST_CLSS = models.CharField("SGNFCNT_ASST_CLSS",max_length=255, choices=SGNFCNT_ASST_CLSS_INPT_domain,default=None, blank=True, null=True, db_comment="SGNFCNT_ASST_CLSS_INPT_domain")

	SNDCTN_SB_PRTCPTN_MMBR_INSTRMNT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Syndication_or_sub_participation_member_instrument",
		"2":"Non_syndicated_contract_nor_sub_participation_member_instrument",
}

	SNDCTN_SB_PRTCPTN_MMBR_INSTRMNT_INDCTR = models.CharField("SNDCTN_SB_PRTCPTN_MMBR_INSTRMNT_INDCTR",max_length=255, choices=SNDCTN_SB_PRTCPTN_MMBR_INSTRMNT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="SNDCTN_SB_PRTCPTN_MMBR_INSTRMNT_INDCTR_INPT_domain")

	TYP_CMMTMNT_INPT_domain = {		"0":"Not_applicable",
		"1":"Forward_deposits",
		"10":"Loans_commitments_received",
		"11":"Other_commitments_received",
		"12":"To_lend_or_to_provide_acceptance_facilities_at_a_below_market_interest_rate",
		"13":"To_lend_or_to_provide_acceptance_facilities_under_pre_specified_terms_and_conditions_other_than_those_at_a_below_market_interest_rate",
		"14":"To_lend_or_to_provide_acceptance_facilities_where_the_terms_and_conditions_are_not_under_pre_specified",
		"15":"To_provide_guarantees",
		"16":"To_purchase_securities",
		"17":"For_tender_and_performance_guarantees",
		"18":"Other_Credit_Facilities_Other",
		"2":"Unpaid_portion_of_partly_paid_shares_and_securities",
		"3":"Documentary_credits_issued_or_confirmed",
		"4":"Trade_finance_off_balance_sheet_items",
		"5":"Documentary_credits_in_which_underlying_shipment_acts_as_collateral_and_other_self_liquidating_transactions",
		"6":"Warranties_and_indemnities_including_tender_and_performance_bonds_and_guarantees_not_having_the_character_of_credit_substitutes",
		"7":"Shipping_guarantees_customs_and_tax_bonds",
		"8":"Note_issuance_facilities_NIFs_and_Revolving_underwritings_facilities_RUFs",
		"9":"Other_off_balance_sheet_items",
}

	TYP_CMMTMNT = models.CharField("TYP_CMMTMNT",max_length=255, choices=TYP_CMMTMNT_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_CMMTMNT_INPT_domain")

	TYP_INSTRMNT_INPT_domain = {		"10":"OTC_Option_other_than_OTC_Credit_spread_option",
		"1003":"Reverse_repurchase_agreement_instrument",
		"1011":"Other_commitment",
		"1020":"Factoring",
		"1022":"Other_loan",
		"1023":"Other_trade_receivables",
		"120":"Transit_items",
		"1201":"Loan_on_demand_used_for_minimum_reserve",
		"1202":"On_demand_deposit_not_used_for_minimum_reserve",
		"13":"Financial_guarantee_instrument_for_a_Debt_security",
		"130":"Suspence_items",
		"14":"Financial_guarantee_instrument_not_for_a_Debt_security",
		"140":"Other_advance",
		"18":"Term_repurchase_agreement_instrument",
		"19":"Open_repurchase_agreement_instrument",
		"2":"Equity_instrument_that_is_not_a_security",
		"26":"Security_against_a_fee_borrowing_and_lending_transaction",
		"27":"Security_against_Security_borrowing_and_lending_transaction",
		"380":"Forward",
		"5":"Other_OTC_Derivative_instrument",
		"51":"Credit_card_debt",
		"511":"Tranferable_deposit",
		"512":"Other_overnight_deposits",
		"522":"Deposits_with_agreed_maturity_other_than_counterpart_liability_to_non_derecognised_loans",
		"6":"OTC_Total_return_swap",
		"7":"OTC_Credit_default_swap",
		"8":"Other_OTC_Swap",
		"80":"Finance_leases",
		"9":"OTC_Credit_spread_option",
}

	TYP_INSTRMNT = models.CharField("TYP_INSTRMNT",max_length=255, choices=TYP_INSTRMNT_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_INSTRMNT_INPT_domain")

	TYP_RSK_INPT_domain = {		"0":"Not_Applicable",
		"1":"Interest_rate_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_a",
		"2":"Equity_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_b",
		"3":"Foreign_exchange_and_gold_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_c",
		"4":"Credit_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_d",
		"5":"Commodities_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_e",
		"6":"Risk_other_than_Interest_rate_risk_Equity_risk_Foreign_exchange_and_gold_risk_Credit_risk_Commodities_risk_Type_of_risk_in_accordance_with_Reg_680_2014_Annex_V_part_2_129_f",
}

	TYP_RSK = models.CharField("TYP_RSK",max_length=255, choices=TYP_RSK_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_RSK_INPT_domain")

	theBLNC_SHT_NTTNG = models.ForeignKey("BLNC_SHT_NTTNG", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_to_theBLNC_SHT_NTTNGs")

	theCRDT_FCLTY = models.ForeignKey("CRDT_FCLTY", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_to_theCRDT_FCLTYs")

	theFNNCL_CNTRCT = models.ForeignKey("FNNCL_CNTRCT", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_to_theFNNCL_CNTRCTs")

	class Meta:

		verbose_name = 'INSTRMNT'

		verbose_name_plural = 'INSTRMNTs'

class INSTRMNT_CLLTRL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_CLLTRL_ASSGNMNT_uniqueID = models.CharField("INSTRMNT_CLLTRL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	CLLTRL_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"1":"Collateral_received",
		"2":"Collateral_given",
}

	CLLTRL_RL_TYP = models.CharField("CLLTRL_RL_TYP",max_length=255, choices=CLLTRL_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="CLLTRL_RL_TYP_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ALLCTD_UNSD_CLLTRL_VL = models.FloatField("ALLCTD_UNSD_CLLTRL_VL",default=None, blank=True, null=True)

	CLLTRL_VL_UNCPPD = models.FloatField("CLLTRL_VL_UNCPPD",default=None, blank=True, null=True)

	INSTRMNT_CLLTRL_ASSGNMNT_TYP_domain = {		"1":"Loan_excluding_repurchase_agreement_and_advance_Collateral_received_assignment",
		"2":"Off_balance_instrument_Collateral_received_assignment",
		"3":"Loan_excluding_repurchase_agreement_and_advance_Collateral_given_assignment",
		"4":"Off_balance_instrument_Collateral_given_assignment",
}

	INSTRMNT_CLLTRL_ASSGNMNT_TYP = models.CharField("INSTRMNT_CLLTRL_ASSGNMNT_TYP",max_length=255, choices=INSTRMNT_CLLTRL_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="INSTRMNT_CLLTRL_ASSGNMNT_TYP_domain")

	PRTCTN_ALLCTD_VL = models.BigIntegerField("PRTCTN_ALLCTD_VL",default=None, blank=True, null=True)

	THRD_PRTY_PRRTY_CLMS = models.BigIntegerField("THRD_PRTY_PRRTY_CLMS",default=None, blank=True, null=True)

	theCLLTRL_RL = models.ForeignKey("CLLTRL_RL", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_CLLTRL_ASSGNMNT_to_theCLLTRL_RLs")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_CLLTRL_ASSGNMNT_to_theINSTRMNTs")

	class Meta:

		verbose_name = 'INSTRMNT_CLLTRL_ASSGNMNT'

		verbose_name_plural = 'INSTRMNT_CLLTRL_ASSGNMNTs'

class INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT_uniqueID = models.CharField("INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"12":"Non_balance_sheet_recognised_financial_liability_instrument",
		"34":"Balance_sheet_recognised_financial_asset_instrument_according_to_national_general_accepted_accounting_principles_nGAAP",
		"35":"Balance_sheet_recognised_financial_asset_instrument_according_to_International_Financial_Reporting_Standard_IFRS",
		"37":"Non_fair_valued_balance_sheet_recognised_financial_liability_instrument",
		"38":"Over_the_counter_OTC_Credit_default_swap_received_as_collateral_instrument",
		"39":"Other_collateral_received_instrument",
		"46":"Fair_valued_Balance_sheet_recognised_financial_liability_instrument_according_to_International_Financial_Reporting_Standard_IFRS",
		"47":"Fair_valued_balance_sheet_recognised_financial_liability_instrument_according_to_national_general_accepted_accounting_principles_nGAAP",
		"501":"Forborne_off_balance_sheet_item_given_instrument",
		"502":"Non_Forborne_off_balance_sheet_item_given_instrument",
		"6":"Off_balance_sheet_item_received_instrument",
		"8":"Collateral_given_instrument",
}

	TYP_INSTRMNT_RL = models.CharField("TYP_INSTRMNT_RL",max_length=255, choices=INSTRMNT_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="INSTRMNT_RL_TYP_INPT_domain")

	INSTRMNT_CLLTRL_INSTRMNT_ASSGNMNT_TYP_domain = {		"1":"Over_the_counter_OTC_Credit_default_swap_Collateral_received_instrument_assignment",
		"2":"Instrument_Collateral_received_instrument_assignment",
		"3":"Collateral_given_instrument_Instrument_assignment",
}

	INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT_TYP = models.CharField("INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT_TYP",max_length=255, choices=INSTRMNT_CLLTRL_INSTRMNT_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="INSTRMNT_CLLTRL_INSTRMNT_ASSGNMNT_TYP_domain")

	PRTCTN_ALLCTD_VL = models.BigIntegerField("PRTCTN_ALLCTD_VL",default=None, blank=True, null=True)

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT_to_theINSTRMNTs")

	theINSTRMNT_RL = models.ForeignKey("INSTRMNT_RL", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT_to_theINSTRMNT_RLs")

	class Meta:

		verbose_name = 'INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT'

		verbose_name_plural = 'INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNTs'

class INSTRMNT_ENTTY_RL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID = models.CharField("INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	PRTY_RL_TYP = models.CharField("PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_ENTTY_RL_ASSGNMNT_TYP_domain = {		"1":"Equity_instrument_that_is_not_a_security_Investor_assignment",
		"10":"Other_commitment_Debtor_assignment",
		"11":"Over_the_counter_OTC_Derivative_Buyer_assignment",
		"12":"Advance_Creditor_assignment",
		"13":"Over_the_counter_OTC_Derivative_Seller_assignment",
		"14":"Advance_Debtor_assignment",
		"15":"Deposit_Depositor_assignment",
		"16":"Credit_card_debt_Creditor_assignment",
		"17":"Credit_card_debt_Debtor_assignment",
		"18":"Deposit_Deposit_taking_corporation_assignment",
		"19":"Financial_guarantee_instrument_Beneficiary_assignment",
		"2":"Equity_instrument_that_is_not_a_security_Issuer_assignment",
		"20":"Trade_receivable_Assigned_debtor_assignment",
		"21":"Financial_guarantee_instrument_Protection_provider_assignment",
		"22":"Trade_receivable_Factor_assignment",
		"23":"Financial_lease_Lessor_assignment",
		"24":"Financial_lease_Lessee_assignment",
		"25":"Instrument_Servicer_assignment",
		"26":"Reverse_repurchase_agreement_loan_Loan_debtor_assignment",
		"27":"Reverse_repurchase_agreement_loan_Creditor_assignment",
		"3":"Security_borrowing_and_lending_transaction_Borrower_assignment",
		"4":"Other_loan_Creditor_assignment",
		"5":"Security_borrowing_and_lending_transaction_Lender_assignment",
		"6":"Other_loan_Debtor_assignment",
		"7":"Repurchase_agreement_Buyer_assignment",
		"8":"Other_commitment_Creditor_assignment",
		"9":"Repurchase_agreement_Seller_assignment",
}

	INSTRMNT_ENTTY_RL_ASSGNMNT_TYP = models.CharField("INSTRMNT_ENTTY_RL_ASSGNMNT_TYP",max_length=255, choices=INSTRMNT_ENTTY_RL_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="INSTRMNT_ENTTY_RL_ASSGNMNT_TYP_domain")

	JNT_LBLTY_AMNT = models.BigIntegerField("JNT_LBLTY_AMNT",default=None, blank=True, null=True)

	LTGTN_STTS_INPT_domain = {		"0":"Not_applicable",
		"1":"In_pre_litigation",
		"2":"In_litigation",
		"3":"Not_in_litigation_pre_litigation",
}

	LTGTN_STTS = models.CharField("LTGTN_STTS",max_length=255, choices=LTGTN_STTS_INPT_domain,default=None, blank=True, null=True, db_comment="LTGTN_STTS_INPT_domain")

	MN_DBTR_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Main_debtor",
		"2":"Not_main_debtor",
}

	MN_DBTR_INDCTR = models.CharField("MN_DBTR_INDCTR",max_length=255, choices=MN_DBTR_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="MN_DBTR_INDCTR_INPT_domain")

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_ENTTY_RL_ASSGNMNT_to_theENTTY_RLs")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_ENTTY_RL_ASSGNMNT_to_theINSTRMNTs")

	class Meta:

		verbose_name = 'INSTRMNT_ENTTY_RL_ASSGNMNT'

		verbose_name_plural = 'INSTRMNT_ENTTY_RL_ASSGNMNTs'

class INSTRMNT_HDGD_EXCHNG_TRDBL_DRVTV(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_HDGD_EXCHNG_TRDBL_DRVTV_uniqueID = models.CharField("INSTRMNT_HDGD_EXCHNG_TRDBL_DRVTV_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	BYR_PRTY_ID = models.CharField("BYR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	BYR_PRTY_RL_TYP = models.CharField("BYR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	EXCHNG_TRDBL_DRVTV_SCRTY_ID = models.CharField("EXCHNG_TRDBL_DRVTV_SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SLLR_PRTY_ID = models.CharField("SLLR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	SLLR_PRTY_RL_TYP = models.CharField("SLLR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	EXCHNG_TRDBL_DRVTV_PSTN_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"10":"Non_fair_valued_balance_sheet_recognised_exchange_tradable_derivative_asset_position",
		"12":"Non_balance_sheet_recognised_exchange_tradable_derivative_asset_position",
		"41":"Exchange_tradable_derivative_position_as_a_hedge_according_to_International_Financial_Reporting_Standard_IFRS",
		"42":"Exchange_tradable_derivative_position_as_a_hedge_according_to_national_general_accepted_accounting_principles_nGAAP",
		"6":"Non_balance_sheet_recognised_exchange_tradable_derivative_liability_position",
		"7":"Fair_valued_balance_sheet_recognised_exchange_tradable_derivative_liability_position",
		"8":"Non_fair_valued_balance_sheet_recognised_exchange_tradable_derivative_liability_position",
		"9":"Fair_valued_balance_sheet_recognised_exchange_tradable_derivative_asset_position",
}

	TYP_EXCHNG_TRDBL_DRVTV_PSTN_RL = models.CharField("TYP_EXCHNG_TRDBL_DRVTV_PSTN_RL",max_length=255, choices=EXCHNG_TRDBL_DRVTV_PSTN_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="EXCHNG_TRDBL_DRVTV_PSTN_RL_TYP_INPT_domain")

	theEXCHNG_TRDBL_DRVTV_PSTN_RL = models.ForeignKey("EXCHNG_TRDBL_DRVTV_PSTN_RL", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_HDGD_EXCHNG_TRDBL_DRVTV_to_theEXCHNG_TRDBL_DRVTV_PSTN_RLs")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_HDGD_EXCHNG_TRDBL_DRVTV_to_theINSTRMNTs")

	class Meta:

		verbose_name = 'INSTRMNT_HDGD_EXCHNG_TRDBL_DRVTV'

		verbose_name_plural = 'INSTRMNT_HDGD_EXCHNG_TRDBL_DRVTVs'

class INSTRMNT_HDGD_OTC_DRVTV(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_HDGD_OTC_DRVTV_uniqueID = models.CharField("INSTRMNT_HDGD_OTC_DRVTV_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	OTC_DRVTV_ID = models.CharField("OTC_DRVTV_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_HDGD_OTC_DRVTV_to_theINSTRMNTs")

	theOTC_DRVTV_HDG = models.ForeignKey("OTC_DRVTV_HDG", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_HDGD_OTC_DRVTV_to_theOTC_DRVTV_HDGs")

	class Meta:

		verbose_name = 'INSTRMNT_HDGD_OTC_DRVTV'

		verbose_name_plural = 'INSTRMNT_HDGD_OTC_DRVTVs'

class INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNT_uniqueID = models.CharField("INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	PRTCTN_ARRNGMNT_RL_TYP_domain = {		"0":"Not_applicable",
		"1":"Protection_arrangement_received",
		"2":"Protection_arrangement_given",
}

	PRTCTN_ARRNGMNT_RL_TYP = models.CharField("PRTCTN_ARRNGMNT_RL_TYP",max_length=255, choices=PRTCTN_ARRNGMNT_RL_TYP_domain,default=None, blank=True, null=True, db_comment="PRTCTN_ARRNGMNT_RL_TYP_domain")

	PRTCTN_ID = models.CharField("PRTCTN_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNT_TYP_domain = {		"1":"Instrument_Protection_arrangement_received_assignment",
		"2":"Protection_arrangement_given_Instrument_assignment",
}

	INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNT_TYP = models.CharField("INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNT_TYP",max_length=255, choices=INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNT_TYP_domain")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNT_to_theINSTRMNTs")

	thePRTCTN_ARRNGMNT_RL = models.ForeignKey("PRTCTN_ARRNGMNT_RL", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNT_to_thePRTCTN_ARRNGMNT_RLs")

	class Meta:

		verbose_name = 'INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNT'

		verbose_name_plural = 'INSTRMNT_PRTCTN_ARRNGMNT_ASSGNMNTs'

class INSTRMNT_RL(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_RL_uniqueID = models.CharField("INSTRMNT_RL_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	INSTRMNT_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"12":"Non_balance_sheet_recognised_financial_liability_instrument",
		"34":"Balance_sheet_recognised_financial_asset_instrument_according_to_national_general_accepted_accounting_principles_nGAAP",
		"35":"Balance_sheet_recognised_financial_asset_instrument_according_to_International_Financial_Reporting_Standard_IFRS",
		"37":"Non_fair_valued_balance_sheet_recognised_financial_liability_instrument",
		"38":"Over_the_counter_OTC_Credit_default_swap_received_as_collateral_instrument",
		"39":"Other_collateral_received_instrument",
		"46":"Fair_valued_Balance_sheet_recognised_financial_liability_instrument_according_to_International_Financial_Reporting_Standard_IFRS",
		"47":"Fair_valued_balance_sheet_recognised_financial_liability_instrument_according_to_national_general_accepted_accounting_principles_nGAAP",
		"501":"Forborne_off_balance_sheet_item_given_instrument",
		"502":"Non_Forborne_off_balance_sheet_item_given_instrument",
		"6":"Off_balance_sheet_item_received_instrument",
		"8":"Collateral_given_instrument",
}

	TYP_INSTRMNT_RL = models.CharField("TYP_INSTRMNT_RL",max_length=255, choices=INSTRMNT_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="INSTRMNT_RL_TYP_INPT_domain")

	ACCMLTD_CHNG_NGTV = models.BigIntegerField("ACCMLTD_CHNG_NGTV",default=None, blank=True, null=True)

	ACCMLTD_CHNGS_FV = models.BigIntegerField("ACCMLTD_CHNGS_FV",default=None, blank=True, null=True)

	ACCMLTD_CHNGS_FV_CR = models.BigIntegerField("ACCMLTD_CHNGS_FV_CR",default=None, blank=True, null=True)

	ACCMLTD_IMPRMNT = models.BigIntegerField("ACCMLTD_IMPRMNT",default=None, blank=True, null=True)

	ACCMLTD_NGTV_VL_ADJSTMNT_CR = models.BigIntegerField("ACCMLTD_NGTV_VL_ADJSTMNT_CR",default=None, blank=True, null=True)

	ACCMLTD_NGTV_VL_ADJSTMNT_MR = models.BigIntegerField("ACCMLTD_NGTV_VL_ADJSTMNT_MR",default=None, blank=True, null=True)

	ACCMLTD_PRTL_WRTFFS = models.BigIntegerField("ACCMLTD_PRTL_WRTFFS",default=None, blank=True, null=True)

	ACCMLTD_TTL_WRTFFS = models.BigIntegerField("ACCMLTD_TTL_WRTFFS",default=None, blank=True, null=True)

	ACCMLTD_WRTFFS = models.BigIntegerField("ACCMLTD_WRTFFS",default=None, blank=True, null=True)

	ACCNTNG_CLSSFCTN_INPT_domain = {		"0":"Not_applicable",
		"14":"IFRS_Cash_balances_at_central_banks_and_other_demand_deposits_Cash_balances_at_central_banks_and_other_demand_deposits_in_accordance_with_IFRS",
		"2":"IFRS_Financial_assets_held_for_trading_Financial_assets_held_for_trading_in_accordance_with_IFRS",
		"21":"IFRS_Financial_liabilities_measured_at_amortised_cost_Financial_liabilities_measured_at_amortised_cost_in_accordance_with_IFRS",
		"23":"IFRS_Financial_liabilities_held_for_trading_Financial_liabilities_held_for_trading_in_accordance_with_IFRS",
		"25":"IFRS_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		"3":"nGAAP_Trading_Financial_assets_Trading_financial_assets_in_accordance_with_national_GAAP",
		"31":"nGAAP_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_accordance_with_national_GAAP_based_on_BAD",
		"33":"nGAAP_Trading_financial_liabilities_Trading_financial_liabilities_in_accordance_with_national_GAAP_based_on_BAD",
		"35":"nGAAP_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_nationa_GAAP_based_on_BAD",
		"4":"IFRS_Financial_assets_designated_at_fair_value_through_profit_or_loss_Financial_assets_measured_at_fair_value_through_profit_and_loss_and_designated_as_such_upon_initial_recognition_or_subsequently_in_accordance_with_IFRS_except_those_classified_as_financial_assets_held_for_trading",
		"41":"IFRS_Non_trading_financial_assets_mandatorily_at_fair_value_through_profit_or_loss_Non_trading_financial_assets_mandatorily_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		"45":"nGAAP_Cash_balances_at_central_banks_and_other_demand_deposits_Cash_balances_at_central_banks_and_other_demand_deposits_in_accordance_with_national_GAAP",
		"47":"nGAAP_Financial_assets_designated_at_fair_value_through_profit_or_loss_Financial_assets_designated_at_fair_value_through_profit_or_loss_in_accordance_with_national_GAAP",
		"6":"IFRS_Financial_assets_at_amortised_cost_Financial_assets_measured_at_amortised_cost_in_accordance_with_IFRS",
		"64":"nGAAP_financial_assets_at_fair_value_or_strict_LOCOM",
		"7":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_fair_value_through_profit_or_loss_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_in_accordance_with_national_GAAP",
		"711":"Accounting_portfolios_for_financial_assets_other_than_classified_as_held_for_sale_excluding_financial_assets_held_for_trading_trading_financial_assets_and_cash_and_cash_balances_at_central_banks_and_other_demand_deposits",
		"73":"nGAAP_Other_non_trading_non_derivative_financial_assets_LOCOM_nGAAP_Other_non_trading_non_derivative_financial_assets_at_LOCOM",
		"74":"nGAAP_Other_non_trading_non_derivative_financial_assets_Other_than_LOCOM",
		"76":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_LOCOM_nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_at_LOCOM",
		"77":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_Other_than_LOCOM",
		"8":"IFRS_Financial_assets_at_fair_value_through_other_comprehensive_income_Financial_assets_measured_at_fair_value_through_other_comprehensive_income_due_to_business_model_and_cash_flows_characteristics_in_accordance_with_IFRS",
		"83":"Investments_in_subsidiaries_joint_ventures_and_associates",
		"85":"nGAAP_Accounting_portfolios_for_trading_financial_instruments_Cost_based_method_or_LOCOM",
		"9":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_in_accordance_with_national_GAAP",
		"90":"Under_IFRS_9_impairment_Off_balance_sheet_accounting_classification_under_IFRS_9_impairment",
		"911":"Measured_under_IAS_37_Off_balance_sheet_accounting_classification_measured_under_IAS_37",
		"912":"Measured_under_IFRS_4_Off_balance_sheet_accounting_classification_measured_under_IFRS_4",
		"92":"Measured_at_fair_value_through_profit_or_loss_Off_balance_sheet_accounting_classification_IFRS_9_fair_valued_commitments_and_financial_guarantees",
		"93":"Under_nGAAP_Off_balance_sheet_accounting_classification_measured_under_nGAAP_based_on_BAD",
}

	ACCNTNG_CLSSFCTN = models.CharField("ACCNTNG_CLSSFCTN",max_length=255, choices=ACCNTNG_CLSSFCTN_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CLSSFCTN_INPT_domain")

	ACCRD_INTRST = models.BigIntegerField("ACCRD_INTRST",default=None, blank=True, null=True)

	ANNLSD_AGRD_RT = models.FloatField("ANNLSD_AGRD_RT",default=None, blank=True, null=True)

	DT_OPNNG_BLNC_F_24_01_INTL_RCGNTN_DT_REF_domain = {		"-1":"Any_date_Total",
		"2":"Current_reference_period_date",
}

	APPLCTN_FRBRNC_STTS_DT = models.CharField("APPLCTN_FRBRNC_STTS_DT",max_length=255, choices=DT_OPNNG_BLNC_F_24_01_INTL_RCGNTN_DT_REF_domain,default=None, blank=True, null=True, db_comment="DT_OPNNG_BLNC_F_24_01_INTL_RCGNTN_DT_REF_domain")

	ARRRS = models.BigIntegerField("ARRRS",default=None, blank=True, null=True)

	RSDL_MTRTY_BND_domain = {		"12":"_3m_6m",
		"16":"_6m_12m",
		"21":"_1y_2y",
		"28":"_2y_3y",
		"3":"_1d_1w",
		"31":"_3y_5y",
		"36":"_5y_10y",
		"40":"Over_10_years",
		"64":"_0d_1d",
		"81":"_gt_7_days_lt_eq_14_days",
		"82":"_gt_2_weeks_lt_eq_1_month",
		"9":"_1m_3m",
		"999":"Open_maturity",
}

	ASST_ENCMBRNC_RSDL_MTRTY_BND = models.CharField("ASST_ENCMBRNC_RSDL_MTRTY_BND",max_length=255, choices=RSDL_MTRTY_BND_domain,default=None, blank=True, null=True, db_comment="RSDL_MTRTY_BND_domain")

	ASST_ENCMBRNC_SRC_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Asset_encumbrance_source",
		"2":"Not_an_asset_encumbrance_source",
}

	ASST_ENCMBRNC_SRC_INDCTR = models.CharField("ASST_ENCMBRNC_SRC_INDCTR",max_length=255, choices=ASST_ENCMBRNC_SRC_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="ASST_ENCMBRNC_SRC_INDCTR_INPT_domain")

	AVLBL_ENCMBRNC_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Available_for_encumbrance",
		"2":"Not_available_for_encumbrance",
}

	AVLBL_ENCMBRNC_INDCTR = models.CharField("AVLBL_ENCMBRNC_INDCTR",max_length=255, choices=AVLBL_ENCMBRNC_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="AVLBL_ENCMBRNC_INDCTR_INPT_domain")

	BLNC_SHT_RCGNSD_FNCL_ASST_INSTRMNT_FR_VL_TYP = models.BooleanField("BLNC_SHT_RCGNSD_FNCL_ASST_INSTRMNT_FR_VL_TYP",default=None, blank=True, null=True)

	CLLTRL_INSTRMNT_RS_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Collateral_instrument_used_once",
		"2":"Collateral_instrument_reused",
}

	CLLTRL_INSTRMNT_RS_INDCTR = models.CharField("CLLTRL_INSTRMNT_RS_INDCTR",max_length=255, choices=CLLTRL_INSTRMNT_RS_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="CLLTRL_INSTRMNT_RS_INDCTR_INPT_domain")

	OBTND_CLLTRL_RCVD_INSTRMNT_TYP_INPT_domain = {		"0":"Not_applicable",
		"71":"Collateral_received_instrument_obtained_by_taking_possession",
		"72":"Not_obtained_collateral_received_instrument",
}

	CLLTRL_OBTND_RCVD_INSTRMNT_TYP = models.CharField("CLLTRL_OBTND_RCVD_INSTRMNT_TYP",max_length=255, choices=OBTND_CLLTRL_RCVD_INSTRMNT_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="OBTND_CLLTRL_RCVD_INSTRMNT_TYP_INPT_domain")

	CMLTV_RCVRS_SNC_DFLT = models.BigIntegerField("CMLTV_RCVRS_SNC_DFLT",default=None, blank=True, null=True)

	CMMTMNT_INCPTN = models.BigIntegerField("CMMTMNT_INCPTN",default=None, blank=True, null=True)

	CRRYNG_AMNT = models.BigIntegerField("CRRYNG_AMNT",default=None, blank=True, null=True)

	DBT_FNNCNG_ANCRDT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Debt_financing_according_to_AnaCredit",
		"2":"Not_debt_financing_according_to_AnaCredit",
}

	DBT_FNNCNG_RGLTN867_2016_INDCTR = models.CharField("DBT_FNNCNG_RGLTN867_2016_INDCTR",max_length=255, choices=DBT_FNNCNG_ANCRDT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="DBT_FNNCNG_ANCRDT_INDCTR_INPT_domain")

	DFLT_STTS_TYP_INPT_domain = {		"0":"Not_applicable",
		"18":"Default_because_both_unlikely_to_pay_and_more_than_90_180_days_past_due",
		"19":"Default_because_unlikely_to_pay",
		"20":"Default_because_more_than_90_180_days_past_due",
}

	DFLT_STTS = models.CharField("DFLT_STTS",max_length=255, choices=DFLT_STTS_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="DFLT_STTS_TYP_INPT_domain")

	DRVD_DFLT_STTS_domain = {		"14":"Not_in_default",
		"6":"Default",
}

	DFLT_STTS_DRVD = models.CharField("DFLT_STTS_DRVD",max_length=255, choices=DRVD_DFLT_STTS_domain,default=None, blank=True, null=True, db_comment="DRVD_DFLT_STTS_domain")

	DT_DFLT_STTS = models.DateTimeField("DT_DFLT_STTS",default=None, blank=True, null=True)

	DT_END_INTRST_ONLY = models.DateTimeField("DT_END_INTRST_ONLY",default=None, blank=True, null=True)

	DT_FRBRNC_MSRS = models.DateTimeField("DT_FRBRNC_MSRS",default=None, blank=True, null=True)

	DT_FRBRNC_STTS = models.DateTimeField("DT_FRBRNC_STTS",default=None, blank=True, null=True)

	DT_INCPTN = models.DateTimeField("DT_INCPTN",default=None, blank=True, null=True)

	DT_NN_PRFRMNG_STTS_INSTRMNT = models.DateTimeField("DT_NN_PRFRMNG_STTS_INSTRMNT",default=None, blank=True, null=True)

	DT_NXT_INTRST_RT_RST = models.DateTimeField("DT_NXT_INTRST_RT_RST",default=None, blank=True, null=True)

	DT_PST_D = models.DateTimeField("DT_PST_D",default=None, blank=True, null=True)

	DT_STTLMNT = models.DateTimeField("DT_STTLMNT",default=None, blank=True, null=True)

	ELGBL_GRNT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Not_eligible_as_guarantee",
		"2":"Eligible_as_guarantee",
}

	ELGBL_GRNT_INDCTR = models.CharField("ELGBL_GRNT_INDCTR",max_length=255, choices=ELGBL_GRNT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="ELGBL_GRNT_INDCTR_INPT_domain")

	ENCMBRD_ASST_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Not_encumbered_asset",
		"100":"Encumbered_asset",
}

	ENCMBRD_ASST_INDCTR = models.CharField("ENCMBRD_ASST_INDCTR",max_length=255, choices=ENCMBRD_ASST_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="ENCMBRD_ASST_INDCTR_INPT_domain")

	EXPSR_RCRS_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Recourse",
		"2":"No_recourse",
}

	EXPSR_RCRS_INDCTR = models.CharField("EXPSR_RCRS_INDCTR",max_length=255, choices=EXPSR_RCRS_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="EXPSR_RCRS_INDCTR_INPT_domain")

	FDCRY_INSTRMNT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Fiduciary_asset",
		"2":"Non_fiduciary_asset",
}

	FDCRY = models.CharField("FDCRY",max_length=255, choices=FDCRY_INSTRMNT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="FDCRY_INSTRMNT_INDCTR_INPT_domain")

	FNNCL_ASST_INSTRMNT_TYP_CRR_INPT_domain = {		"0":"Not_applicable",
		"24":"Performing_non_retail_exposure_class_financial_asset_instrument",
		"25":"Non_performing_non_retail_exposure_class_financial_asset_instrument",
		"28":"Default_financial_asset_instrument_individually_assessed",
		"30":"Performing_financial_asset_instrument_debtor_assessed",
		"31":"Non_performing_financial_asset_instrument_debtor_assessed",
		"32":"Performing_non_default_financial_asset_instrument_individually_assessed",
		"33":"Non_performing_non_default_financial_asset_instrument_individually_assessed",
}

	FNNCL_ASST_INSTRMNT_TYP_CRR_123 = models.CharField("FNNCL_ASST_INSTRMNT_TYP_CRR_123",max_length=255, choices=FNNCL_ASST_INSTRMNT_TYP_CRR_INPT_domain,default=None, blank=True, null=True, db_comment="FNNCL_ASST_INSTRMNT_TYP_CRR_INPT_domain")

	FNNCL_ASST_INSTRMNT_TYP_FXD_INTRST_RT_INPT_domain = {		"0":"Not_applicable",
		"18":"Fixed_interest_financial_asset_instrument",
		"19":"Non_fixed_interest_financial_asset_instrument",
}

	FNNCL_ASST_INSTRMNT_TYP_FXD_INTRST_RT = models.CharField("FNNCL_ASST_INSTRMNT_TYP_FXD_INTRST_RT",max_length=255, choices=FNNCL_ASST_INSTRMNT_TYP_FXD_INTRST_RT_INPT_domain,default=None, blank=True, null=True, db_comment="FNNCL_ASST_INSTRMNT_TYP_FXD_INTRST_RT_INPT_domain")

	FNNCL_ASST_INSTRMNT_TYP_INTRST_RT_INPT_domain = {		"0":"Not_applicable",
		"20":"Interest_only_financial_asset_instrument",
		"21":"Non_interest_only_financial_asset_instrument",
}

	FNNCL_ASST_INSTRMNT_TYP_INTRST_RT_ONL = models.CharField("FNNCL_ASST_INSTRMNT_TYP_INTRST_RT_ONL",max_length=255, choices=FNNCL_ASST_INSTRMNT_TYP_INTRST_RT_INPT_domain,default=None, blank=True, null=True, db_comment="FNNCL_ASST_INSTRMNT_TYP_INTRST_RT_INPT_domain")

	FNNCL_ASST_INSTRMNT_TYP_RNGTTN_STTS_INPT_domain = {		"0":"Not_applicable",
		"14":"Renegotiated_financial_asset_instrument_without_forbearance_measure",
		"15":"Renegotiated_financial_asset_instrument_with_forbearance_measure",
		"17":"Non_renegotiated_financial_asset_instrument",
}

	FNNCL_ASST_INSTRMNT_TYP_RNGTTN_STTS = models.CharField("FNNCL_ASST_INSTRMNT_TYP_RNGTTN_STTS",max_length=255, choices=FNNCL_ASST_INSTRMNT_TYP_RNGTTN_STTS_INPT_domain,default=None, blank=True, null=True, db_comment="FNNCL_ASST_INSTRMNT_TYP_RNGTTN_STTS_INPT_domain")

	FRBRNC_MSR_CNT = models.BigIntegerField("FRBRNC_MSR_CNT",default=None, blank=True, null=True)

	FRBRNC_MSR_TYP_domain = {		"0":"Not_applicable",
		"1":"Grace_period_payment_moratorium",
		"10":"Forborne_instruments_with_modified_interest_rate_below_market_conditions",
		"11":"Forborne_instruments_with_modified_interest_rate_not_below_market_conditions",
		"3":"Extension_of_maturity_term",
		"4":"Rescheduled_payments",
		"5":"Debt_forgiveness",
		"6":"Debt_asset_swaps",
		"7":"Other_forbearance_measures",
		"8":"Forborne_Refinanced_debt",
		"9":"Forborne_instruments_with_other_modified_terms_and_conditions",
}

	FRBRNC_MSR_TYP = models.CharField("FRBRNC_MSR_TYP",max_length=255, choices=FRBRNC_MSR_TYP_domain,default=None, blank=True, null=True, db_comment="FRBRNC_MSR_TYP_domain")

	FRZNG_PRD_DYS = models.BigIntegerField("FRZNG_PRD_DYS",default=None, blank=True, null=True)

	FV = models.BigIntegerField("FV",default=None, blank=True, null=True)

	FV_CHNG = models.BigIntegerField("FV_CHNG",default=None, blank=True, null=True)

	FV_CHNG_CR_BFR_PRCHS = models.BigIntegerField("FV_CHNG_CR_BFR_PRCHS",default=None, blank=True, null=True)

	FV_CHNGS_HDG_ACCNTNG = models.BigIntegerField("FV_CHNGS_HDG_ACCNTNG",default=None, blank=True, null=True)

	FV_HRRCHY_INPT_domain = {		"0":"Not_applicable",
		"1":"Level_1_Level_1_inputs_used_for_the_measurement_of_fair_value_Level_1_inputs_are_quoted_prices_in_active_markets_for_identical_assets_or_liabilities_that_the_entity_can_access_at_the_measurement_date",
		"2":"Level_2_Level_2_inputs_used_for_the_measurment_of_fair_value_Level_2_inputs_are_inputs_other_than_quoted_prices_included_within_Level_1_that_are_observable_for_the_asset_or_liability_either_directly_or_indirectly",
		"3":"Level_3_Level_3_inputs_used_for_the_measurment_of_fair_value_Level_3_inputs_are_unobservable_inputs_for_the_asset_or_liability",
}

	FV_HRRCHY = models.CharField("FV_HRRCHY",max_length=255, choices=FV_HRRCHY_INPT_domain,default=None, blank=True, null=True, db_comment="FV_HRRCHY_INPT_domain")

	FVO_DSGNTN_INPT_domain = {		"0":"Not_applicable",
		"2":"Management_on_a_fair_value_basis",
		"5":"Management_of_credit_risk_Upon_designation",
		"6":"Management_of_credit_risk_After_the_designation",
}

	FVO_DSGNTN = models.CharField("FVO_DSGNTN",max_length=255, choices=FVO_DSGNTN_INPT_domain,default=None, blank=True, null=True, db_comment="FVO_DSGNTN_INPT_domain")

	GCA_EXPSR_DRCGNSD_EXCHNG_CLLTRL = models.BigIntegerField("GCA_EXPSR_DRCGNSD_EXCHNG_CLLTRL",default=None, blank=True, null=True)

	GNRL_ALLWNCS_BNK_RSK = models.BigIntegerField("GNRL_ALLWNCS_BNK_RSK",default=None, blank=True, null=True)

	GNRL_ALLWNCS_CRDT_RSK = models.BigIntegerField("GNRL_ALLWNCS_CRDT_RSK",default=None, blank=True, null=True)	

	GRSS_CRRYNG_AMNT_E_INTRST = models.BigIntegerField("GRSS_CRRYNG_AMNT_E_INTRST",default=None, blank=True, null=True)

	HLD_SL_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Held_for_sale_The_member_indicates_that_the_instrument_is_held_for_sale",
		"2":"Not_held_for_sale_The_member_indicates_that_the_instrument_is_not_held_for_sale",
}

	HLD_SL_INDCTR = models.CharField("HLD_SL_INDCTR",max_length=255, choices=HLD_SL_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="HLD_SL_INDCTR_INPT_domain")

	HRCTS_TRDNG_PSTNS_FV = models.BigIntegerField("HRCTS_TRDNG_PSTNS_FV",default=None, blank=True, null=True)

	IMPRMNT_STTS_INPT_domain = {		"0":"Not_applicable",
		"211":"General_allowances_for_credit_risk_GAAP",
		"212":"General_allowances_for_banking_risk_GAAP",
		"23":"Stage_1_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_12_month_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"24":"Stage_2_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"25":"Stage_3_IFRS_To_be_used_if_the_instrument_is_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"26":"Specific_allowances_GAAP_To_be_used_if_the_instrument_is_subject_to_impairment_in_accordance_with_an_applied_accounting_standard_other_than_IFRS_9_and_specific_loss_allowances_are_raised_irrespective_of_whether_these_allowances_are_individually_or_collectively_assessed_impaired",
		"27":"Purchased_or_originated_credit_impaired_instruments_POCI_IFRS",
}

	IMPRMNT_STTS = models.CharField("IMPRMNT_STTS",max_length=255, choices=IMPRMNT_STTS_INPT_domain,default=None, blank=True, null=True, db_comment="IMPRMNT_STTS_INPT_domain")

	INTL_IMPRMNT_STTS_INPT_domain = {		"0":"Not_applicable",
		"23":"Stage_1_IFRS",
		"24":"Stage_2_IFRS",
		"25":"Stage_3_IFRS",
}

	INTL_IMPRMNT_STTS = models.CharField("INTL_IMPRMNT_STTS",max_length=255, choices=INTL_IMPRMNT_STTS_INPT_domain,default=None, blank=True, null=True, db_comment="INTL_IMPRMNT_STTS_INPT_domain")

	INTRST_RT_CP = models.FloatField("INTRST_RT_CP",default=None, blank=True, null=True)

	INTRST_RT_FLR = models.FloatField("INTRST_RT_FLR",default=None, blank=True, null=True)

	INTRST_RT_RST_FRQNCY_domain = {		"0":"Not_applicable",
		"1":"Annual",
		"12":"Other_than_overnight_monthly_quarterly_half_yearly_annually_or_at_creditor_discretion",
		"16":"Overnight",
		"18":"Quarterly",
		"19":"Semi_annually",
		"3":"At_creditor_discretion",
		"8":"Monthly",
}

	INTRST_RT_RST_FRQNCY = models.CharField("INTRST_RT_RST_FRQNCY",max_length=255, choices=INTRST_RT_RST_FRQNCY_domain,default=None, blank=True, null=True, db_comment="INTRST_RT_RST_FRQNCY_domain")

	INTRST_RT_SPRD = models.FloatField("INTRST_RT_SPRD",default=None, blank=True, null=True)

	LW_CRDT_RSK_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Low_credit_risk_instrument",
		"2":"Non_low_credit_risk_instrument",
}

	LW_CRDT_RSK_INDCTR = models.CharField("LW_CRDT_RSK_INDCTR",max_length=255, choices=LW_CRDT_RSK_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="LW_CRDT_RSK_INDCTR_INPT_domain")

	MLTPL_FRBRNC_MSR_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Multiple_forbearance_measures_in_place",
		"2":"Not_multiple_forbearance_measures_in_place",
}

	MLTPL_FRBRNC_MSRS_INDCTR = models.CharField("MLTPL_FRBRNC_MSRS_INDCTR",max_length=255, choices=MLTPL_FRBRNC_MSR_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="MLTPL_FRBRNC_MSR_INDCTR_INPT_domain")

	NN_PRFRMNG_EXT_CRTR_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Failed_to_meet_the_non_performing_exit_criteria",
		"2":"Still_able_to_meet_the_non_performing_exit_criteria",
}

	NN_PRFRMNG_EXT_CRTR_MT_INDCTR = models.CharField("NN_PRFRMNG_EXT_CRTR_MT_INDCTR",max_length=255, choices=NN_PRFRMNG_EXT_CRTR_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="NN_PRFRMNG_EXT_CRTR_INDCTR_INPT_domain")

	NN_PRFRMNG_PRR_FRBRNC_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Non_performing_prior_to_forbearance",
		"2":"Not_non_performing_prior_to_forbearance",
}

	NN_PRFRMNG_PRR_FRBRNC_INDCTR = models.CharField("NN_PRFRMNG_PRR_FRBRNC_INDCTR",max_length=255, choices=NN_PRFRMNG_PRR_FRBRNC_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="NN_PRFRMNG_PRR_FRBRNC_INDCTR_INPT_domain")

	PRDNTL_PRTFL_domain = {		"1":"Trading_book",
		"2":"Non_trading_book",
}

	PRDNTL_PRTFL_TYP = models.CharField("PRDNTL_PRTFL_TYP",max_length=255, choices=PRDNTL_PRTFL_domain,default=None, blank=True, null=True, db_comment="PRDNTL_PRTFL_domain")

	P_FRBRN_EXPSR_PRBTN_RCLD_NP_INPT_domain = {		"0":"Not_applicable",
		"1":"Performing_forborne_exposure_under_probation",
		"2":"Performing_forborne_exposure_not_under_probation",
}

	PRFRMNG_FRBRN_EXPSR_UNDR_PRBTN_RCLSSFD_NN_PRFRMNG_INDCTR = models.CharField("PRFRMNG_FRBRN_EXPSR_UNDR_PRBTN_RCLSSFD_NN_PRFRMNG_INDCTR",max_length=255, choices=P_FRBRN_EXPSR_PRBTN_RCLD_NP_INPT_domain,default=None, blank=True, null=True, db_comment="P_FRBRN_EXPSR_PRBTN_RCLD_NP_INPT_domain")

	PRFRMNG_STTS_INPT_domain = {		"0":"Not_applicable",
		"1":"Non_performing",
		"11":"Performing",
}

	PRFRMNG_STTS = models.CharField("PRFRMNG_STTS",max_length=255, choices=PRFRMNG_STTS_INPT_domain,default=None, blank=True, null=True, db_comment="PRFRMNG_STTS_INPT_domain")

	PRFRMNG_STTS_RSN_INPT_domain = {		"0":"Not_applicable",
		"1":"Failed_reclassification_to_performing_at_end_of_probation_period",
		"2":"Exited_from_NPE_in_the_last_12_months",
}

	PRFRMNG_STTS_RSN = models.CharField("PRFRMNG_STTS_RSN",max_length=255, choices=PRFRMNG_STTS_RSN_INPT_domain,default=None, blank=True, null=True, db_comment="PRFRMNG_STTS_RSN_INPT_domain")

	PRJCT_FNNC_LN_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Project_finance_loan",
		"2":"Non_project_finance_loan",
}

	PRJCT_FNNC_LN = models.CharField("PRJCT_FNNC_LN",max_length=255, choices=PRJCT_FNNC_LN_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="PRJCT_FNNC_LN_INDCTR_INPT_domain")

	PRPS_INPT_domain = {		"0":"Not_applicable",
		"1":"Credit_for_consumption_Credit_for_consumption_a_loan_granted_predominantly_for_the_purpose_of_personal_consumption_of_goods_and_services_in_accordance_with_Part_2_of_Annex_II_of_Regulation_EU_No_1071_2013_ECB_2013_33",
		"12":"Residential_real_estate_purchase_Financing_of_residential_property_Residential_property_is_defined_in_Article_4_1_75_of_Regulation_EU_No_575_2013",
		"13":"Commercial_real_estate_purchase_Financing_of_real_estate_property_other_than_residential_property",
		"19":"Other_purposes_Purposes_other_than_consumption_residential_and_commercial_real_estate_purchase_margin_lending_imports_exports_construction_investment_and_working_capital_facility",
		"4":"Margin_lending_Instruments_in_which_an_institution_extends_credit_in_connection_with_the_purchase_sale_carrying_or_trading_of_securities_Margin_lending_instruments_do_not_include_other_loans_that_are_secured_by_collateral_in_the_form_of_securities",
		"6":"Imports_Financing_of_goods_and_services_purchases_barter_and_or_gifts_from_non_residents_to_residents",
		"7":"Exports_Financing_of_goods_and_services_sales_barter_and_or_gifts_from_residents_to_non_residents",
		"8":"Construction_investment_Financing_of_construction_of_buildings_infrastructure_and_industrial_facilities",
		"9":"Working_capital_facility_Financing_the_cash_flow_management_of_an_organisation",
}

	PRPS = models.CharField("PRPS",max_length=255, choices=PRPS_INPT_domain,default=None, blank=True, null=True, db_comment="PRPS_INPT_domain")

	PRVSNS_OFF_BLNC_SHT = models.BigIntegerField("PRVSNS_OFF_BLNC_SHT",default=None, blank=True, null=True)

	PST_DU_FNNCL_ASST_INSTRMNT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"48":"Past_due_financial_asset_instrument",
		"49":"Not_past_due_financial_asset_instrument",
}

	PST_DU_FNNCL_ASST_INSTRMNT_INDCTR = models.CharField("PST_DU_FNNCL_ASST_INSTRMNT_INDCTR",max_length=255, choices=PST_DU_FNNCL_ASST_INSTRMNT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="PST_DU_FNNCL_ASST_INSTRMNT_INDCTR_INPT_domain")

	FRQNCY_PYMNT_INPT_domain = {		"0":"Not_applicable",
		"1":"Annual",
		"15":"Other_than_monthly_quarterly_half_yearly_annually_bullet_or_zero_coupon",
		"18":"Quarterly",
		"19":"Semi_annually",
		"22":"Zero_coupon_Amortisation_in_which_the_full_principal_amount_and_interest_is_repaid_in_the_last_instalment",
		"4":"Bullet_Amortisation_in_which_the_full_principal_amount_is_repaid_in_the_last_instalment_regardless_of_the_interest_payment_frequency",
		"8":"Monthly",
}

	PYMNT_FRQNCY = models.CharField("PYMNT_FRQNCY",max_length=255, choices=FRQNCY_PYMNT_INPT_domain,default=None, blank=True, null=True, db_comment="FRQNCY_PYMNT_INPT_domain")

	RCGNTN_STTS = models.BooleanField("RCGNTN_STTS",default=None, blank=True, null=True)

	RFRNC_RT_INPT_domain = {		"0":"Not_applicable",
		"10":"EURIBOR_1W",
		"100":"EURIBOR_8M",
		"101":"USD_LIBOR_8M",
		"102":"GBP_LIBOR_8M",
		"103":"EUR_LIBOR_8M",
		"104":"JPY_LIBOR_8M",
		"105":"CHF_LIBOR_8M",
		"106":"MIBOR_8M",
		"107":"other_single_reference_rate_8M",
		"108":"multiple_reference_rates_8M",
		"109":"EURIBOR_9M",
		"11":"USD_LIBOR_1W",
		"110":"USD_LIBOR_9M",
		"111":"GBP_LIBOR_9M",
		"112":"EUR_LIBOR_9M",
		"113":"JPY_LIBOR_9M",
		"114":"CHF_LIBOR_9M",
		"115":"MIBOR_9M",
		"116":"other_single_reference_rate_9M",
		"117":"multiple_reference_rates_9M",
		"118":"EURIBOR_10M",
		"119":"USD_LIBOR_10M",
		"12":"GBP_LIBOR_1W",
		"120":"GBP_LIBOR_10M",
		"121":"EUR_LIBOR_10M",
		"122":"JPY_LIBOR_10M",
		"123":"CHF_LIBOR_10M",
		"124":"MIBOR_10M",
		"125":"other_single_reference_rate_10M",
		"126":"multiple_reference_rates_10M",
		"127":"EURIBOR_11M",
		"128":"USD_LIBOR_11M",
		"129":"GBP_LIBOR_11M",
		"13":"EUR_LIBOR_1W",
		"130":"EUR_LIBOR_11M",
		"131":"JPY_LIBOR_11M",
		"132":"CHF_LIBOR_11M",
		"133":"MIBOR_11M",
		"134":"other_single_reference_rate_11M",
		"135":"multiple_reference_rates_11M",
		"136":"EURIBOR_12M",
		"137":"USD_LIBOR_12M",
		"138":"GBP_LIBOR_12M",
		"139":"EUR_LIBOR_12M",
		"14":"JPY_LIBOR_1W",
		"140":"JPY_LIBOR_12M",
		"141":"CHF_LIBOR_12M",
		"142":"MIBOR_12M",
		"143":"other_single_reference_rate_12M",
		"144":"multiple_reference_rates_12M",
		"145":"EONIA",
		"15":"CHF_LIBOR_1W",
		"16":"MIBOR_1W",
		"17":"other_single_reference_rate_1W",
		"18":"multiple_reference_rates_1W",
		"19":"EURIBOR_2W",
		"2":"USD_LIBOR_ON",
		"20":"USD_LIBOR_2W",
		"21":"GBP_LIBOR_2W",
		"22":"EUR_LIBOR_2W",
		"23":"JPY_LIBOR_2W",
		"24":"CHF_LIBOR_2W",
		"25":"MIBOR_2W",
		"26":"other_single_reference_rate_2W",
		"27":"multiple_reference_rates_2W",
		"28":"EURIBOR_3W",
		"29":"USD_LIBOR_3W",
		"3":"GBP_LIBOR_ON",
		"30":"GBP_LIBOR_3W",
		"31":"EUR_LIBOR_3W",
		"32":"JPY_LIBOR_3W",
		"33":"CHF_LIBOR_3W",
		"34":"MIBOR_3W",
		"35":"other_single_reference_rate_3W",
		"36":"multiple_reference_rates_3W",
		"37":"EURIBOR_1M",
		"38":"USD_LIBOR_1M",
		"39":"GBP_LIBOR_1M",
		"4":"EUR_LIBOR_ON",
		"40":"EUR_LIBOR_1M",
		"41":"JPY_LIBOR_1M",
		"42":"CHF_LIBOR_1M",
		"43":"MIBOR_1M",
		"44":"other_single_reference_rate_1M",
		"45":"multiple_reference_rates_1M",
		"46":"EURIBOR_2M",
		"47":"USD_LIBOR_2M",
		"48":"GBP_LIBOR_2M",
		"49":"EUR_LIBOR_2M",
		"5":"JPY_LIBOR_ON",
		"50":"JPY_LIBOR_2M",
		"51":"CHF_LIBOR_2M",
		"52":"MIBOR_2M",
		"53":"other_single_reference_rate_2M",
		"54":"multiple_reference_rates_2M",
		"55":"EURIBOR_3M",
		"56":"USD_LIBOR_3M",
		"57":"GBP_LIBOR_3M",
		"58":"EUR_LIBOR_3M",
		"59":"JPY_LIBOR_3M",
		"6":"CHF_LIBOR_ON",
		"60":"CHF_LIBOR_3M",
		"61":"MIBOR_3M",
		"62":"other_single_reference_rate_3M",
		"63":"multiple_reference_rates_3M",
		"64":"EURIBOR_4M",
		"65":"USD_LIBOR_4M",
		"66":"GBP_LIBOR_4M",
		"67":"EUR_LIBOR_4M",
		"68":"JPY_LIBOR_4M",
		"69":"CHF_LIBOR_4M",
		"7":"MIBOR_ON",
		"70":"MIBOR_4M",
		"71":"other_single_reference_rate_4M",
		"72":"multiple_reference_rates_4M",
		"73":"EURIBOR_5M",
		"74":"USD_LIBOR_5M",
		"75":"GBP_LIBOR_5M",
		"76":"EUR_LIBOR_5M",
		"77":"JPY_LIBOR_5M",
		"78":"CHF_LIBOR_5M",
		"79":"MIBOR_5M",
		"8":"other_single_reference_rate_ON",
		"80":"other_single_reference_rate_5M",
		"81":"multiple_reference_rates_5M",
		"82":"EURIBOR_6M",
		"83":"USD_LIBOR_6M",
		"84":"GBP_LIBOR_6M",
		"85":"EUR_LIBOR_6M",
		"86":"JPY_LIBOR_6M",
		"87":"CHF_LIBOR_6M",
		"88":"MIBOR_6M",
		"89":"other_single_reference_rate_6M",
		"9":"multiple_reference_rates_ON",
		"90":"multiple_reference_rates_6M",
		"91":"EURIBOR_7M",
		"92":"USD_LIBOR_7M",
		"93":"GBP_LIBOR_7M",
		"94":"EUR_LIBOR_7M",
		"95":"JPY_LIBOR_7M",
		"96":"CHF_LIBOR_7M",
		"97":"MIBOR_7M",
		"98":"other_single_reference_rate_7M",
		"99":"multiple_reference_rates_7M",
}

	RFRNC_RT = models.CharField("RFRNC_RT",max_length=255, choices=RFRNC_RT_INPT_domain,default=None, blank=True, null=True, db_comment="RFRNC_RT_INPT_domain")

	SBJCT_IMPRMNT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Subject_to_impairment",
		"2":"Not_subject_to_impairment",
}

	SBJCT_IMPRMNT_INDCTR = models.CharField("SBJCT_IMPRMNT_INDCTR",max_length=255, choices=SBJCT_IMPRMNT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="SBJCT_IMPRMNT_INDCTR_INPT_domain")

	SBRDNTD_DBT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Subordinated_debt",
		"2":"Not_subordinated_debt",
}

	SBRDNTD_DBT = models.CharField("SBRDNTD_DBT",max_length=255, choices=SBRDNTD_DBT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="SBRDNTD_DBT_INDCTR_INPT_domain")

	STRT_DT_PRD = models.DateTimeField("STRT_DT_PRD",default=None, blank=True, null=True)

	TKN_PSSSSN_DT = models.DateTimeField("TKN_PSSSSN_DT",default=None, blank=True, null=True)

	TM_PST_DU_BND_domain = {		"1002":"_0_days",
		"12":"_gt_3_months_lt_eq_6_months",
		"16":"_gt_6_months_lt_eq_12_months",
		"21":"_gt_1_year_lt_eq_2_years",
		"29":"_gt_2_years_lt_eq_5_years",
		"75":"_gt_eq_1_day_lt_eq_30_days",
		"84":"_gt_5_year_lt_eq_7_years",
		"85":"_gt_7_years",
		"9":"_gt_30_days_lt_eq_90_days",
}

	TM_PST_DU_BND = models.CharField("TM_PST_DU_BND",max_length=255, choices=TM_PST_DU_BND_domain,default=None, blank=True, null=True, db_comment="TM_PST_DU_BND_domain")

	TM_SNC_INTL_RCGNTN_domain = {		"27":"_lt_eq_2_years",
		"29":"_gt_2_years_lt_eq_5_years",
		"37":"_gt_5_years",
}

	TM_SNC_INTL_RCGNTN = models.CharField("TM_SNC_INTL_RCGNTN",max_length=255, choices=TM_SNC_INTL_RCGNTN_domain,default=None, blank=True, null=True, db_comment="TM_SNC_INTL_RCGNTN_domain")

	TRNSFR_IMPRMNT_STGS_F_12_02_TRNSFR_IMPRMNT_STGS_REF_domain = {		"1":"To_stage_1_from_stage_2",
		"2":"To_stage_1_from_stage_3",
		"3":"To_stage_2_from_stage_1",
		"4":"To_stage_2_from_stage_3",
		"5":"To_stage_3_from_stage_1",
		"6":"To_stage_3_from_stage_2",
}

	TRNSFR_IMPRMNT_STGS = models.CharField("TRNSFR_IMPRMNT_STGS",max_length=255, choices=TRNSFR_IMPRMNT_STGS_F_12_02_TRNSFR_IMPRMNT_STGS_REF_domain,default=None, blank=True, null=True, db_comment="TRNSFR_IMPRMNT_STGS_F_12_02_TRNSFR_IMPRMNT_STGS_REF_domain")

	TYP_AMRTSTN_INPT_domain = {		"0":"Not_applicable",
		"1":"French_Amortisation_in_which_the_total_amount_principal_plus_interest_repaid_in_each_instalment_is_the_same",
		"2":"German_Amortisation_in_which_the_first_instalment_is_interest_only_and_the_remaining_instalments_are_constant_including_capital_amortisation_and_interest",
		"3":"Fixed_amortisation_schedule_Amortisation_in_which_the_principal_amount_repaid_in_each_instalment_is_the_same",
		"4":"Bullet_Amortisation_in_which_the_full_principal_amount_is_repaid_in_the_last_instalment",
		"5":"Amortisation_types_other_than_French_German_Fixed_amortisation_schedule_or_bullet_Other_amortisation_schedule_applied_than_the_ones_specified",
}

	TYP_AMRTSTN = models.CharField("TYP_AMRTSTN",max_length=255, choices=TYP_AMRTSTN_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_AMRTSTN_INPT_domain")

	TYP_INTRST_RT_INPT_domain = {		"0":"Not_applicable",
		"1":"Fixed_Scheme_defining_the_interest_rates_during_the_life_of_the_exposure_which_only_includes_constant_rates_numeric_constant_rate_known_with_certainty_at_the_inception_of_the_exposure_and_where_the_interest_rates_apply_to_the_whole_exposure_The_scheme_may_contain_more_than_one_constant_interest_rate_to_be_applied_at_different_periods_during_the_life_of_the_exposure_e_g_loan_with_a_constant_interest_rate_during_the_initial_fixed_rate_period_which_then_changes_to_a_different_interest_rate_which_is_still_constant_and_which_was_known_at_the_inception_of_the_exposure",
		"2":"Variable_Scheme_defining_the_interest_rates_during_the_life_of_the_exposure_which_only_includes_interest_rates_based_on_the_evolution_of_another_variable_the_reference_variable_and_where_the_interest_rate_applies_to_the_whole_exposure",
		"3":"Mixed_Interest_rate_class_other_than_fixed_or_variable",
}

	TYP_INTRST_RT = models.CharField("TYP_INTRST_RT",max_length=255, choices=TYP_INTRST_RT_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_INTRST_RT_INPT_domain")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="INSTRMNT_RL_to_theINSTRMNTs")

	@property
	@lineage(dependencies={"INSTRMNT_RL.PRFRMNG_STTS",
		"INSTRMNT_RL.ACCNTNG_CLSSFCTN",
		"INSTRMNT_RL.ACCMLTD_IMPRMNT",
		"INSTRMNT_RL.CRRYNG_AMNT",
		"INSTRMNT_RL.IMPRMNT_STTS",
		"INSTRMNT_RL.BLNC_SHT_RCGNSD_FNCL_ASST_INSTRMNT_FR_VL_TYP",
		"INSTRMNT_RL.ACCMLTD_CHNGS_FV",
		"INSTRMNT_RL.FV",
		"INSTRMNT_RL.GNRL_ALLWNCS_BNK_RSK",
		"INSTRMNT_RL.GNRL_ALLWNCS_CRDT_RSK",
		"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def GRSS_CRRYNG_AMNT(self):
		accntng_clssfctn = None
		accmltd_imprmnt = 0
		accmltd_chngs_fv_cr = 0
		crryng_amnt  = 0 			
		fv = 0
		gnrl_allwncs_bnk_rsk = 0
		gnrl_allwncs_crdt_rsk = 0
		prfrmng_stts = self.PRFRMNG_STTS
		imprmnt_stts = self.IMPRMNT_STTS
		sbjct_imprmnt_idctr = self.SBJCT_IMPRMNT_INDCTR


		# "10":"Non_balance_sheet_recognised_financial_asset_instrument",
		# "34":"Balance_sheet_recognised_financial_asset_instrument_according_to_national_general_accepted_accounting_principles_nGAAP",
		# "35":"Balance_sheet_recognised_financial_asset_instrument_according_to_International_Financial_Reporting_Standard_IFRS",

		if (self.TYP_INSTRMNT_RL == '10') or \
			(self.TYP_INSTRMNT_RL == '34') or \
			(self.TYP_INSTRMNT_RL == '35'):
			accntng_clssfctn = self.ACCNTNG_CLSSFCTN
			accmltd_imprmnt = self.ACCMLTD_IMPRMNT
			crryng_amnt  = self.CRRYNG_AMNT
			imprmnt_stts = self.IMPRMNT_STTS
	 			
	 	# for some reason 	BLNC_SHT_RCGNSD_FNCL_ASST_INSTRMNT_FR_VL_TYP is a boolean, 
		# and we would expect it to be a domain with 2 members, need to investigate this.
		# 	
		if (self.BLNC_SHT_RCGNSD_FNCL_ASST_INSTRMNT_FR_VL_TYP):
			accmltd_chngs_fv_cr = self.ACCMLTD_CHNGS_FV
			fv = self.FV 

		if (self.TYP_INSTRMNT_RL == '34'):	 		
			gnrl_allwncs_bnk_rsk = self.GNRL_ALLWNCS_BNK_RSK
			gnrl_allwncs_crdt_rsk = self.GNRL_ALLWNCS_CRDT_RSK


		return_grss_crryng_amnt = 0
		# ACCNTNG_CLSSFCTN_INPT_domain = {		"0":"Not_applicable",
		# "14":"IFRS_Cash_balances_at_central_banks_and_other_demand_deposits_Cash_balances_at_central_banks_and_other_demand_deposits_in_accordance_with_IFRS",
		# "2":"IFRS_Financial_assets_held_for_trading_Financial_assets_held_for_trading_in_accordance_with_IFRS",
		# "21":"IFRS_Financial_liabilities_measured_at_amortised_cost_Financial_liabilities_measured_at_amortised_cost_in_accordance_with_IFRS",
		# "23":"IFRS_Financial_liabilities_held_for_trading_Financial_liabilities_held_for_trading_in_accordance_with_IFRS",
		# "25":"IFRS_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		# "3":"nGAAP_Trading_Financial_assets_Trading_financial_assets_in_accordance_with_national_GAAP",
		# "31":"nGAAP_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_Non_trading_non_derivative_financial_liabilities_measured_at_a_cost_based_method_accordance_with_national_GAAP_based_on_BAD",
		# "33":"nGAAP_Trading_financial_liabilities_Trading_financial_liabilities_in_accordance_with_national_GAAP_based_on_BAD",
		# "35":"nGAAP_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_Financial_liabilities_designated_at_fair_value_through_profit_or_loss_in_accordance_with_nationa_GAAP_based_on_BAD",
		# "4":"IFRS_Financial_assets_designated_at_fair_value_through_profit_or_loss_Financial_assets_measured_at_fair_value_through_profit_and_loss_and_designated_as_such_upon_initial_recognition_or_subsequently_in_accordance_with_IFRS_except_those_classified_as_financial_assets_held_for_trading",
		# "41":"IFRS_Non_trading_financial_assets_mandatorily_at_fair_value_through_profit_or_loss_Non_trading_financial_assets_mandatorily_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		# "45":"nGAAP_Cash_balances_at_central_banks_and_other_demand_deposits_Cash_balances_at_central_banks_and_other_demand_deposits_in_accordance_with_national_GAAP",
		# "47":"nGAAP_Financial_assets_designated_at_fair_value_through_profit_or_loss_Financial_assets_designated_at_fair_value_through_profit_or_loss_in_accordance_with_national_GAAP",
		# "6":"IFRS_Financial_assets_at_amortised_cost_Financial_assets_measured_at_amortised_cost_in_accordance_with_IFRS",
		# "64":"nGAAP_financial_assets_at_fair_value_or_strict_LOCOM",
		# "7":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_fair_value_through_profit_or_loss_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_in_accordance_with_national_GAAP",
		# "711":"Accounting_portfolios_for_financial_assets_other_than_classified_as_held_for_sale_excluding_financial_assets_held_for_trading_trading_financial_assets_and_cash_and_cash_balances_at_central_banks_and_other_demand_deposits",
		# "73":"nGAAP_Other_non_trading_non_derivative_financial_assets_LOCOM_nGAAP_Other_non_trading_non_derivative_financial_assets_at_LOCOM",
		# "74":"nGAAP_Other_non_trading_non_derivative_financial_assets_Other_than_LOCOM",
		# "76":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_LOCOM_nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_at_LOCOM",
		# "77":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_Other_than_LOCOM",
		# "8":"IFRS_Financial_assets_at_fair_value_through_other_comprehensive_income_Financial_assets_measured_at_fair_value_through_other_comprehensive_income_due_to_business_model_and_cash_flows_characteristics_in_accordance_with_IFRS",
		# "83":"Investments_in_subsidiaries_joint_ventures_and_associates",
		# "85":"nGAAP_Accounting_portfolios_for_trading_financial_instruments_Cost_based_method_or_LOCOM",
		# "9":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_in_accordance_with_national_GAAP",
		# "90":"Under_IFRS_9_impairment_Off_balance_sheet_accounting_classification_under_IFRS_9_impairment",
		# "911":"Measured_under_IAS_37_Off_balance_sheet_accounting_classification_measured_under_IAS_37",
		# "912":"Measured_under_IFRS_4_Off_balance_sheet_accounting_classification_measured_under_IFRS_4",
		# "92":"Measured_at_fair_value_through_profit_or_loss_Off_balance_sheet_accounting_classification_IFRS_9_fair_valued_commitments_and_financial_guarantees",
		# "93":"Under_nGAAP_Off_balance_sheet_accounting_classification_measured_under_nGAAP_based_on_BAD",

		match accntng_clssfctn:
			case '4' | \
	 			 '41' | \
	 			 '47' | \
	 			 '7' :
				  
				# PRFRMNG_STTS_INPT_domain = {		"0":"Not_applicable",
				# "1":"Non_performing",
				# "11":"Performing",
				# }
				match prfrmng_stts:
					case '11':
						return_grss_crryng_amnt = fv
					case '1':
						return_grss_crryng_amnt = fv + accmltd_chngs_fv_cr
					case _ : return_grss_crryng_amnt = 0

			case ('6' | '8' | '9'):
				return_grss_crryng_amnt = crryng_amnt - accmltd_imprmnt
			case ('77'):
				# IMPRMNT_STTS_domain = {		"211":"General_allowances_for_credit_risk_GAAP",
				# "212":"General_allowances_for_banking_risk_GAAP",
				# "23":"Stage_1_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_12_month_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
				# "24":"Stage_2_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
				# "25":"Stage_3_IFRS_To_be_used_if_the_instrument_is_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
				# "26":"Specific_allowances_GAAP_To_be_used_if_the_instrument_is_subject_to_impairment_in_accordance_with_an_applied_accounting_standard_other_than_IFRS_9_and_specific_loss_allowances_are_raised_irrespective_of_whether_these_allowances_are_individually_or_collectively_assessed_impaired",
				# "27":"Purchased_or_originated_credit_impaired_instruments_POCI_IFRS",
				match imprmnt_stts:
					case '26' :
						return_grss_crryng_amnt = crryng_amnt - accmltd_imprmnt
					case '211':
						return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_crdt_rsk
					case '212':
						return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_bnk_rsk
					case _ : 
						return_grss_crryng_amnt = 0
	 			
	 			
			case ('9'):
				match sbjct_imprmnt_idctr:
					#	SBJCT_IMPRMNT_INDCTR_INPT_domain = {		"0":"Not_applicable",
					# "1":"Subject_to_impairment",
					# "2":"Not_subject_to_impairment",
					case '1':
						match prfrmng_stts:
							case '26':
								return_grss_crryng_amnt = crryng_amnt - accmltd_imprmnt
							case '211':
								return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_crdt_rsk
							case '212':
								return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_bnk_rsk
							case _ : 
								return_grss_crryng_amnt = 0

					case '2':
						match prfrmng_stts:
							case '11':
								return_grss_crryng_amnt = fv
							case '1':
								return_grss_crryng_amnt = fv + accmltd_chngs_fv_cr
							case _ : 
								return_grss_crryng_amnt = 0
					case _ : 
						return_grss_crryng_amnt = 0
			 			
			 		
			case ('76' | '73'):	
				return_grss_crryng_amnt = crryng_amnt
			case '74':		
				return_grss_crryng_amnt = crryng_amnt + accmltd_imprmnt
			case ('2' | '3') :
				return_grss_crryng_amnt = fv
			case _ : 
				return_grss_crryng_amnt = 0		
	 				
		return return_grss_crryng_amnt

	class Meta:

		verbose_name = 'INSTRMNT_RL'

		verbose_name_plural = 'INSTRMNT_RLs'

class INTRNL_GRP_RL(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	INTRNL_GRP_RL_uniqueID = models.CharField("INTRNL_GRP_RL_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	GRP_ID = models.CharField("GRP_ID",max_length=255,default=None, blank=True, null=True)

	GRP_RL_TYP_domain = {		"1":"Reporting_agent_group",
}

	GRP_RL_TYP = models.CharField("GRP_RL_TYP",max_length=255, choices=GRP_RL_TYP_domain,default=None, blank=True, null=True, db_comment="GRP_RL_TYP_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ACCNTNG_FRMWRK_domain = {		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD_CNLDTD_RPRTNG = models.CharField("ACCNTNG_STNDRD_CNLDTD_RPRTNG",max_length=255, choices=ACCNTNG_FRMWRK_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_domain")

	ACCNTNG_FRMWRK_domain = {		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD_SOLO_RPRTNG = models.CharField("ACCNTNG_STNDRD_SOLO_RPRTNG",max_length=255, choices=ACCNTNG_FRMWRK_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_domain")

	ACCNTNG_FRMWRK_domain = {		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD_STTSTCL_RPRTNG = models.CharField("ACCNTNG_STNDRD_STTSTCL_RPRTNG",max_length=255, choices=ACCNTNG_FRMWRK_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_domain")

	theGRP = models.ForeignKey("GRP", models.SET_NULL,blank=True,null=True,related_name="INTRNL_GRP_RL_to_theGRPs")

	class Meta:

		verbose_name = 'INTRNL_GRP_RL'

		verbose_name_plural = 'INTRNL_GRP_RLs'

class INTRST_RT_RSK_HDG_PRTFL(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	INTRST_RT_RSK_HDG_PRTFL_uniqueID = models.CharField("INTRST_RT_RSK_HDG_PRTFL_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	ACCNTNG_FRMWRK_domain = {		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_domain")

	DMSTC_ACTVT_INDCTR_domain = {		"1":"_Domestic_activities",
		"2":"Non_Domestic_activities",
}

	DMSTC_ACTVT_INDCTR = models.CharField("DMSTC_ACTVT_INDCTR",max_length=255, choices=DMSTC_ACTVT_INDCTR_domain,default=None, blank=True, null=True, db_comment="DMSTC_ACTVT_INDCTR_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	HDGD_PRTFL_ASST_LBLTY_INDCTR_domain = {		"1":"Hedged_portfolio_assets",
		"2":"Hedged_portfolio_liabilities",
}

	HDGD_PRTFL_ASST_LBLTY_INDCTR = models.CharField("HDGD_PRTFL_ASST_LBLTY_INDCTR",max_length=255, choices=HDGD_PRTFL_ASST_LBLTY_INDCTR_domain,default=None, blank=True, null=True, db_comment="HDGD_PRTFL_ASST_LBLTY_INDCTR_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	HDGD_ITMS_FV_CHNGS = models.BigIntegerField("HDGD_ITMS_FV_CHNGS",default=None, blank=True, null=True)

	class Meta:

		verbose_name = 'INTRST_RT_RSK_HDG_PRTFL'

		verbose_name_plural = 'INTRST_RT_RSK_HDG_PRTFLs'

class KB_PR_BCKT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	KB_PR_BCKT_uniqueID = models.CharField("KB_PR_BCKT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	ACCNTNG_FRMWRK_domain = {		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_domain")

	BCKT_ID = models.CharField("BCKT_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	GIRR_DLTA_RSK_PSTN = models.BigIntegerField("GIRR_DLTA_RSK_PSTN",default=None, blank=True, null=True)

	class Meta:

		verbose_name = 'KB_PR_BCKT'

		verbose_name_plural = 'KB_PR_BCKTs'

class LN_EXCLDNG_RPRCHS_AGRMNT_AND_ADVNC_HDG(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	LN_EXCLDNG_RPRCHS_AGRMNT_AND_ADVNC_HDG_uniqueID = models.CharField("LN_EXCLDNG_RPRCHS_AGRMNT_AND_ADVNC_HDG_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ACCNTNG_HDG_INDCTR_domain = {		"1":"Accounting_hedge",
}

	ACCNTNG_HDG_INDCTR = models.CharField("ACCNTNG_HDG_INDCTR",max_length=255, choices=ACCNTNG_HDG_INDCTR_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_HDG_INDCTR_domain")

	TYP_HDG_BIRD_domain = {		"1":"Fair_value_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_a",
		"11":"Hedges_other_than_cash_flow_hedge_and_hedge_of_net_investment_in_a_foreign_operation_Economic_hedge",
		"12":"Economic_hedge_With_use_of_fair_value_option",
		"13":"Economic_hedge_Other",
		"2":"Cash_flow_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_b",
		"3":"Hedge_of_a_net_investment_in_a_foreign_operation_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_c",
		"4":"Portfolio_fair_value_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"5":"Portfolio_cash_flow_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"6":"Cost_price_hedge_Hedging_relationship_as_defined_in_Reg_680_2014_Annex_V_part_2_114_This_hedging_relationship_is_applicable_only_under_nGAAP_based_on_BAD",
		"7":"Other_than_Fair_value_hedge_Cash_flow_hedge_Hedge_of_a_net_investment_in_a_foreign_operation_Portfolio_fair_value_hedges_of_interest_rate_risk_Portfolio_cash_flow_hedges_of_interest_rate_risk_Cost_price_hedge_Other_applicable_hedging_relationship_for_nGAAP_based_on_BAD_reporters",
}

	TYP_HDG = models.CharField("TYP_HDG",max_length=255, choices=TYP_HDG_BIRD_domain,default=None, blank=True, null=True, db_comment="TYP_HDG_BIRD_domain")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="LN_EXCLDNG_RPRCHS_AGRMNT_AND_ADVNC_HDG_to_theINSTRMNTs")

	class Meta:

		verbose_name = 'LN_EXCLDNG_RPRCHS_AGRMNT_AND_ADVNC_HDG'

		verbose_name_plural = 'LN_EXCLDNG_RPRCHS_AGRMNT_AND_ADVNC_HDGs'

class LNG_DBT_SCRTY_PSTN_ENCMBRNC_DRVD_DT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	LNG_DBT_SCRTY_PSTN_ENCMBRNC_DRVD_DT_uniqueID = models.CharField("LNG_DBT_SCRTY_PSTN_ENCMBRNC_DRVD_DT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	SRC_ENCMBRNC_INPT_domain = {		"10":"Debt_securities_issued_covered_bonds_securities_Covered_bonds_securities_issued_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"11":"Debt_securities_issued_asset_backed_securities_Asset_backed_securities_ABS_issued_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"12":"Debt_securities_issued_other_than_covered_bonds_and_ABSs_Debt_securities_issued_other_than_covered_bonds_and_ABSs_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"13":"Other_sources_of_encumbrance_Other_sources_of_encumbrance_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"14":"Repurchase_agreements",
		"15":"Short_position",
		"16":"Loan_commitments_received",
		"17":"Financial_guarantees_received",
		"18":"Securities_borrowed_with_non_cash_collateral",
		"6":"Exchange_traded_derivatives_Exchange_traded_derivatives_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"7":"Over_the_counter_derivatives_Over_the_counter_derivatives_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"9":"Deposits_other_than_repurchase_agreements_Deposits_other_than_repurchase_agreements_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
}

	SRC_ENCMBRNC = models.CharField("SRC_ENCMBRNC",max_length=255, choices=SRC_ENCMBRNC_INPT_domain,default=None, blank=True, null=True, db_comment="SRC_ENCMBRNC_INPT_domain")

	ENCMBRD_NMNL_AMNT = models.BigIntegerField("ENCMBRD_NMNL_AMNT",default=None, blank=True, null=True)

	theSCRTY_PSTN = models.ForeignKey("SCRTY_PSTN", models.SET_NULL,blank=True,null=True,related_name="LNG_DBT_SCRTY_PSTN_ENCMBRNC_DRVD_DT_to_theSCRTY_PSTNs")

	class Meta:

		verbose_name = 'LNG_DBT_SCRTY_PSTN_ENCMBRNC_DRVD_DT'

		verbose_name_plural = 'LNG_DBT_SCRTY_PSTN_ENCMBRNC_DRVD_DTs'

class LNG_EQTY_FND_SCRYT_PSTN_ENCMBRNC_DT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	LNG_EQTY_FND_SCRYT_PSTN_ENCMBRNC_DT_uniqueID = models.CharField("LNG_EQTY_FND_SCRYT_PSTN_ENCMBRNC_DT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	SRC_ENCMBRNC_INPT_domain = {		"10":"Debt_securities_issued_covered_bonds_securities_Covered_bonds_securities_issued_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"11":"Debt_securities_issued_asset_backed_securities_Asset_backed_securities_ABS_issued_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"12":"Debt_securities_issued_other_than_covered_bonds_and_ABSs_Debt_securities_issued_other_than_covered_bonds_and_ABSs_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"13":"Other_sources_of_encumbrance_Other_sources_of_encumbrance_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"14":"Repurchase_agreements",
		"15":"Short_position",
		"16":"Loan_commitments_received",
		"17":"Financial_guarantees_received",
		"18":"Securities_borrowed_with_non_cash_collateral",
		"6":"Exchange_traded_derivatives_Exchange_traded_derivatives_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"7":"Over_the_counter_derivatives_Over_the_counter_derivatives_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
		"9":"Deposits_other_than_repurchase_agreements_Deposits_other_than_repurchase_agreements_in_accordance_with_the_EBA_s_implementing_technical_standards_on_asset_encumbrance_reporting_as_referred_to_in_Article_99_5_and_Article_100_of_Regulation_EU_No_575_2013",
}

	SRC_ENCMBRNC = models.CharField("SRC_ENCMBRNC",max_length=255, choices=SRC_ENCMBRNC_INPT_domain,default=None, blank=True, null=True, db_comment="SRC_ENCMBRNC_INPT_domain")

	ENCMBRD_NMBR_SHRS = models.BigIntegerField("ENCMBRD_NMBR_SHRS",default=None, blank=True, null=True)

	theSCRTY_PSTN = models.ForeignKey("SCRTY_PSTN", models.SET_NULL,blank=True,null=True,related_name="LNG_EQTY_FND_SCRYT_PSTN_ENCMBRNC_DT_to_theSCRTY_PSTNs")

	class Meta:

		verbose_name = 'LNG_EQTY_FND_SCRYT_PSTN_ENCMBRNC_DT'

		verbose_name_plural = 'LNG_EQTY_FND_SCRYT_PSTN_ENCMBRNC_DTs'

class LNG_NN_NGTBL_SCRTY_PSTN_CLLTRL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	LNG_NN_NGTBL_SCRTY_PSTN_CLLTRL_ASSGNMNT_uniqueID = models.CharField("LNG_NN_NGTBL_SCRTY_PSTN_CLLTRL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	CLLTRL_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"1":"Collateral_received",
		"2":"Collateral_given",
}

	CLLTRL_RL_TYP = models.CharField("CLLTRL_RL_TYP",max_length=255, choices=CLLTRL_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="CLLTRL_RL_TYP_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	ALLCTD_UNSD_CLLTRL_VL = models.FloatField("ALLCTD_UNSD_CLLTRL_VL",default=None, blank=True, null=True)

	PRTCTN_ALLCTD_VL = models.BigIntegerField("PRTCTN_ALLCTD_VL",default=None, blank=True, null=True)

	theCLLTRL_RL = models.ForeignKey("CLLTRL_RL", models.SET_NULL,blank=True,null=True,related_name="LNG_NN_NGTBL_SCRTY_PSTN_CLLTRL_ASSGNMNT_to_theCLLTRL_RLs")

	theSCRTY_PSTN = models.ForeignKey("SCRTY_PSTN", models.SET_NULL,blank=True,null=True,related_name="LNG_NN_NGTBL_SCRTY_PSTN_CLLTRL_ASSGNMNT_to_theSCRTY_PSTNs")

	class Meta:

		verbose_name = 'LNG_NN_NGTBL_SCRTY_PSTN_CLLTRL_ASSGNMNT'

		verbose_name_plural = 'LNG_NN_NGTBL_SCRTY_PSTN_CLLTRL_ASSGNMNTs'

class LNG_SCRTY_PSTN_HDG(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	LNG_SCRTY_PSTN_HDG_uniqueID = models.CharField("LNG_SCRTY_PSTN_HDG_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	ACCNTNG_HDG_INDCTR_domain = {		"1":"Accounting_hedge",
}

	ACCNTNG_HDG_INDCTR = models.CharField("ACCNTNG_HDG_INDCTR",max_length=255, choices=ACCNTNG_HDG_INDCTR_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_HDG_INDCTR_domain")

	TYP_HDG_BIRD_domain = {		"1":"Fair_value_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_a",
		"11":"Hedges_other_than_cash_flow_hedge_and_hedge_of_net_investment_in_a_foreign_operation_Economic_hedge",
		"12":"Economic_hedge_With_use_of_fair_value_option",
		"13":"Economic_hedge_Other",
		"2":"Cash_flow_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_b",
		"3":"Hedge_of_a_net_investment_in_a_foreign_operation_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_c",
		"4":"Portfolio_fair_value_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"5":"Portfolio_cash_flow_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"6":"Cost_price_hedge_Hedging_relationship_as_defined_in_Reg_680_2014_Annex_V_part_2_114_This_hedging_relationship_is_applicable_only_under_nGAAP_based_on_BAD",
		"7":"Other_than_Fair_value_hedge_Cash_flow_hedge_Hedge_of_a_net_investment_in_a_foreign_operation_Portfolio_fair_value_hedges_of_interest_rate_risk_Portfolio_cash_flow_hedges_of_interest_rate_risk_Cost_price_hedge_Other_applicable_hedging_relationship_for_nGAAP_based_on_BAD_reporters",
}

	TYP_HDG = models.CharField("TYP_HDG",max_length=255, choices=TYP_HDG_BIRD_domain,default=None, blank=True, null=True, db_comment="TYP_HDG_BIRD_domain")

	theSCRTY_PSTN = models.ForeignKey("SCRTY_PSTN", models.SET_NULL,blank=True,null=True,related_name="LNG_SCRTY_PSTN_HDG_to_theSCRTY_PSTNs")

	class Meta:

		verbose_name = 'LNG_SCRTY_PSTN_HDG'

		verbose_name_plural = 'LNG_SCRTY_PSTN_HDGs'

class LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_uniqueID = models.CharField("LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain = {		"3":"Long_security_position_trading_book_assignment_International_Financial_Reporting_Standard_IFRS",
		"4":"Long_security_position_trading_book_assignment_national_general_accepted_accounting_principles_nGAAP",
		"5":"Long_security_position_banking_book_assignment",
}

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP = models.CharField("LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP",max_length=255, choices=LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	ARRRS = models.BigIntegerField("ARRRS",default=None, blank=True, null=True)

	HRCTS_TRDNG_PSTNS_FV = models.BigIntegerField("HRCTS_TRDNG_PSTNS_FV",default=None, blank=True, null=True)

	IMPRMNT_ASSSSMNT_MTHD_INPT_domain = {		"0":"Not_applicable",
		"1":"Collectively_assessed",
		"2":"Individually_assessed",
}

	IMPRMNT_ASSSSMNT_MTHD = models.CharField("IMPRMNT_ASSSSMNT_MTHD",max_length=255, choices=IMPRMNT_ASSSSMNT_MTHD_INPT_domain,default=None, blank=True, null=True, db_comment="IMPRMNT_ASSSSMNT_MTHD_INPT_domain")

	IMPRMNT_STTS_INPT_domain = {		"0":"Not_applicable",
		"211":"General_allowances_for_credit_risk_GAAP",
		"212":"General_allowances_for_banking_risk_GAAP",
		"23":"Stage_1_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_12_month_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"24":"Stage_2_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"25":"Stage_3_IFRS_To_be_used_if_the_instrument_is_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"26":"Specific_allowances_GAAP_To_be_used_if_the_instrument_is_subject_to_impairment_in_accordance_with_an_applied_accounting_standard_other_than_IFRS_9_and_specific_loss_allowances_are_raised_irrespective_of_whether_these_allowances_are_individually_or_collectively_assessed_impaired",
		"27":"Purchased_or_originated_credit_impaired_instruments_POCI_IFRS",
}

	IMPRMNT_STTS = models.CharField("IMPRMNT_STTS",max_length=255, choices=IMPRMNT_STTS_INPT_domain,default=None, blank=True, null=True, db_comment="IMPRMNT_STTS_INPT_domain")

	NMBR_SHRS = models.BigIntegerField("NMBR_SHRS",default=None, blank=True, null=True)

	NMNL_AMNT = models.BigIntegerField("NMNL_AMNT",default=None, blank=True, null=True)

	NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain = {		"1":"Non_performing_prior_to_forbearance",
		"2":"Not_non_performing_prior_to_forbearance",
}

	NN_PRFRMNG_PRR_FRBRNC_INDCTR = models.CharField("NN_PRFRMNG_PRR_FRBRNC_INDCTR",max_length=255, choices=NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain,default=None, blank=True, null=True, db_comment="NN_PRFRMNG_PRR_FRBRNC_INDCTR_domain")

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_TYP_domain = {		"1":"Long_debt_security_position_Prudential_portfolio_assignment",
		"2":"Long_equity_or_fund_security_position_Prudential_portfolio_assignment",
}

	TYP_LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT = models.CharField("TYP_LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT",max_length=255, choices=LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_TYP_domain")

	theSCRTY_PSTN = models.ForeignKey("SCRTY_PSTN", models.SET_NULL,blank=True,null=True,related_name="LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_to_theSCRTY_PSTNs")

	class Meta:

		verbose_name = 'LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT'

		verbose_name_plural = 'LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNTs'

class LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_uniqueID = models.CharField("LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CLSSFCTN_ASSTS_domain = {		"14":"IFRS_Cash_balances_at_central_banks_and_other_demand_deposits_Cash_balances_at_central_banks_and_other_demand_deposits_in_accordance_with_IFRS",
		"2":"IFRS_Financial_assets_held_for_trading_Financial_assets_held_for_trading_in_accordance_with_IFRS",
		"3":"nGAAP_Trading_Financial_assets_Trading_financial_assets_in_accordance_with_national_GAAP",
		"4":"IFRS_Financial_assets_designated_at_fair_value_through_profit_or_loss_Financial_assets_measured_at_fair_value_through_profit_and_loss_and_designated_as_such_upon_initial_recognition_or_subsequently_in_accordance_with_IFRS_except_those_classified_as_financial_assets_held_for_trading",
		"41":"IFRS_Non_trading_financial_assets_mandatorily_at_fair_value_through_profit_or_loss_Non_trading_financial_assets_mandatorily_at_fair_value_through_profit_or_loss_in_accordance_with_IFRS",
		"45":"nGAAP_Cash_balances_at_central_banks_and_other_demand_deposits_Cash_balances_at_central_banks_and_other_demand_deposits_in_accordance_with_national_GAAP",
		"47":"nGAAP_Financial_assets_designated_at_fair_value_through_profit_or_loss_Financial_assets_designated_at_fair_value_through_profit_or_loss_in_accordance_with_national_GAAP",
		"6":"IFRS_Financial_assets_at_amortised_cost_Financial_assets_measured_at_amortised_cost_in_accordance_with_IFRS",
		"64":"nGAAP_financial_assets_at_fair_value_or_strict_LOCOM",
		"7":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_fair_value_through_profit_or_loss_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_in_accordance_with_national_GAAP",
		"711":"Accounting_portfolios_for_financial_assets_other_than_classified_as_held_for_sale_excluding_financial_assets_held_for_trading_trading_financial_assets_and_cash_and_cash_balances_at_central_banks_and_other_demand_deposits",
		"73":"nGAAP_Other_non_trading_non_derivative_financial_assets_LOCOM_nGAAP_Other_non_trading_non_derivative_financial_assets_at_LOCOM",
		"74":"nGAAP_Other_non_trading_non_derivative_financial_assets_Other_than_LOCOM",
		"76":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_LOCOM_nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_at_LOCOM",
		"77":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_a_cost_based_method_Other_than_LOCOM",
		"8":"IFRS_Financial_assets_at_fair_value_through_other_comprehensive_income_Financial_assets_measured_at_fair_value_through_other_comprehensive_income_due_to_business_model_and_cash_flows_characteristics_in_accordance_with_IFRS",
		"83":"Investments_in_subsidiaries_joint_ventures_and_associates",
		"85":"nGAAP_Accounting_portfolios_for_trading_financial_instruments_Cost_based_method_or_LOCOM",
		"9":"nGAAP_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_Non_trading_non_derivative_financial_assets_measured_at_fair_value_to_equity_in_accordance_with_national_GAAP",
}

	ACCNTNG_CLSSFCTN = models.CharField("ACCNTNG_CLSSFCTN",max_length=255, choices=ACCNTNG_CLSSFCTN_ASSTS_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CLSSFCTN_ASSTS_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain = {		"3":"Long_security_position_trading_book_assignment_International_Financial_Reporting_Standard_IFRS",
		"4":"Long_security_position_trading_book_assignment_national_general_accepted_accounting_principles_nGAAP",
		"5":"Long_security_position_banking_book_assignment",
}

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP = models.CharField("LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP",max_length=255, choices=LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	ACCMLTD_CHNGS_FV = models.BigIntegerField("ACCMLTD_CHNGS_FV",default=None, blank=True, null=True)

	ACCMLTD_CHNGS_FV_CR = models.BigIntegerField("ACCMLTD_CHNGS_FV_CR",default=None, blank=True, null=True)

	ACCMLTD_CVRG_RT = models.FloatField("ACCMLTD_CVRG_RT",default=None, blank=True, null=True)

	ACCMLTD_IMPRMNT = models.BigIntegerField("ACCMLTD_IMPRMNT",default=None, blank=True, null=True)

	ACCMLTD_NGTV_VL_ADJSTMNT_CR = models.BigIntegerField("ACCMLTD_NGTV_VL_ADJSTMNT_CR",default=None, blank=True, null=True)

	ACCMLTD_NGTV_VL_ADJSTMNT_MR = models.BigIntegerField("ACCMLTD_NGTV_VL_ADJSTMNT_MR",default=None, blank=True, null=True)

	ACCMLTD_PRTL_WRTFFS = models.BigIntegerField("ACCMLTD_PRTL_WRTFFS",default=None, blank=True, null=True)

	ACCMLTD_TTL_WRTFFS = models.BigIntegerField("ACCMLTD_TTL_WRTFFS",default=None, blank=True, null=True)

	ACCMLTD_WRTFFS = models.BigIntegerField("ACCMLTD_WRTFFS",default=None, blank=True, null=True)

	ACCRD_INTRST = models.BigIntegerField("ACCRD_INTRST",default=None, blank=True, null=True)

	ARRRS = models.BigIntegerField("ARRRS",default=None, blank=True, null=True)

	CRRYNG_AMNT = models.BigIntegerField("CRRYNG_AMNT",default=None, blank=True, null=True)

	FV_CHNG = models.BigIntegerField("FV_CHNG",default=None, blank=True, null=True)

	FV_CHNGS_HDG_ACCNTNG = models.BigIntegerField("FV_CHNGS_HDG_ACCNTNG",default=None, blank=True, null=True)

	FVO_DSGNTN_INPT_domain = {		"0":"Not_applicable",
		"2":"Management_on_a_fair_value_basis",
		"5":"Management_of_credit_risk_Upon_designation",
		"6":"Management_of_credit_risk_After_the_designation",
}

	FVO_DSGNTN = models.CharField("FVO_DSGNTN",max_length=255, choices=FVO_DSGNTN_INPT_domain,default=None, blank=True, null=True, db_comment="FVO_DSGNTN_INPT_domain")

	GNRL_ALLWNCS_BNK_RSK = models.BigIntegerField("GNRL_ALLWNCS_BNK_RSK",default=None, blank=True, null=True)

	GNRL_ALLWNCS_CRDT_RSK = models.BigIntegerField("GNRL_ALLWNCS_CRDT_RSK",default=None, blank=True, null=True)

	GRSS_CRRYNG_AMNT = models.BigIntegerField("GRSS_CRRYNG_AMNT",default=None, blank=True, null=True)

	GRSS_CRRYNG_AMNT_E_INTRST = models.BigIntegerField("GRSS_CRRYNG_AMNT_E_INTRST",default=None, blank=True, null=True)

	HLD_SL_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Held_for_sale_The_member_indicates_that_the_instrument_is_held_for_sale",
		"2":"Not_held_for_sale_The_member_indicates_that_the_instrument_is_not_held_for_sale",
}

	HLD_SL_INDCTR = models.CharField("HLD_SL_INDCTR",max_length=255, choices=HLD_SL_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="HLD_SL_INDCTR_INPT_domain")

	IMPRMNT_ASSSSMNT_MTHD_ANCRDT_CLLCTN_domain = {		"1":"Collectively_assessed",
		"2":"Individually_assessed",
}

	IMPRMNT_ASSSSMNT_MTHD = models.CharField("IMPRMNT_ASSSSMNT_MTHD",max_length=255, choices=IMPRMNT_ASSSSMNT_MTHD_ANCRDT_CLLCTN_domain,default=None, blank=True, null=True, db_comment="IMPRMNT_ASSSSMNT_MTHD_ANCRDT_CLLCTN_domain")

	IMPRMNT_STTS_domain = {		"211":"General_allowances_for_credit_risk_GAAP",
		"212":"General_allowances_for_banking_risk_GAAP",
		"23":"Stage_1_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_12_month_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"24":"Stage_2_IFRS_To_be_used_if_the_instrument_is_not_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"25":"Stage_3_IFRS_To_be_used_if_the_instrument_is_impaired_and_a_loss_allowance_at_an_amount_equal_to_lifetime_expected_credit_losses_is_raised_against_the_instrument_under_IFRS_Only_for_instruments_subject_to_impairment_under_IFRS_9",
		"26":"Specific_allowances_GAAP_To_be_used_if_the_instrument_is_subject_to_impairment_in_accordance_with_an_applied_accounting_standard_other_than_IFRS_9_and_specific_loss_allowances_are_raised_irrespective_of_whether_these_allowances_are_individually_or_collectively_assessed_impaired",
		"27":"Purchased_or_originated_credit_impaired_instruments_POCI_IFRS",
}

	IMPRMNT_STTS = models.CharField("IMPRMNT_STTS",max_length=255, choices=IMPRMNT_STTS_domain,default=None, blank=True, null=True, db_comment="IMPRMNT_STTS_domain")

	INTL_IMPRMNT_STTS_domain = {		"23":"Stage_1_IFRS",
		"24":"Stage_2_IFRS",
		"25":"Stage_3_IFRS",
}

	INTL_IMPRMNT_STTS = models.CharField("INTL_IMPRMNT_STTS",max_length=255, choices=INTL_IMPRMNT_STTS_domain,default=None, blank=True, null=True, db_comment="INTL_IMPRMNT_STTS_domain")

	NMBR_SHRS = models.BigIntegerField("NMBR_SHRS",default=None, blank=True, null=True)

	NMNL_AMNT = models.BigIntegerField("NMNL_AMNT",default=None, blank=True, null=True)

	SBJCT_IMPRMNT_INDCTR_F_04_08_SBJCT_IMPRMNT_INDCTR_REF_domain = {		"1":"Subject_to_impairment",
		"2":"Not_subject_to_impairment",
}

	SBJCT_IMPRMNT_INDCTR = models.CharField("SBJCT_IMPRMNT_INDCTR",max_length=255, choices=SBJCT_IMPRMNT_INDCTR_F_04_08_SBJCT_IMPRMNT_INDCTR_REF_domain,default=None, blank=True, null=True, db_comment="SBJCT_IMPRMNT_INDCTR_F_04_08_SBJCT_IMPRMNT_INDCTR_REF_domain")

	TRNSFR_IMPRMNT_STGS_F_12_02_TRNSFR_IMPRMNT_STGS_REF_domain = {		"1":"To_stage_1_from_stage_2",
		"2":"To_stage_1_from_stage_3",
		"3":"To_stage_2_from_stage_1",
		"4":"To_stage_2_from_stage_3",
		"5":"To_stage_3_from_stage_1",
		"6":"To_stage_3_from_stage_2",
}

	TRNSFR_IMPRMNT_STGS = models.CharField("TRNSFR_IMPRMNT_STGS",max_length=255, choices=TRNSFR_IMPRMNT_STGS_F_12_02_TRNSFR_IMPRMNT_STGS_REF_domain,default=None, blank=True, null=True, db_comment="TRNSFR_IMPRMNT_STGS_F_12_02_TRNSFR_IMPRMNT_STGS_REF_domain")

	TYP_LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_INPT_domain = {		"3":"Long_debt_security_position_Prudential_portfolio_assignment_Accounting_classification_for_financial_assets_assignment_according_to_International_Financial_Reporting_Standard_IFRS",
		"4":"Long_debt_security_position_Prudential_portfolio_assignment_Accounting_classification_for_financial_assets_assignment_according_to_national_general_accepted_accounting_principles_nGAAP",
		"5":"Long_equity_or_fund_security_position_Prudential_portfolio_assignment_Accounting_classification_for_assets_assignment_according_to_International_Financial_Reporting_Standard_IFRS",
		"6":"Long_equity_or_fund_security_position_Prudential_portfolio_assignment_Accounting_classification_for_assets_assignment_according_to_national_general_accepted_accounting_principles_nGAAP",
}

	TYP_LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = models.CharField("TYP_LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT",max_length=255, choices=TYP_LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_INPT_domain")

	theLNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT = models.ForeignKey("LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT", models.SET_NULL,blank=True,null=True,related_name="LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_to_theLNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNTs")

	class Meta:

		verbose_name = 'LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT'

		verbose_name_plural = 'LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNTs'

class LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_RSK_DT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_RSK_DT_uniqueID = models.CharField("LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_RSK_DT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	EXPSR_CLSS_CLCLTN_domain = {		"1":"SA_Equity_exposures",
		"10":"SA_Exposures_to_international_organisations",
		"11":"SA_Exposures_to_multilateral_development_banks",
		"12":"SA_Exposures_to_public_sector_entities",
		"13":"SA_Exposures_to_regional_governments_or_local_authorities",
		"14":"SA_Items_associated_with_a_particular_high_risk",
		"16":"SA_Other_items",
		"2":"SA_Exposures_in_default",
		"3":"SA_Exposures_in_the_form_of_covered_bonds",
		"4":"SA_Exposures_in_the_form_of_units_or_shares_in_CIUs",
		"6":"SA_Exposures_to_central_governments_or_central_banks",
		"7":"SA_Exposures_to_corporates_without_a_short_term_credit_assessment",
		"8":"SA_Exposures_to_institutions_and_corporates_with_a_short_term_credit_assessment",
		"9":"SA_Exposures_to_institutions_without_a_short_term_credit_assessment",
}

	EXPSR_CLSS = models.CharField("EXPSR_CLSS",max_length=255, choices=EXPSR_CLSS_CLCLTN_domain,default=None, blank=True, null=True, db_comment="EXPSR_CLSS_CLCLTN_domain")

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain = {		"3":"Long_security_position_trading_book_assignment_International_Financial_Reporting_Standard_IFRS",
		"4":"Long_security_position_trading_book_assignment_national_general_accepted_accounting_principles_nGAAP",
		"5":"Long_security_position_banking_book_assignment",
}

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP = models.CharField("LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP",max_length=255, choices=LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	APPRCH_PRDNTL_PRPSS_domain = {		"1":"_1250_for_positions_not_subject_to_any_method_Securitisations_Calculation_of_the_risk_weighted_exposure_amounts_for_securitisation_positions_to_which_a_risk_weight_of_1250_is_assigned_in_accordance_with_Article_259_1_d_of_CRR",
		"118":"SEC_IRBA_Internal_ratings_based_approach_for_securitisation_positions_Securitisations_Calculation_of_the_risk_weighted_exposure_amounts_for_securitisation_positions_for_which_the_Internal_ratings_based_approach_is_used",
		"122":"SEC_SA_Standardised_approach_for_securitisations_Securitisations_Calculation_of_the_risk_weighted_exposure_amounts_for_securitisation_positions_for_which_the_Standardised_approach_is_used",
		"125":"SEC_ERBA_External_ratings_based_approach_for_securitisation_positions_Securitisations_Calculation_of_the_risk_weighted_exposure_amounts_for_securitisation_positions_for_which_the_External_ratings_based_approach_is_used",
		"18":"Ratings_based_method_Securitisations_Calculation_of_the_risk_weighted_exposure_amounts_for_securitisation_positions_for_which_the_Ratings_based_method_set_out_in_Article_261_of_CRR_is_used",
		"19":"Supervisory_formula_method_Securitisations_Calculation_of_the_risk_weighted_exposure_amounts_for_securitisation_positions_for_which_the_Supervisory_formula_method_set_out_in_Article_262_of_CRR_is_used",
		"25":"Internal_assessment_approach_Securitisations_Calculation_of_the_risk_weighted_exposure_amounts_for_securitisation_positions_for_which_the_Internal_assessment_approach_set_out_in_Article_259_3_and_4_of_CRR_is_used",
		"30":"Look_through_approach_Securitisations_Calculation_of_the_risk_weighted_exposure_amounts_for_securitisation_positions_for_which_the_Look_through_approach_set_out_in_Article_259_1_e_of_CRR_is_used",
		"33":"IRB_Internal_models_approach_Equity_exposures_Calculation_of_the_risk_weighted_exposure_amounts_for_equity_exposures_for_which_the_Internal_models_approach_set_out_in_Article_155_4_of_CRR_is_used",
		"34":"IRB_PD_LGD_approach_Equity_exposures_Calculation_of_the_risk_weighted_exposure_amounts_for_equity_exposures_for_which_the_PD_LGD_approach_set_out_in_Article_155_3_of_CRR_is_used",
		"35":"IRB_Simple_risk_weight_approach_Equity_exposures_Calculation_of_the_risk_weighted_exposure_amounts_for_equity_exposures_for_which_the_Simple_risk_weight_approach_set_out_in_Article_155_2_of_CRR_is_used",
		"42":"Standardised_approach_Standardised_approach_to_calculate_the_risk_weighted_exposure_amounts_in_accordance_with_Chapter_2_of_Regulation_EU_No_575_2013",
		"66":"Advanced_IRB_Internal_Ratings_Based_IRB_approach_to_calculate_the_risk_weighted_exposure_amounts_in_accordance_with_Chapter_3_of_Regulation_EU_No_575_2013_and_banks_calculate_and_use_in_addition_to_the_PDs_their_own_risk_parameter_subject_to_the_supervisory_guid",
		"67":"Foundation_IRB_Internal_Ratings_Based_IRB_approach_to_calculate_the_risk_weighted_exposure_amounts_in_accordance_with_Chapter_3_of_Regulation_EU_No_575_2013_and_banks_use_their_own_calculated_PDs_while_for_the_other_parameters_such_as_LGD_predefined_values_provid",
		"68":"IRB_Fixed_risk_weights_Equity_exposures_Calculation_of_the_risk_weighted_exposure_amounts_for_equity_exposures_which_attract_a_fixed_risk_weight_treatment_without_however_being_explicitly_treated_according_to_the_Simple_Risk_Weight_approach_or_the_temporary_or_permanent_partial_use_of_the_credit_risk_standardised_approach_set_out_in_Article_155_of_CRR",
}

	APPRCH_PRDNTL_PRPSS = models.CharField("APPRCH_PRDNTL_PRPSS",max_length=255, choices=APPRCH_PRDNTL_PRPSS_domain,default=None, blank=True, null=True, db_comment="APPRCH_PRDNTL_PRPSS_domain")

	EXPSR_VL = models.BigIntegerField("EXPSR_VL",default=None, blank=True, null=True)

	LGD_DWNTRNS = models.FloatField("LGD_DWNTRNS",default=None, blank=True, null=True)

	LGD_NRML = models.FloatField("LGD_NRML",default=None, blank=True, null=True)

	RSK_WGHT = models.FloatField("RSK_WGHT",default=None, blank=True, null=True)

	SPCFC_RSK_WGHT = models.FloatField("SPCFC_RSK_WGHT",default=None, blank=True, null=True)

	theLNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT = models.ForeignKey("LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT", models.SET_NULL,blank=True,null=True,related_name="LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_RSK_DT_to_theLNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNTs")

	class Meta:

		verbose_name = 'LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_RSK_DT'

		verbose_name_plural = 'LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_RSK_DTs'

class LNG_SCRTY_PSTN_PRTCTN_ARRNGMNT_GVN_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	LNG_SCRTY_PSTN_PRTCTN_ARRNGMNT_GVN_ASSGNMNT_uniqueID = models.CharField("LNG_SCRTY_PSTN_PRTCTN_ARRNGMNT_GVN_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	PRTCTN_ARRNGMNT_RL_TYP_domain = {		"0":"Not_applicable",
		"1":"Protection_arrangement_received",
		"2":"Protection_arrangement_given",
}

	PRTCTN_ARRNGMNT_RL_TYP = models.CharField("PRTCTN_ARRNGMNT_RL_TYP",max_length=255, choices=PRTCTN_ARRNGMNT_RL_TYP_domain,default=None, blank=True, null=True, db_comment="PRTCTN_ARRNGMNT_RL_TYP_domain")

	PRTCTN_ID = models.CharField("PRTCTN_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	ALLCTD_UNSD_CLLTRL_VL = models.FloatField("ALLCTD_UNSD_CLLTRL_VL",default=None, blank=True, null=True)

	PRTCTN_ALLCTD_VL = models.BigIntegerField("PRTCTN_ALLCTD_VL",default=None, blank=True, null=True)

	thePRTCTN_ARRNGMNT_RL = models.ForeignKey("PRTCTN_ARRNGMNT_RL", models.SET_NULL,blank=True,null=True,related_name="LNG_SCRTY_PSTN_PRTCTN_ARRNGMNT_GVN_ASSGNMNT_to_thePRTCTN_ARRNGMNT_RLs")

	theSCRTY_PSTN = models.ForeignKey("SCRTY_PSTN", models.SET_NULL,blank=True,null=True,related_name="LNG_SCRTY_PSTN_PRTCTN_ARRNGMNT_GVN_ASSGNMNT_to_theSCRTY_PSTNs")

	class Meta:

		verbose_name = 'LNG_SCRTY_PSTN_PRTCTN_ARRNGMNT_GVN_ASSGNMNT'

		verbose_name_plural = 'LNG_SCRTY_PSTN_PRTCTN_ARRNGMNT_GVN_ASSGNMNTs'

class LNKD_ENTRPRS_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	LNKD_ENTRPRS_ASSGNMNT_uniqueID = models.CharField("LNKD_ENTRPRS_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CNTR_BNK_PRVT_SCTR_CMPNY_PRTY_ID = models.CharField("CNTR_BNK_PRVT_SCTR_CMPNY_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	LNKD_ENTRPRS_PRTY_ID = models.CharField("LNKD_ENTRPRS_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	LNKD_ENTRPRS_PRTY_RL_TYP = models.CharField("LNKD_ENTRPRS_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="LNKD_ENTRPRS_ASSGNMNT_to_theENTTY_RLs")

	thePRTY = models.ForeignKey("PRTY", models.SET_NULL,blank=True,null=True,related_name="LNKD_ENTRPRS_ASSGNMNT_to_thePRTYs")

	class Meta:

		verbose_name = 'LNKD_ENTRPRS_ASSGNMNT'

		verbose_name_plural = 'LNKD_ENTRPRS_ASSGNMNTs'

class MSTR_AGRMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	MSTR_AGRMNT_uniqueID = models.CharField("MSTR_AGRMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	MSTR_AGRMNT_ID = models.CharField("MSTR_AGRMNT_ID",max_length=255,default=None, blank=True, null=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	TYP_MSTR_AGRMNT_INPT_domain = {		"2":"Master_agreement_with_a_clearing_member",
		"3":"Master_agreement_with_a_qualifying_central_counterparty",
		"4":"Master_agreement_with_a_non_qualified_central_counterparty",
}

	TYP_MSTR_AGRMNT = models.CharField("TYP_MSTR_AGRMNT",max_length=255, choices=TYP_MSTR_AGRMNT_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_MSTR_AGRMNT_INPT_domain")

	class Meta:

		verbose_name = 'MSTR_AGRMNT'

		verbose_name_plural = 'MSTR_AGRMNTs'

class MSTR_AGRMNT_ENTTY_RL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	MSTR_AGRMNT_ENTTY_RL_ASSGNMNT_uniqueID = models.CharField("MSTR_AGRMNT_ENTTY_RL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	MSTR_AGRMNT_ID = models.CharField("MSTR_AGRMNT_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	ORGNSTN_RL_TYP = models.CharField("ORGNSTN_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	TYP_MSTR_AGRMNT_ENTTY_RL_ASSGNMNT_INPT_domain = {		"1":"Master_agreement_Non_qualifying_central_counterparty_assignment",
		"2":"Master_agreement_Qualifying_central_counterparty_assignment",
		"4":"Master_agreement_Clearing_member_assignment",
}

	TYP_MSTR_AGRMNT_ENTTY_RL_ASSGNMNT = models.CharField("TYP_MSTR_AGRMNT_ENTTY_RL_ASSGNMNT",max_length=255, choices=TYP_MSTR_AGRMNT_ENTTY_RL_ASSGNMNT_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_MSTR_AGRMNT_ENTTY_RL_ASSGNMNT_INPT_domain")

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="MSTR_AGRMNT_ENTTY_RL_ASSGNMNT_to_theENTTY_RLs")

	theMSTR_AGRMNT = models.ForeignKey("MSTR_AGRMNT", models.SET_NULL,blank=True,null=True,related_name="MSTR_AGRMNT_ENTTY_RL_ASSGNMNT_to_theMSTR_AGRMNTs")

	class Meta:

		verbose_name = 'MSTR_AGRMNT_ENTTY_RL_ASSGNMNT'

		verbose_name_plural = 'MSTR_AGRMNT_ENTTY_RL_ASSGNMNTs'

class MSTR_AGRMNT_FNNCL_CNTRCT_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	MSTR_AGRMNT_FNNCL_CNTRCT_ASSGNMNT_uniqueID = models.CharField("MSTR_AGRMNT_FNNCL_CNTRCT_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	FNNCL_CNTRCT_ID = models.CharField("FNNCL_CNTRCT_ID",max_length=255,default=None, blank=True, null=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	MSTR_AGRMNT_ID = models.CharField("MSTR_AGRMNT_ID",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	theFNNCL_CNTRCT = models.ForeignKey("FNNCL_CNTRCT", models.SET_NULL,blank=True,null=True,related_name="MSTR_AGRMNT_FNNCL_CNTRCT_ASSGNMNT_to_theFNNCL_CNTRCTs")

	theMSTR_AGRMNT = models.ForeignKey("MSTR_AGRMNT", models.SET_NULL,blank=True,null=True,related_name="MSTR_AGRMNT_FNNCL_CNTRCT_ASSGNMNT_to_theMSTR_AGRMNTs")

	class Meta:

		verbose_name = 'MSTR_AGRMNT_FNNCL_CNTRCT_ASSGNMNT'

		verbose_name_plural = 'MSTR_AGRMNT_FNNCL_CNTRCT_ASSGNMNTs'

class NN_FNNCL_ASST(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	NN_FNNCL_ASST_uniqueID = models.CharField("NN_FNNCL_ASST_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	HLD_SL_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Held_for_sale_The_member_indicates_that_the_instrument_is_held_for_sale",
		"2":"Not_held_for_sale_The_member_indicates_that_the_instrument_is_not_held_for_sale",
}

	HLD_SL_INDCTR = models.CharField("HLD_SL_INDCTR",max_length=255, choices=HLD_SL_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="HLD_SL_INDCTR_INPT_domain")

	MSRMNT_MTHD_INPT_domain = {		"0":"Not_applicable",
		"1":"Cost_model_IAS_17_49_IAS_16_30_73_a_d",
		"3":"Revaluation_model_IAS_17_49_IAS_16_31_73_a_d",
}

	MSRMNT_MTHD = models.CharField("MSRMNT_MTHD",max_length=255, choices=MSRMNT_MTHD_INPT_domain,default=None, blank=True, null=True, db_comment="MSRMNT_MTHD_INPT_domain")

	NN_FNNCL_ASST_ID = models.CharField("NN_FNNCL_ASST_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SBJCT_OPRTNG_LS_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Subject_to_operating_lease_The_asset_is_subject_to_operating_lease",
		"2":"Not_Subject_to_operating_lease_The_asset_is_not_subject_to_operating_lease",
}

	SBJCT_OPRTNG_LS_INDCTR = models.CharField("SBJCT_OPRTNG_LS_INDCTR",max_length=255, choices=SBJCT_OPRTNG_LS_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="SBJCT_OPRTNG_LS_INDCTR_INPT_domain")

	SFTWR_ASST_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Software_assets",
		"2":"Not_software_assets",
}

	SFTWR_ASST_INDCTR = models.CharField("SFTWR_ASST_INDCTR",max_length=255, choices=SFTWR_ASST_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="SFTWR_ASST_INDCTR_INPT_domain")

	TM_SNC_INTL_RCGNTN_INPT_domain = {		"0":"Not_Applicable",
		"27":"_lt_eq_2_years",
		"29":"_gt_2_years_lt_eq_5_years",
		"37":"_gt_5_years",
}

	TM_SNC_INTL_RCGNTN = models.CharField("TM_SNC_INTL_RCGNTN",max_length=255, choices=TM_SNC_INTL_RCGNTN_INPT_domain,default=None, blank=True, null=True, db_comment="TM_SNC_INTL_RCGNTN_INPT_domain")

	TYP_NN_FNNCL_ASST_INPT_domain = {		"14":"Other_intangible_asset_not_taken_into_possession",
		"15":"Other_intangible_asset_taken_into_possession",
		"413":"Tangible_assets_Investment_property",
		"420":"Intangible_assets_Goodwill",
		"440":"Current_tax_assets",
		"450":"Deferred_tax_assets",
		"46":"Other_non_financial_asset_not_taken_into_possession",
		"48":"Other_non_financial_asset_taken_into_possession_before_the_period",
		"49":"Other_non_financial_asset_taken_into_possession_during_the_period",
		"6301":"Software_property_plant_and_equipment_not_taken_into_possession",
		"6302":"Non_software_property_plant_and_equipment_not_taken_into_possession",
		"66":"Software_property_plant_and_equipment_taken_into_possession",
		"67":"Non_software_property_plant_and_equipment_taken_into_possession",
}

	TYP_NN_FNNCL_ASST = models.CharField("TYP_NN_FNNCL_ASST",max_length=255, choices=TYP_NN_FNNCL_ASST_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_NN_FNNCL_ASST_INPT_domain")

	ACCMLTD_CHNG_NGTV = models.BigIntegerField("ACCMLTD_CHNG_NGTV",default=None, blank=True, null=True)

	ACCMLTD_CHNGS_FV_CR = models.BigIntegerField("ACCMLTD_CHNGS_FV_CR",default=None, blank=True, null=True)

	ACCMLTD_IMPRMNT = models.BigIntegerField("ACCMLTD_IMPRMNT",default=None, blank=True, null=True)

	CRRYNG_AMNT = models.BigIntegerField("CRRYNG_AMNT",default=None, blank=True, null=True)

	GCA_EXPSR_DRCGNSD_EXCHNG_CLLTRL = models.BigIntegerField("GCA_EXPSR_DRCGNSD_EXCHNG_CLLTRL",default=None, blank=True, null=True)

	GRSS_CRRYNG_AMNT = models.BigIntegerField("GRSS_CRRYNG_AMNT",default=None, blank=True, null=True)

	class Meta:

		verbose_name = 'NN_FNNCL_ASST'

		verbose_name_plural = 'NN_FNNCL_ASSTs'

class NN_FNNCL_LBLTY(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	NN_FNNCL_LBLTY_uniqueID = models.CharField("NN_FNNCL_LBLTY_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	NN_FNNCL_LBLTY_ID = models.CharField("NN_FNNCL_LBLTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	CRRYNG_AMNT = models.BigIntegerField("CRRYNG_AMNT",default=None, blank=True, null=True)

	HLD_SL_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Held_for_sale_The_member_indicates_that_the_instrument_is_held_for_sale",
		"2":"Not_held_for_sale_The_member_indicates_that_the_instrument_is_not_held_for_sale",
}

	HLD_SL_INDCTR = models.CharField("HLD_SL_INDCTR",max_length=255, choices=HLD_SL_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="HLD_SL_INDCTR_INPT_domain")

	TYP_NN_FNNCL_LBLTY_PRVSN_INPT_domain = {		"1301":"Non_financial_liabilites_other_than_Tax_liability_Share_capital_repayable_on_demand_or_Provision",
		"701":"Provisions_Funds_for_general_banking_risks",
		"702":"Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligations",
		"703":"Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligations",
		"704":"Provisions_Restructuring",
		"705":"Provisions_Pending_legal_issues_and_tax_litigation",
		"707":"Provisions_Other_than_Employee_benefits_Restructuring_Pending_legal_issues_and_tax_litigation_Off_balance_sheet_exposures_subject_to_credit_risk",
		"710":"Current_tax_liabilities",
		"720":"Deferred_tax_liabilities",
		"730":"Share_capital_repayable_on_demand",
}

	TYP_NN_FNNCL_LBLTY = models.CharField("TYP_NN_FNNCL_LBLTY",max_length=255, choices=TYP_NN_FNNCL_LBLTY_PRVSN_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_NN_FNNCL_LBLTY_PRVSN_INPT_domain")

	class Meta:

		verbose_name = 'NN_FNNCL_LBLTY'

		verbose_name_plural = 'NN_FNNCL_LBLTYs'

class NTRL_PRSN_KY_MNGMNT_PRSNLL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	NTRL_PRSN_KY_MNGMNT_PRSNLL_ASSGNMNT_uniqueID = models.CharField("NTRL_PRSN_KY_MNGMNT_PRSNLL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	NTRL_PRSN_GRP_RL_PRTY_ID = models.CharField("NTRL_PRSN_GRP_RL_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	NTRL_PRSN_GRP_RL_TYP = models.CharField("NTRL_PRSN_GRP_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="NTRL_PRSN_KY_MNGMNT_PRSNLL_ASSGNMNT_to_theENTTY_RLs")

	thePRTY = models.ForeignKey("PRTY", models.SET_NULL,blank=True,null=True,related_name="NTRL_PRSN_KY_MNGMNT_PRSNLL_ASSGNMNT_to_thePRTYs")

	class Meta:

		verbose_name = 'NTRL_PRSN_KY_MNGMNT_PRSNLL_ASSGNMNT'

		verbose_name_plural = 'NTRL_PRSN_KY_MNGMNT_PRSNLL_ASSGNMNTs'

class OTC_DRVTV_HDG(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	OTC_DRVTV_HDG_uniqueID = models.CharField("OTC_DRVTV_HDG_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ACCNTNG_HDG_INDCTR_domain = {		"1":"Accounting_hedge",
}

	ACCNTNG_HDG_INDCTR = models.CharField("ACCNTNG_HDG_INDCTR",max_length=255, choices=ACCNTNG_HDG_INDCTR_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_HDG_INDCTR_domain")

	CST_BSD_MTHD_LCM_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"At_cost_based_method_or_Lower_of_cost_or_market_LOCOM",
		"2":"Not_at_cost_based_method_or_Lower_of_cost_or_market_LOCOM",
}

	CST_BSD_MTHD_LCM_INDCTR = models.CharField("CST_BSD_MTHD_LCM_INDCTR",max_length=255, choices=CST_BSD_MTHD_LCM_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="CST_BSD_MTHD_LCM_INDCTR_INPT_domain")

	OTC_DRVTV_HDG_ACCNTNG_STNDRD_TYP_domain = {		"1":"Over_the_counter_OTC_Derivative_as_a_hedge_according_to_International_Financial_Reporting_Standard_IFRS",
		"2":"Over_the_counter_OTC_Derivative_as_a_hedge_according_to_national_general_accepted_accounting_principles_nGAAP",
}

	OTC_DRVTV_HDG_ACCNTNG_STNDRD_TYP = models.CharField("OTC_DRVTV_HDG_ACCNTNG_STNDRD_TYP",max_length=255, choices=OTC_DRVTV_HDG_ACCNTNG_STNDRD_TYP_domain,default=None, blank=True, null=True, db_comment="OTC_DRVTV_HDG_ACCNTNG_STNDRD_TYP_domain")

	TYP_HDG_BIRD_domain = {		"1":"Fair_value_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_a",
		"11":"Hedges_other_than_cash_flow_hedge_and_hedge_of_net_investment_in_a_foreign_operation_Economic_hedge",
		"12":"Economic_hedge_With_use_of_fair_value_option",
		"13":"Economic_hedge_Other",
		"2":"Cash_flow_hedge_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_b",
		"3":"Hedge_of_a_net_investment_in_a_foreign_operation_Hedging_relationship_as_defined_in_IFRS_9_6_5_2_c",
		"4":"Portfolio_fair_value_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"5":"Portfolio_cash_flow_hedges_of_interest_rate_risk_Hedging_relationship_as_defined_in_IAS39_AG_114_132",
		"6":"Cost_price_hedge_Hedging_relationship_as_defined_in_Reg_680_2014_Annex_V_part_2_114_This_hedging_relationship_is_applicable_only_under_nGAAP_based_on_BAD",
		"7":"Other_than_Fair_value_hedge_Cash_flow_hedge_Hedge_of_a_net_investment_in_a_foreign_operation_Portfolio_fair_value_hedges_of_interest_rate_risk_Portfolio_cash_flow_hedges_of_interest_rate_risk_Cost_price_hedge_Other_applicable_hedging_relationship_for_nGAAP_based_on_BAD_reporters",
}

	TYP_HDG = models.CharField("TYP_HDG",max_length=255, choices=TYP_HDG_BIRD_domain,default=None, blank=True, null=True, db_comment="TYP_HDG_BIRD_domain")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="OTC_DRVTV_HDG_to_theINSTRMNTs")

	class Meta:

		verbose_name = 'OTC_DRVTV_HDG'

		verbose_name_plural = 'OTC_DRVTV_HDGs'

class OTC_DRVTV_INSTRMNT_SNTHTC_SCRTSTN_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	OTC_DRVTV_INSTRMNT_SNTHTC_SCRTSTN_ASSGNMNT_uniqueID = models.CharField("OTC_DRVTV_INSTRMNT_SNTHTC_SCRTSTN_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSTN_ID = models.CharField("SCRTSTN_ID",max_length=255,default=None, blank=True, null=True)

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="OTC_DRVTV_INSTRMNT_SNTHTC_SCRTSTN_ASSGNMNT_to_theINSTRMNTs")

	theSNTHTC_SCRTSTN = models.ForeignKey("SNTHTC_SCRTSTN", models.SET_NULL,blank=True,null=True,related_name="OTC_DRVTV_INSTRMNT_SNTHTC_SCRTSTN_ASSGNMNT_to_theSNTHTC_SCRTSTNs")

	class Meta:

		verbose_name = 'OTC_DRVTV_INSTRMNT_SNTHTC_SCRTSTN_ASSGNMNT'

		verbose_name_plural = 'OTC_DRVTV_INSTRMNT_SNTHTC_SCRTSTN_ASSGNMNTs'

class OTHR_PRTY_ID(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	OTHR_PRTY_ID_uniqueID = models.CharField("OTHR_PRTY_ID_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTY_CD_TYP_domain = {		"1":"Legal_entity_identifier_party_code",
		"2":"Register_of_Institutions_and_Affiliates_Database_RIAD_party_code",
		"3":"Other_party_code",
}

	PRTY_CD_TYP = models.CharField("PRTY_CD_TYP",max_length=255, choices=PRTY_CD_TYP_domain,default=None, blank=True, null=True, db_comment="PRTY_CD_TYP_domain")

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	EXTRNL_PRTY_ID_TYP_domain = {		"10":"Other_Non_LEI_code",
		"11":"Public_sector_entity_identifier",
		"12":"TAX_Code",
		"13":"Trade_register_identifier",
		"14":"Value_added_tax_identifier",
		"2":"RIAD_Code",
		"3":"BIC_code",
		"4":"Other",
		"5":"Identifier_assigned_by_the_National_Central_Bank",
		"6":"Investment_Pension_fund_identifier",
		"7":"National_Business_register_identifier",
		"8":"National_Statistical_Institute_number",
		"9":"National_Supervisory_Authority_code",
}

	PRTY_ID_TYP = models.CharField("PRTY_ID_TYP",max_length=255, choices=EXTRNL_PRTY_ID_TYP_domain,default=None, blank=True, null=True, db_comment="EXTRNL_PRTY_ID_TYP_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	OTHR_PRTY_CD = models.CharField("OTHR_PRTY_CD",max_length=255,default=None, blank=True, null=True)

	thePRTY_CD = models.ForeignKey("PRTY_CD", models.SET_NULL,blank=True,null=True,related_name="OTHR_PRTY_ID_to_thePRTY_CDs")

	class Meta:

		verbose_name = 'OTHR_PRTY_ID'

		verbose_name_plural = 'OTHR_PRTY_IDs'

class PRTCTN_ARRNGMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	PRTCTN_ARRNGMNT_uniqueID = models.CharField("PRTCTN_ARRNGMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTCTN_ID = models.CharField("PRTCTN_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	RSDL_MTRTY_BND_domain = {		"12":"_3m_6m",
		"16":"_6m_12m",
		"21":"_1y_2y",
		"28":"_2y_3y",
		"3":"_1d_1w",
		"31":"_3y_5y",
		"36":"_5y_10y",
		"40":"Over_10_years",
		"64":"_0d_1d",
		"81":"_gt_7_days_lt_eq_14_days",
		"82":"_gt_2_weeks_lt_eq_1_month",
		"9":"_1m_3m",
		"999":"Open_maturity",
}

	ASST_ENCMBRNC_RSDL_MTRTY_BND = models.CharField("ASST_ENCMBRNC_RSDL_MTRTY_BND",max_length=255, choices=RSDL_MTRTY_BND_domain,default=None, blank=True, null=True, db_comment="RSDL_MTRTY_BND_domain")

	DT_MTRTY_PRTCTN = models.DateTimeField("DT_MTRTY_PRTCTN",default=None, blank=True, null=True)

	PRTCTN_ARRNGMNT_RS_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Protection_arrangement_instrument_used_once",
		"2":"Protection_arrangement_instrument_reused",
}

	PRTCTN_ARRNGMNT_RS_INDCTR = models.CharField("PRTCTN_ARRNGMNT_RS_INDCTR",max_length=255, choices=PRTCTN_ARRNGMNT_RS_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="PRTCTN_ARRNGMNT_RS_INDCTR_INPT_domain")

	PRTCN_ARRNGMNT_TYP_domain = {		"6":"Credit_risk_mitigation_arrangement",
		"7":"Collateral_annex",
}

	PRTCTN_ARRNGMNT_TYP = models.CharField("PRTCTN_ARRNGMNT_TYP",max_length=255, choices=PRTCN_ARRNGMNT_TYP_domain,default=None, blank=True, null=True, db_comment="PRTCN_ARRNGMNT_TYP_domain")

	class Meta:

		verbose_name = 'PRTCTN_ARRNGMNT'

		verbose_name_plural = 'PRTCTN_ARRNGMNTs'

class PRTCTN_ARRNGMNT_RL(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	PRTCTN_ARRNGMNT_RL_uniqueID = models.CharField("PRTCTN_ARRNGMNT_RL_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTCTN_ARRNGMNT_RL_TYP_domain = {		"0":"Not_applicable",
		"1":"Protection_arrangement_received",
		"2":"Protection_arrangement_given",
}

	PRTCTN_ARRNGMNT_RL_TYP = models.CharField("PRTCTN_ARRNGMNT_RL_TYP",max_length=255, choices=PRTCTN_ARRNGMNT_RL_TYP_domain,default=None, blank=True, null=True, db_comment="PRTCTN_ARRNGMNT_RL_TYP_domain")

	PRTCTN_ID = models.CharField("PRTCTN_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	AVLBL_ENCMBRNC_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Available_for_encumbrance",
		"2":"Not_available_for_encumbrance",
}

	AVLBL_ENCMBRNC_INDCTR = models.CharField("AVLBL_ENCMBRNC_INDCTR",max_length=255, choices=AVLBL_ENCMBRNC_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="AVLBL_ENCMBRNC_INDCTR_INPT_domain")

	thePRTCTN_ARRNGMNT = models.ForeignKey("PRTCTN_ARRNGMNT", models.SET_NULL,blank=True,null=True,related_name="PRTCTN_ARRNGMNT_RL_to_thePRTCTN_ARRNGMNTs")

	class Meta:

		verbose_name = 'PRTCTN_ARRNGMNT_RL'

		verbose_name_plural = 'PRTCTN_ARRNGMNT_RLs'

class PRTCTN_PRTCTN_PRVD_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	PRTCTN_PRTCTN_PRVD_ASSGNMNT_uniqueID = models.CharField("PRTCTN_PRTCTN_PRVD_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTCTN_ID = models.CharField("PRTCTN_ID",max_length=255,default=None, blank=True, null=True)

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	PRTY_RL_TYP = models.CharField("PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	PRMRY_PRTCTN_PRVDR_INDCTR_domain = {		"1":"Primary_protection_provider",
		"2":"Not_primary_protection_provider",
}

	PRMRY_PRTCTN_PRVDR_INDCTR = models.CharField("PRMRY_PRTCTN_PRVDR_INDCTR",max_length=255, choices=PRMRY_PRTCTN_PRVDR_INDCTR_domain,default=None, blank=True, null=True, db_comment="PRMRY_PRTCTN_PRVDR_INDCTR_domain")

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="PRTCTN_PRTCTN_PRVD_ASSGNMNT_to_theENTTY_RLs")

	thePRTCTN_ARRNGMNT = models.ForeignKey("PRTCTN_ARRNGMNT", models.SET_NULL,blank=True,null=True,related_name="PRTCTN_PRTCTN_PRVD_ASSGNMNT_to_thePRTCTN_ARRNGMNTs")

	class Meta:

		verbose_name = 'PRTCTN_PRTCTN_PRVD_ASSGNMNT'

		verbose_name_plural = 'PRTCTN_PRTCTN_PRVD_ASSGNMNTs'

class PRTNR_ENTRPRS_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	PRTNR_ENTRPRS_ASSGNMNT_uniqueID = models.CharField("PRTNR_ENTRPRS_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CNTR_BNK_PRVT_SCTR_CMPNY_PRTY_ID = models.CharField("CNTR_BNK_PRVT_SCTR_CMPNY_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	OTHR_ORGNSTN_RL_TYP = models.CharField("OTHR_ORGNSTN_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	PRTNR_ENTRPRS_PRTY_ID = models.CharField("PRTNR_ENTRPRS_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	VTNG_RGHT = models.FloatField("VTNG_RGHT",default=None, blank=True, null=True)

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="PRTNR_ENTRPRS_ASSGNMNT_to_theENTTY_RLs")

	thePRTY = models.ForeignKey("PRTY", models.SET_NULL,blank=True,null=True,related_name="PRTNR_ENTRPRS_ASSGNMNT_to_thePRTYs")

	class Meta:

		verbose_name = 'PRTNR_ENTRPRS_ASSGNMNT'

		verbose_name_plural = 'PRTNR_ENTRPRS_ASSGNMNTs'

class PRTY(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	PRTY_uniqueID = models.CharField("PRTY_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ANNL_TRNVR = models.BigIntegerField("ANNL_TRNVR",default=None, blank=True, null=True)

	GGRPHCL_ARS_SHSG4_ENTITY_1_CNTRY_REF_domain = {		"4A":"All_the_European_Union_Institutions_excluding_the_institutions_of_the_euro_area_changing_composition",
		"9A":"International_Organisations_excluding_European_Union_Institutions",
		"AD":"Andorra",
		"AE":"United_Arab_Emirates_the",
		"AF":"Afghanistan",
		"AG":"Antigua_and_Barbuda",
		"AI":"Anguilla",
		"AL":"Albania",
		"AM":"Armenia",
		"AN":"Netherlands_Antilles",
		"AO":"Angola",
		"AQ":"Antarctica",
		"AR":"Argentina",
		"AS":"American_Samoa",
		"AT":"Austria",
		"AU":"Australia",
		"AW":"Aruba",
		"AZ":"Azerbaijan",
		"BA":"Bosnia_and_Herzegovina",
		"BB":"Barbados",
		"BD":"Bangladesh",
		"BE":"Belgium",
		"BF":"Burkina_Faso",
		"BG":"Bulgaria",
		"BH":"Bahrain",
		"BI":"Burundi",
		"BJ":"Benin",
		"BL":"Saint_Barthelemy",
		"BM":"Bermuda",
		"BN":"Brunei_Darussalam",
		"BO":"Bolivia_Plurinational_State_of",
		"BQ":"Bonaire_Saint_Eustatius_and_Saba",
		"BR":"Brazil",
		"BS":"Bahamas_the",
		"BT":"Bhutan",
		"BV":"Bouvet_Island",
		"BW":"Botswana",
		"BY":"Belarus",
		"BZ":"Belize",
		"CA":"Canada",
		"CC":"Cocos_Keeling_Islands_the",
		"CD":"Congo_the_Democratic_Republic_of_the",
		"CF":"Central_African_Republic_the",
		"CG":"Congo_the",
		"CH":"Switzerland",
		"CI":"Cote_d_Ivoire",
		"CK":"Cook_Islands_the",
		"CL":"Chile",
		"CM":"Cameroon",
		"CN":"China_China_excluding_Taiwan_TW_Hong_Kong_HK_Macao_MO",
		"CO":"Colombia",
		"CR":"Costa_Rica",
		"CS":"Serbia_and_Montenegro",
		"CU":"Cuba",
		"CV":"Cabo_Verde",
		"CW":"Curacao",
		"CX":"Christmas_Island",
		"CY":"Cyprus",
		"CZ":"Czechia",
		"D09":"Extra_EU_changing_composition_not_allocated",
		"DE":"Germany",
		"DJ":"Djibouti",
		"DK":"Denmark",
		"DM":"Dominica",
		"DO":"Dominican_Republic_the",
		"DZ":"Algeria",
		"EC":"Ecuador",
		"EE":"Estonia",
		"EG":"Egypt",
		"EH":"Western_Sahara",
		"ER":"Eritrea",
		"ES":"Spain",
		"ET":"Ethiopia",
		"FIext":"Finland_Aland_Islands",
		"FJ":"Fiji",
		"FK":"Falkland_Islands_the_Malvinas",
		"FM":"Micronesia_Federated_States_of",
		"FO":"Faroe_Islands_the",
		"FRext":"France_Monaco_French_overseas_departments_Saint_Pierre_et_Miquelon_Mayotte",
		"GA":"Gabon",
		"GB":"United_Kingdom_of_Great_Britain_and_Northern_Ireland_the",
		"GD":"Grenada",
		"GE":"Georgia",
		"GG":"Guernsey",
		"GH":"Ghana",
		"GI":"Gibraltar",
		"GL":"Greenland",
		"GM":"Gambia_the",
		"GN":"Guinea",
		"GQ":"Equatorial_Guinea",
		"GR":"Greece",
		"GS":"South_Georgia_and_the_South_Sandwich_Islands",
		"GT":"Guatemala",
		"GU":"Guam",
		"GW":"Guinea_Bissau",
		"GY":"Guyana",
		"HK":"Hong_Kong",
		"HM":"Heard_Island_and_McDonald_Islands",
		"HN":"Honduras",
		"HR":"Croatia",
		"HT":"Haiti",
		"HU":"Hungary",
		"ID":"Indonesia",
		"IE":"Ireland",
		"IL":"Israel",
		"IM":"Isle_of_Man",
		"IN":"India",
		"IO":"British_Indian_Ocean_Territory_the",
		"IQ":"Iraq",
		"IR":"Iran_Islamic_Republic_of",
		"IS":"Iceland",
		"IT":"Italy",
		"JE":"Jersey",
		"JM":"Jamaica",
		"JO":"Jordan",
		"JP":"Japan",
		"KE":"Kenya",
		"KG":"Kyrgyzstan",
		"KH":"Cambodia",
		"KI":"Kiribati",
		"KM":"Comoros_the",
		"KN":"Saint_Kitts_and_Nevis",
		"KP":"Korea_the_Democratic_People_s_Republic_of",
		"KR":"Korea_the_Republic_of",
		"KW":"Kuwait",
		"KY":"Cayman_Islands_the",
		"KZ":"Kazakhstan",
		"LA":"Lao_People_s_Democratic_Republic_the",
		"LB":"Lebanon",
		"LC":"Saint_Lucia",
		"LI":"Liechtenstein",
		"LK":"Sri_Lanka",
		"LR":"Liberia",
		"LS":"Lesotho",
		"LT":"Lithuania",
		"LU":"Luxembourg",
		"LV":"Latvia",
		"LY":"Libya",
		"MA":"Morocco",
		"MD":"Moldova_the_Republic_of",
		"ME":"Montenegro",
		"MF":"Saint_Martin_French_part",
		"MG":"Madagascar",
		"MH":"Marshall_Islands_the",
		"MK":"Macedonia_the_former_Yugoslav_Republic_of",
		"ML":"Mali",
		"MM":"Myanmar",
		"MN":"Mongolia",
		"MO":"Macao",
		"MP":"Northern_Mariana_Islands_the",
		"MR":"Mauritania",
		"MS":"Montserrat",
		"MT":"Malta",
		"MU":"Mauritius",
		"MV":"Maldives",
		"MW":"Malawi",
		"MX":"Mexico",
		"MY":"Malaysia",
		"MZ":"Mozambique",
		"NA":"Namibia",
		"NC":"New_Caledonia",
		"NE":"Niger_the",
		"NF":"Norfolk_Island",
		"NG":"Nigeria",
		"NI":"Nicaragua",
		"NL":"Netherlands_the_Netherlands_excluding_Aruba_AW_Bonaire_Saint_Eustatius_and_Saba_BQ_Curacao_CW_Sint_Maarten_SX",
		"NO":"Norway_Norway_excluding_Svalbard_and_Jan_Mayen_SJ",
		"NP":"Nepal",
		"NR":"Nauru",
		"NU":"Niue",
		"NZ":"New_Zealand",
		"OM":"Oman",
		"PA":"Panama",
		"PE":"Peru",
		"PF":"French_Polynesia",
		"PG":"Papua_New_Guinea",
		"PH":"Philippines_the",
		"PK":"Pakistan",
		"PL":"Poland",
		"PN":"Pitcairn",
		"PR":"Puerto_Rico",
		"PS":"Palestine_State_of",
		"PT":"Portugal",
		"PW":"Palau",
		"PY":"Paraguay",
		"QA":"Qatar",
		"RO":"Romania",
		"RS":"Serbia",
		"RU":"Russian_Federation_the",
		"RW":"Rwanda",
		"SA":"Saudi_Arabia",
		"SB":"Solomon_Islands",
		"SC":"Seychelles",
		"SD":"Sudan_the",
		"SE":"Sweden",
		"SG":"Singapore",
		"SH":"Saint_Helena_Ascension_and_Tristan_da_Cunha",
		"SI":"Slovenia",
		"SJ":"Svalbard_and_Jan_Mayen",
		"SK":"Slovakia",
		"SL":"Sierra_Leone",
		"SM":"San_Marino",
		"SN":"Senegal",
		"SO":"Somalia",
		"SR":"Suriname",
		"SS":"South_Sudan",
		"ST":"Sao_Tome_and_Principe",
		"SV":"El_Salvador",
		"SX":"Sint_Maarten_Dutch_part",
		"SY":"Syrian_Arab_Republic",
		"SZ":"Swaziland",
		"TC":"Turks_and_Caicos_Islands_the",
		"TD":"Chad",
		"TF":"French_Southern_Territories_the",
		"TG":"Togo",
		"TH":"Thailand",
		"TJ":"Tajikistan",
		"TK":"Tokelau",
		"TL":"Timor_Leste",
		"TM":"Turkmenistan",
		"TN":"Tunisia",
		"TO":"Tonga",
		"TR":"Turkey",
		"TT":"Trinidad_and_Tobago",
		"TV":"Tuvalu",
		"TW":"Taiwan_Province_of_China",
		"TZ":"Tanzania_United_Republic_of",
		"U29":"Euro_area_Member_States_and_Institutions_of_the_Euro_Area_changing_composition_not_allocated",
		"U39":"Intra_EU_Extra_Euro_Area_changing_composition_not_allocated",
		"UA":"Ukraine",
		"UG":"Uganda",
		"UM":"United_States_Minor_Outlying_Islands_the",
		"US":"United_States_of_America_the_United_States_excluding_American_Samoa_AS_Guam_GU_Northern_Mariana_Islands_MP_Puerto_Rico_PR_United_States_Minor_Outlying_Islands_UM_Virgin_Islands_U_S_VI",
		"UY":"Uruguay",
		"UZ":"Uzbekistan",
		"VA":"Holy_See_the",
		"VC":"Saint_Vincent_and_the_Grenadines",
		"VE":"Venezuela_Bolivarian_Republic_of",
		"VG":"Virgin_Islands_British",
		"VI":"Virgin_Islands_U_S",
		"VN":"Viet_Nam",
		"VU":"Vanuatu",
		"WF":"Wallis_and_Futuna",
		"WS":"Samoa",
		"XK":"Kosovo",
		"YE":"Yemen",
		"ZA":"South_Africa",
		"ZM":"Zambia",
		"ZW":"Zimbabwe",
		"_X":"Not_allocated_unspecified_not_assigned",
}

	AREA_ISSR_SHS = models.CharField("AREA_ISSR_SHS",max_length=255, choices=GGRPHCL_ARS_SHSG4_ENTITY_1_CNTRY_REF_domain,default=None, blank=True, null=True, db_comment="GGRPHCL_ARS_SHSG4_ENTITY_1_CNTRY_REF_domain")

	BLNC_SHT_TTL = models.BigIntegerField("BLNC_SHT_TTL",default=None, blank=True, null=True)

	ISO3166_INPT_domain = {		"0":"Not_applicable",
		"AD":"Andorra",
		"AE":"United_Arab_Emirates_the",
		"AF":"Afghanistan",
		"AG":"Antigua_and_Barbuda",
		"AI":"Anguilla",
		"AL":"Albania",
		"AM":"Armenia",
		"AO":"Angola",
		"AQ":"Antarctica",
		"AR":"Argentina",
		"AS":"American_Samoa",
		"AT":"Austria",
		"AU":"Australia",
		"AW":"Aruba",
		"AX":"Aland_Islands",
		"AZ":"Azerbaijan",
		"BA":"Bosnia_and_Herzegovina",
		"BB":"Barbados",
		"BD":"Bangladesh",
		"BE":"Belgium",
		"BF":"Burkina_Faso",
		"BG":"Bulgaria",
		"BH":"Bahrain",
		"BI":"Burundi",
		"BJ":"Benin",
		"BL":"Saint_Barthelemy",
		"BM":"Bermuda",
		"BN":"Brunei_Darussalam",
		"BO":"Bolivia_Plurinational_State_of",
		"BQ":"Bonaire_Saint_Eustatius_and_Saba",
		"BR":"Brazil",
		"BS":"Bahamas_the",
		"BT":"Bhutan",
		"BV":"Bouvet_Island",
		"BW":"Botswana",
		"BY":"Belarus",
		"BZ":"Belize",
		"CA":"Canada",
		"CC":"Cocos_Keeling_Islands_the",
		"CD":"Congo_the_Democratic_Republic_of_the",
		"CF":"Central_African_Republic_the",
		"CG":"Congo_the",
		"CH":"Switzerland",
		"CI":"Cote_d_Ivoire",
		"CK":"Cook_Islands_the",
		"CL":"Chile",
		"CM":"Cameroon",
		"CN":"China_China_excluding_Taiwan_TW_Hong_Kong_HK_Macao_MO",
		"CO":"Colombia",
		"CR":"Costa_Rica",
		"CU":"Cuba",
		"CV":"Cabo_Verde",
		"CW":"Curacao",
		"CX":"Christmas_Island",
		"CY":"Cyprus",
		"CZ":"Czechia",
		"DE":"Germany",
		"DJ":"Djibouti",
		"DK":"Denmark",
		"DM":"Dominica",
		"DO":"Dominican_Republic_the",
		"DZ":"Algeria",
		"EC":"Ecuador",
		"EE":"Estonia",
		"EG":"Egypt",
		"EH":"Western_Sahara",
		"ER":"Eritrea",
		"ES":"Spain",
		"ET":"Ethiopia",
		"FI":"Finland_Finland_excluding_Aland_AX",
		"FJ":"Fiji",
		"FK":"Falkland_Islands_the_Malvinas",
		"FM":"Micronesia_Federated_States_of",
		"FO":"Faroe_Islands_the",
		"FR":"France_France_excluding_Guadeloupe_GP_Guyane_GF_La_Reunion_RE_Martinique_MQ_Mayotte_YT_Nouvelle_Caledonie_NC_Polynesie_francaise_PF_Saint_Barthelemy_BL_Saint_Martin_MF_Saint_Pierre_et_Miquelon_PM_Terres_australes_francaises_TF_Wallis_et_Futuna_WF",
		"GA":"Gabon",
		"GB":"United_Kingdom_of_Great_Britain_and_Northern_Ireland_the",
		"GD":"Grenada",
		"GE":"Georgia",
		"GF":"French_Guiana",
		"GG":"Guernsey",
		"GH":"Ghana",
		"GI":"Gibraltar",
		"GL":"Greenland",
		"GM":"Gambia_the",
		"GN":"Guinea",
		"GP":"Guadeloupe",
		"GQ":"Equatorial_Guinea",
		"GR":"Greece",
		"GS":"South_Georgia_and_the_South_Sandwich_Islands",
		"GT":"Guatemala",
		"GU":"Guam",
		"GW":"Guinea_Bissau",
		"GY":"Guyana",
		"HK":"Hong_Kong",
		"HM":"Heard_Island_and_McDonald_Islands",
		"HN":"Honduras",
		"HR":"Croatia",
		"HT":"Haiti",
		"HU":"Hungary",
		"ID":"Indonesia",
		"IE":"Ireland",
		"IL":"Israel",
		"IM":"Isle_of_Man",
		"IN":"India",
		"IO":"British_Indian_Ocean_Territory_the",
		"IQ":"Iraq",
		"IR":"Iran_Islamic_Republic_of",
		"IS":"Iceland",
		"IT":"Italy",
		"JE":"Jersey",
		"JM":"Jamaica",
		"JO":"Jordan",
		"JP":"Japan",
		"KE":"Kenya",
		"KG":"Kyrgyzstan",
		"KH":"Cambodia",
		"KI":"Kiribati",
		"KM":"Comoros_the",
		"KN":"Saint_Kitts_and_Nevis",
		"KP":"Korea_the_Democratic_People_s_Republic_of",
		"KR":"Korea_the_Republic_of",
		"KW":"Kuwait",
		"KY":"Cayman_Islands_the",
		"KZ":"Kazakhstan",
		"LA":"Lao_People_s_Democratic_Republic_the",
		"LB":"Lebanon",
		"LC":"Saint_Lucia",
		"LI":"Liechtenstein",
		"LK":"Sri_Lanka",
		"LR":"Liberia",
		"LS":"Lesotho",
		"LT":"Lithuania",
		"LU":"Luxembourg",
		"LV":"Latvia",
		"LY":"Libya",
		"MA":"Morocco",
		"MC":"Monaco",
		"MD":"Moldova_the_Republic_of",
		"ME":"Montenegro",
		"MF":"Saint_Martin_French_part",
		"MG":"Madagascar",
		"MH":"Marshall_Islands_the",
		"MK":"Macedonia_the_former_Yugoslav_Republic_of",
		"ML":"Mali",
		"MM":"Myanmar",
		"MN":"Mongolia",
		"MO":"Macao",
		"MP":"Northern_Mariana_Islands_the",
		"MQ":"Martinique",
		"MR":"Mauritania",
		"MS":"Montserrat",
		"MT":"Malta",
		"MU":"Mauritius",
		"MV":"Maldives",
		"MW":"Malawi",
		"MX":"Mexico",
		"MY":"Malaysia",
		"MZ":"Mozambique",
		"NA":"Namibia",
		"NC":"New_Caledonia",
		"NE":"Niger_the",
		"NF":"Norfolk_Island",
		"NG":"Nigeria",
		"NI":"Nicaragua",
		"NL":"Netherlands_the_Netherlands_excluding_Aruba_AW_Bonaire_Saint_Eustatius_and_Saba_BQ_Curacao_CW_Sint_Maarten_SX",
		"NO":"Norway_Norway_excluding_Svalbard_and_Jan_Mayen_SJ",
		"NP":"Nepal",
		"NR":"Nauru",
		"NU":"Niue",
		"NZ":"New_Zealand",
		"OM":"Oman",
		"PA":"Panama",
		"PE":"Peru",
		"PF":"French_Polynesia",
		"PG":"Papua_New_Guinea",
		"PH":"Philippines_the",
		"PK":"Pakistan",
		"PL":"Poland",
		"PM":"Saint_Pierre_and_Miquelon",
		"PN":"Pitcairn",
		"PR":"Puerto_Rico",
		"PS":"Palestine_State_of",
		"PT":"Portugal",
		"PW":"Palau",
		"PY":"Paraguay",
		"QA":"Qatar",
		"RE":"Reunion",
		"RO":"Romania",
		"RS":"Serbia",
		"RU":"Russian_Federation_the",
		"RW":"Rwanda",
		"SA":"Saudi_Arabia",
		"SB":"Solomon_Islands",
		"SC":"Seychelles",
		"SD":"Sudan_the",
		"SE":"Sweden",
		"SG":"Singapore",
		"SH":"Saint_Helena_Ascension_and_Tristan_da_Cunha",
		"SI":"Slovenia",
		"SJ":"Svalbard_and_Jan_Mayen",
		"SK":"Slovakia",
		"SL":"Sierra_Leone",
		"SM":"San_Marino",
		"SN":"Senegal",
		"SO":"Somalia",
		"SR":"Suriname",
		"SS":"South_Sudan",
		"ST":"Sao_Tome_and_Principe",
		"SV":"El_Salvador",
		"SX":"Sint_Maarten_Dutch_part",
		"SY":"Syrian_Arab_Republic",
		"SZ":"Swaziland",
		"TC":"Turks_and_Caicos_Islands_the",
		"TD":"Chad",
		"TF":"French_Southern_Territories_the",
		"TG":"Togo",
		"TH":"Thailand",
		"TJ":"Tajikistan",
		"TK":"Tokelau",
		"TL":"Timor_Leste",
		"TM":"Turkmenistan",
		"TN":"Tunisia",
		"TO":"Tonga",
		"TR":"Turkey",
		"TT":"Trinidad_and_Tobago",
		"TV":"Tuvalu",
		"TW":"Taiwan_Province_of_China",
		"TZ":"Tanzania_United_Republic_of",
		"UA":"Ukraine",
		"UG":"Uganda",
		"UM":"United_States_Minor_Outlying_Islands_the",
		"US":"United_States_of_America_the_United_States_excluding_American_Samoa_AS_Guam_GU_Northern_Mariana_Islands_MP_Puerto_Rico_PR_United_States_Minor_Outlying_Islands_UM_Virgin_Islands_U_S_VI",
		"UY":"Uruguay",
		"UZ":"Uzbekistan",
		"VA":"Holy_See_the",
		"VC":"Saint_Vincent_and_the_Grenadines",
		"VE":"Venezuela_Bolivarian_Republic_of",
		"VG":"Virgin_Islands_British",
		"VI":"Virgin_Islands_U_S",
		"VN":"Viet_Nam",
		"VU":"Vanuatu",
		"WF":"Wallis_and_Futuna",
		"WS":"Samoa",
		"YE":"Yemen",
		"YT":"Mayotte",
		"ZA":"South_Africa",
		"ZM":"Zambia",
		"ZW":"Zimbabwe",
}

	CNTRY_CD = models.CharField("CNTRY_CD",max_length=255, choices=ISO3166_INPT_domain,default=None, blank=True, null=True, db_comment="ISO3166_INPT_domain")

	CTY = models.CharField("CTY",max_length=255,default=None, blank=True, null=True)

	DFLT_STTS_domain = {		"14":"Not_in_default",
		"18":"Default_because_both_unlikely_to_pay_and_more_than_90_180_days_past_due",
		"19":"Default_because_unlikely_to_pay",
		"20":"Default_because_more_than_90_180_days_past_due",
}

	DFLT_STTS = models.CharField("DFLT_STTS",max_length=255, choices=DFLT_STTS_domain,default=None, blank=True, null=True, db_comment="DFLT_STTS_domain")

	DT_DFLT_STTS = models.DateTimeField("DT_DFLT_STTS",default=None, blank=True, null=True)

	DT_ENTRPRS_SZ = models.DateTimeField("DT_ENTRPRS_SZ",default=None, blank=True, null=True)

	DT_INTTN_LGL_PRCDNGS = models.DateTimeField("DT_INTTN_LGL_PRCDNGS",default=None, blank=True, null=True)

	NACE_LVLS2TO4_STGNG_domain = {		"-99":"Technical_null_Technical_member_to_represent_the_null_value",
		"01":"Crop_and_animal_production_hunting_and_related_service_activities",
		"01_1":"Growing_of_non_perennial_crops",
		"01_11":"Growing_of_cereals_except_rice_leguminous_crops_and_oil_seeds",
		"01_12":"Growing_of_rice",
		"01_13":"Growing_of_vegetables_and_melons_roots_and_tubers",
		"01_14":"Growing_of_sugar_cane",
		"01_15":"Growing_of_tobacco",
		"01_16":"Growing_of_fibre_crops",
		"01_19":"Growing_of_other_non_perennial_crops",
		"01_2":"Growing_of_perennial_crops",
		"01_21":"Growing_of_grapes",
		"01_22":"Growing_of_tropical_and_subtropical_fruits",
		"01_23":"Growing_of_citrus_fruits",
		"01_24":"Growing_of_pome_fruits_and_stone_fruits",
		"01_25":"Growing_of_other_tree_and_bush_fruits_and_nuts",
		"01_26":"Growing_of_oleaginous_fruits",
		"01_27":"Growing_of_beverage_crops",
		"01_28":"Growing_of_spices_aromatic_drug_and_pharmaceutical_crops",
		"01_29":"Growing_of_other_perennial_crops",
		"01_3":"Plant_propagation",
		"01_30":"Plant_propagation_x2",
		"01_4":"Animal_production",
		"01_41":"Raising_of_dairy_cattle",
		"01_42":"Raising_of_other_cattle_and_buffaloes",
		"01_43":"Raising_of_horses_and_other_equines",
		"01_44":"Raising_of_camels_and_camelids",
		"01_45":"Raising_of_sheep_and_goats",
		"01_46":"Raising_of_swine_pigs",
		"01_47":"Raising_of_poultry",
		"01_49":"Raising_of_other_animals",
		"01_5":"Mixed_farming",
		"01_50":"Mixed_farming_x2",
		"01_6":"Support_activities_to_agriculture_and_post_harvest_crop_activities",
		"01_61":"Support_activities_for_crop_production",
		"01_62":"Support_activities_for_animal_production",
		"01_63":"Post_harvest_crop_activities",
		"01_64":"Seed_processing_for_propagation",
		"01_7":"Hunting_trapping_and_related_service_activities",
		"01_70":"Hunting_trapping_and_related_service_activities_x2",
		"02":"Forestry_and_logging",
		"02_1":"Silviculture_and_other_forestry_activities",
		"02_10":"Silviculture_and_other_forestry_activities_x2",
		"02_2":"Logging",
		"02_20":"Logging_x2",
		"02_3":"Gathering_of_wild_growing_non_wood_products",
		"02_30":"Gathering_of_wild_growing_non_wood_products_x2",
		"02_4":"Support_services_to_forestry",
		"02_40":"Support_services_to_forestry_x2",
		"03":"Fishing_and_aquaculture",
		"03_1":"Fishing",
		"03_11":"Marine_fishing",
		"03_12":"Freshwater_fishing",
		"03_2":"Aquaculture",
		"03_21":"Marine_aquaculture",
		"03_22":"Freshwater_aquaculture",
		"05":"Mining_of_coal_and_lignite",
		"05_1":"Mining_of_hard_coal",
		"05_10":"Mining_of_hard_coal_x2",
		"05_2":"Mining_of_lignite",
		"05_20":"Mining_of_lignite_x2",
		"06":"Extraction_of_crude_petroleum_and_natural_gas",
		"06_1":"Extraction_of_crude_petroleum",
		"06_10":"Extraction_of_crude_petroleum_x2",
		"06_2":"Extraction_of_natural_gas",
		"06_20":"Extraction_of_natural_gas_x2",
		"07":"Mining_of_metal_ores",
		"07_1":"Mining_of_iron_ores",
		"07_10":"Mining_of_iron_ores_x2",
		"07_2":"Mining_of_non_ferrous_metal_ores",
		"07_21":"Mining_of_uranium_and_thorium_ores",
		"07_29":"Mining_of_other_non_ferrous_metal_ores",
		"08":"Other_mining_and_quarrying",
		"08_1":"Quarrying_of_stone_sand_and_clay",
		"08_11":"Quarrying_of_ornamental_and_building_stone_limestone_gypsum_chalk_and_slate",
		"08_12":"Operation_of_gravel_and_sand_pits_mining_of_clays_and_kaolin",
		"08_9":"Mining_and_quarrying_n_e_c",
		"08_91":"Mining_of_chemical_and_fertiliser_minerals",
		"08_92":"Extraction_of_peat",
		"08_93":"Extraction_of_salt",
		"08_99":"Other_mining_and_quarrying_n_e_c",
		"09":"Mining_support_service_activities",
		"09_1":"Support_activities_for_petroleum_and_natural_gas_extraction",
		"09_10":"Support_activities_for_petroleum_and_natural_gas_extraction_x2",
		"09_9":"Support_activities_for_other_mining_and_quarrying",
		"09_90":"Support_activities_for_other_mining_and_quarrying_x2",
		"10":"Manufacture_of_food_products",
		"10_1":"Processing_and_preserving_of_meat_and_production_of_meat_products",
		"10_11":"Processing_and_preserving_of_meat",
		"10_12":"Processing_and_preserving_of_poultry_meat",
		"10_13":"Production_of_meat_and_poultry_meat_products",
		"10_2":"Processing_and_preserving_of_fish_crustaceans_and_molluscs",
		"10_20":"Processing_and_preserving_of_fish_crustaceans_and_molluscs_x2",
		"10_3":"Processing_and_preserving_of_fruit_and_vegetables",
		"10_31":"Processing_and_preserving_of_potatoes",
		"10_32":"Manufacture_of_fruit_and_vegetable_juice",
		"10_39":"Other_processing_and_preserving_of_fruit_and_vegetables",
		"10_4":"Manufacture_of_vegetable_and_animal_oils_and_fats",
		"10_41":"Manufacture_of_oils_and_fats",
		"10_42":"Manufacture_of_margarine_and_similar_edible_fats",
		"10_5":"Manufacture_of_dairy_products",
		"10_51":"Operation_of_dairies_and_cheese_making",
		"10_52":"Manufacture_of_ice_cream",
		"10_6":"Manufacture_of_grain_mill_products_starches_and_starch_products",
		"10_61":"Manufacture_of_grain_mill_products",
		"10_62":"Manufacture_of_starches_and_starch_products",
		"10_7":"Manufacture_of_bakery_and_farinaceous_products",
		"10_71":"Manufacture_of_bread_manufacture_of_fresh_pastry_goods_and_cakes",
		"10_72":"Manufacture_of_rusks_and_biscuits_manufacture_of_preserved_pastry_goods_and_cakes",
		"10_73":"Manufacture_of_macaroni_noodles_couscous_and_similar_farinaceous_products",
		"10_8":"Manufacture_of_other_food_products",
		"10_81":"Manufacture_of_sugar",
		"10_82":"Manufacture_of_cocoa_chocolate_and_sugar_confectionery",
		"10_83":"Processing_of_tea_and_coffee",
		"10_84":"Manufacture_of_condiments_and_seasonings",
		"10_85":"Manufacture_of_prepared_meals_and_dishes",
		"10_86":"Manufacture_of_homogenised_food_preparations_and_dietetic_food",
		"10_89":"Manufacture_of_other_food_products_n_e_c",
		"10_9":"Manufacture_of_prepared_animal_feeds",
		"10_91":"Manufacture_of_prepared_feeds_for_farm_animals",
		"10_92":"Manufacture_of_prepared_pet_foods",
		"11":"Manufacture_of_beverages",
		"11_0":"Manufacture_of_beverages_x2",
		"11_01":"Distilling_rectifying_and_blending_of_spirits",
		"11_02":"Manufacture_of_wine_from_grape",
		"11_03":"Manufacture_of_cider_and_other_fruit_wines",
		"11_04":"Manufacture_of_other_non_distilled_fermented_beverages",
		"11_05":"Manufacture_of_beer",
		"11_06":"Manufacture_of_malt",
		"11_07":"Manufacture_of_soft_drinks_production_of_mineral_waters_and_other_bottled_waters",
		"12":"Manufacture_of_tobacco_products",
		"12_0":"Manufacture_of_tobacco_products_x2",
		"12_00":"Manufacture_of_tobacco_products_x3",
		"13":"Manufacture_of_textiles",
		"13_1":"Preparation_and_spinning_of_textile_fibres",
		"13_10":"Preparation_and_spinning_of_textile_fibres_x2",
		"13_2":"Weaving_of_textiles",
		"13_20":"Weaving_of_textiles_x2",
		"13_3":"Finishing_of_textiles",
		"13_30":"Finishing_of_textiles_x2",
		"13_9":"Manufacture_of_other_textiles",
		"13_91":"Manufacture_of_knitted_and_crocheted_fabrics",
		"13_92":"Manufacture_of_made_up_textile_articles_except_apparel",
		"13_93":"Manufacture_of_carpets_and_rugs",
		"13_94":"Manufacture_of_cordage_rope_twine_and_netting",
		"13_95":"Manufacture_of_non_wovens_and_articles_made_from_non_wovens_except_apparel",
		"13_96":"Manufacture_of_other_technical_and_industrial_textiles",
		"13_99":"Manufacture_of_other_textiles_n_e_c",
		"14":"Manufacture_of_wearing_apparel",
		"14_1":"Manufacture_of_wearing_apparel_except_fur_apparel",
		"14_11":"Manufacture_of_leather_clothes",
		"14_12":"Manufacture_of_workwear",
		"14_13":"Manufacture_of_other_outerwear",
		"14_14":"Manufacture_of_underwear",
		"14_19":"Manufacture_of_other_wearing_apparel_and_accessories",
		"14_2":"Manufacture_of_articles_of_fur",
		"14_20":"Manufacture_of_articles_of_fur_x2",
		"14_3":"Manufacture_of_knitted_and_crocheted_apparel",
		"14_31":"Manufacture_of_knitted_and_crocheted_hosiery",
		"14_39":"Manufacture_of_other_knitted_and_crocheted_apparel",
		"15":"Manufacture_of_leather_and_related_products",
		"15_1":"Tanning_and_dressing_of_leather_manufacture_of_luggage_handbags_saddlery_and_harness_dressing_and_dyeing_of_fur",
		"15_11":"Tanning_and_dressing_of_leather_dressing_and_dyeing_of_fur",
		"15_12":"Manufacture_of_luggage_handbags_and_the_like_saddlery_and_harness",
		"15_2":"Manufacture_of_footwear",
		"15_20":"Manufacture_of_footwear_x2",
		"16":"Manufacture_of_wood_and_of_products_of_wood_and_cork_except_furniture_manufacture_of_articles_of_straw_and_plaiting_materials",
		"16_1":"Sawmilling_and_planing_of_wood",
		"16_10":"Sawmilling_and_planing_of_wood_x2",
		"16_2":"Manufacture_of_products_of_wood_cork_straw_and_plaiting_materials",
		"16_21":"Manufacture_of_veneer_sheets_and_wood_based_panels",
		"16_22":"Manufacture_of_assembled_parquet_floors",
		"16_23":"Manufacture_of_other_builders_carpentry_and_joinery",
		"16_24":"Manufacture_of_wooden_containers",
		"16_29":"Manufacture_of_other_products_of_wood_manufacture_of_articles_of_cork_straw_and_plaiting_materials",
		"17":"Manufacture_of_paper_and_paper_products",
		"17_1":"Manufacture_of_pulp_paper_and_paperboard",
		"17_11":"Manufacture_of_pulp",
		"17_12":"Manufacture_of_paper_and_paperboard",
		"17_2":"Manufacture_of_articles_of_paper_and_paperboard",
		"17_21":"Manufacture_of_corrugated_paper_and_paperboard_and_of_containers_of_paper_and_paperboard",
		"17_22":"Manufacture_of_household_and_sanitary_goods_and_of_toilet_requisites",
		"17_23":"Manufacture_of_paper_stationery",
		"17_24":"Manufacture_of_wallpaper",
		"17_29":"Manufacture_of_other_articles_of_paper_and_paperboard",
		"18":"Printing_and_reproduction_of_recorded_media",
		"18_1":"Printing_and_service_activities_related_to_printing",
		"18_11":"Printing_of_Newspapers",
		"18_12":"Other_printing",
		"18_13":"Pre_press_and_pre_media_services",
		"18_14":"Binding_and_related_services",
		"18_2":"Reproduction_of_recorded_media",
		"18_20":"Reproduction_of_recorded_media_x2",
		"19":"Manufacture_of_coke_and_refined_petroleum_products",
		"19_1":"Manufacture_of_coke_oven_products",
		"19_10":"Manufacture_of_coke_oven_products_x2",
		"19_2":"Manufacture_of_refined_petroleum_products",
		"19_20":"Manufacture_of_refined_petroleum_products_x2",
		"20":"Manufacture_of_chemicals_and_chemical_products",
		"20_1":"Manufacture_of_basic_chemicals_fertilisers_and_nitrogen_compounds_plastics_and_synthetic_rubber_in_primary_forms",
		"20_11":"Manufacture_of_industrial_gases",
		"20_12":"Manufacture_of_dyes_and_pigments",
		"20_13":"Manufacture_of_other_inorganic_basic_chemicals",
		"20_14":"Manufacture_of_other_organic_basic_chemicals",
		"20_15":"Manufacture_of_fertilisers_and_nitrogen_compounds",
		"20_16":"Manufacture_of_plastics_in_primary_forms",
		"20_17":"Manufacture_of_synthetic_rubber_in_primary_forms",
		"20_2":"Manufacture_of_pesticides_and_other_agrochemical_products",
		"20_20":"Manufacture_of_pesticides_and_other_agrochemical_products_x2",
		"20_3":"Manufacture_of_paints_varnishes_and_similar_coatings_printing_ink_and_mastics",
		"20_30":"Manufacture_of_paints_varnishes_and_similar_coatings_printing_ink_and_mastics_x2",
		"20_4":"Manufacture_of_soap_and_detergents_cleaning_and_polishing_preparations_perfumes_and_toilet_preparations",
		"20_41":"Manufacture_of_soap_and_detergents_cleaning_and_polishing_preparations",
		"20_42":"Manufacture_of_perfumes_and_toilet_preparations",
		"20_5":"Manufacture_of_other_chemical_products",
		"20_51":"Manufacture_of_explosives",
		"20_52":"Manufacture_of_glues",
		"20_53":"Manufacture_of_essential_oils",
		"20_59":"Manufacture_of_other_chemical_products_n_e_c",
		"20_6":"Manufacture_of_man_made_fibres",
		"20_60":"Manufacture_of_man_made_fibres_x2",
		"21":"Manufacture_of_basic_pharmaceutical_products_and_pharmaceutical_preparations",
		"21_1":"Manufacture_of_basic_pharmaceutical_products",
		"21_10":"Manufacture_of_basic_pharmaceutical_products_x2",
		"21_2":"Manufacture_of_pharmaceutical_preparations",
		"21_20":"Manufacture_of_pharmaceutical_preparations_x2",
		"22":"Manufacture_of_rubber_and_plastic_products",
		"22_1":"Manufacture_of_rubber_products",
		"22_11":"Manufacture_of_rubber_tyres_and_tubes_retreading_and_rebuilding_of_rubber_tyres",
		"22_19":"Manufacture_of_other_rubber_products",
		"22_2":"Manufacture_of_plastics_products",
		"22_21":"Manufacture_of_plastic_plates_sheets_tubes_and_profiles",
		"22_22":"Manufacture_of_plastic_packing_goods",
		"22_23":"Manufacture_of_builders_ware_of_plastic",
		"22_29":"Manufacture_of_other_plastic_products",
		"23":"Manufacture_of_other_non_metallic_mineral_products",
		"23_1":"Manufacture_of_glass_and_glass_products",
		"23_11":"Manufacture_of_flat_glass",
		"23_12":"Shaping_and_processing_of_flat_glass",
		"23_13":"Manufacture_of_hollow_glass",
		"23_14":"Manufacture_of_glass_fibres",
		"23_19":"Manufacture_and_processing_of_other_glass_including_technical_glassware",
		"23_2":"Manufacture_of_refractory_products",
		"23_20":"Manufacture_of_refractory_products_x2",
		"23_3":"Manufacture_of_clay_building_materials",
		"23_31":"Manufacture_of_ceramic_tiles_and_flags",
		"23_32":"Manufacture_of_bricks_tiles_and_construction_products_in_baked_clay",
		"23_4":"Manufacture_of_other_porcelain_and_ceramic_products",
		"23_41":"Manufacture_of_ceramic_household_and_ornamental_articles",
		"23_42":"Manufacture_of_ceramic_sanitary_fixtures",
		"23_43":"Manufacture_of_ceramic_insulators_and_insulating_fittings",
		"23_44":"Manufacture_of_other_technical_ceramic_products",
		"23_49":"Manufacture_of_other_ceramic_products",
		"23_5":"Manufacture_of_cement_lime_and_plaster",
		"23_51":"Manufacture_of_cement",
		"23_52":"Manufacture_of_lime_and_plaster",
		"23_6":"Manufacture_of_articles_of_concrete_cement_and_plaster",
		"23_61":"Manufacture_of_concrete_products_for_construction_purposes",
		"23_62":"Manufacture_of_plaster_products_for_construction_purposes",
		"23_63":"Manufacture_of_ready_mixed_concrete",
		"23_64":"Manufacture_of_mortars",
		"23_65":"Manufacture_of_fibre_cement",
		"23_69":"Manufacture_of_other_articles_of_concrete_plaster_and_cement",
		"23_7":"Cutting_shaping_and_finishing_of_stone",
		"23_70":"Cutting_shaping_and_finishing_of_stone_x2",
		"23_9":"Manufacture_of_abrasive_products_and_non_metallic_mineral_products_n_e_c",
		"23_91":"Production_of_abrasive_products",
		"23_99":"Manufacture_of_other_non_metallic_mineral_products_n_e_c",
		"24":"Manufacture_of_basic_metals",
		"24_1":"Manufacture_of_basic_iron_and_steel_and_of_ferro_alloys",
		"24_10":"Manufacture_of_basic_iron_and_steel_and_of_ferro_alloys_x2",
		"24_2":"Manufacture_of_tubes_pipes_hollow_profiles_and_related_fittings_of_steel",
		"24_20":"Manufacture_of_tubes_pipes_hollow_profiles_and_related_fittings_of_steel_x2",
		"24_3":"Manufacture_of_other_products_of_first_processing_of_steel",
		"24_31":"Cold_drawing_of_bars",
		"24_32":"Cold_rolling_of_narrow_strip",
		"24_33":"Cold_forming_or_folding",
		"24_34":"Cold_drawing_of_wire",
		"24_4":"Manufacture_of_basic_precious_and_other_non_ferrous_metals",
		"24_41":"Precious_metals_production",
		"24_42":"Aluminium_production",
		"24_43":"Lead_zinc_and_tin_production",
		"24_44":"Copper_production",
		"24_45":"Other_non_ferrous_metal_production",
		"24_46":"Processing_of_nuclear_fuel",
		"24_5":"Casting_of_metals",
		"24_51":"Casting_of_iron",
		"24_52":"Casting_of_steel",
		"24_53":"Casting_of_light_metals",
		"24_54":"Casting_of_other_non_ferrous_metals",
		"25":"Manufacture_of_fabricated_metal_products_except_machinery_and_equipment",
		"25_1":"Manufacture_of_structural_metal_products",
		"25_11":"Manufacture_of_metal_structures_and_parts_of_structures",
		"25_12":"Manufacture_of_doors_and_windows_of_metal",
		"25_2":"Manufacture_of_tanks_reservoirs_and_containers_of_metal",
		"25_21":"Manufacture_of_central_heating_radiators_and_boilers",
		"25_29":"Manufacture_of_other_tanks_reservoirs_and_containers_of_metal",
		"25_3":"Manufacture_of_steam_generators_except_central_heating_hot_water_boilers",
		"25_30":"Manufacture_of_steam_generators_except_central_heating_hot_water_boilers_x2",
		"25_4":"Manufacture_of_weapons_and_ammunition",
		"25_40":"Manufacture_of_weapons_and_ammunition_x2",
		"25_5":"Forging_pressing_stamping_and_roll_forming_of_metal_powder_metallurgy",
		"25_50":"Forging_pressing_stamping_and_roll_forming_of_metal_powder_metallurgy_x2",
		"25_6":"Treatment_and_coating_of_metals_machining",
		"25_61":"Treatment_and_coating_of_metals",
		"25_62":"Machining",
		"25_7":"Manufacture_of_cutlery_tools_and_general_hardware",
		"25_71":"Manufacture_of_cutlery",
		"25_72":"Manufacture_of_locks_and_hinges",
		"25_73":"Manufacture_of_tools",
		"25_9":"Manufacture_of_other_fabricated_metal_products",
		"25_91":"Manufacture_of_steel_drums_and_similar_containers",
		"25_92":"Manufacture_of_light_metal_packaging",
		"25_93":"Manufacture_of_wire_products_chain_and_springs",
		"25_94":"Manufacture_of_fasteners_and_screw_machine_products",
		"25_99":"Manufacture_of_other_fabricated_metal_products_n_e_c",
		"26":"Manufacture_of_computer_electronic_and_optical_products",
		"26_1":"Manufacture_of_electronic_components_and_boards",
		"26_11":"Manufacture_of_electronic_components",
		"26_12":"Manufacture_of_loaded_electronic_boards",
		"26_2":"Manufacture_of_computers_and_peripheral_equipment",
		"26_20":"Manufacture_of_computers_and_peripheral_equipment_x2",
		"26_3":"Manufacture_of_communication_equipment",
		"26_30":"Manufacture_of_communication_equipment_x2",
		"26_4":"Manufacture_of_consumer_electronics",
		"26_40":"Manufacture_of_consumer_electronics_x2",
		"26_5":"Manufacture_of_instruments_and_appliances_for_measuring_testing_and_navigation_watches_and_clocks",
		"26_51":"Manufacture_of_instruments_and_appliances_for_measuring_testing_and_navigation",
		"26_52":"Manufacture_of_watches_and_clocks",
		"26_6":"Manufacture_of_irradiation_electromedical_and_electrotherapeutic_equipment",
		"26_60":"Manufacture_of_irradiation_electromedical_and_electrotherapeutic_equipment_x2",
		"26_7":"Manufacture_of_optical_instruments_and_photographic_equipment",
		"26_70":"Manufacture_of_optical_instruments_and_photographic_equipment_x2",
		"26_8":"Manufacture_of_magnetic_and_optical_media",
		"26_80":"Manufacture_of_magnetic_and_optical_media_x2",
		"27":"Manufacture_of_electrical_equipment",
		"27_1":"Manufacture_of_electric_motors_generators_transformers_and_electricity_distribution_and_control_apparatus",
		"27_11":"Manufacture_of_electric_motors_generators_and_transformers",
		"27_12":"Manufacture_of_electricity_distribution_and_control_apparatus",
		"27_2":"Manufacture_of_batteries_and_accumulators",
		"27_20":"Manufacture_of_batteries_and_accumulators_x2",
		"27_3":"Manufacture_of_wiring_and_wiring_devices",
		"27_31":"Manufacture_of_fibre_optic_cables",
		"27_32":"Manufacture_of_other_electronic_and_electric_wires_and_cables",
		"27_33":"Manufacture_of_wiring_devices",
		"27_4":"Manufacture_of_electric_lighting_equipment",
		"27_40":"Manufacture_of_electric_lighting_equipment_x2",
		"27_5":"Manufacture_of_domestic_appliances",
		"27_51":"Manufacture_of_electric_domestic_appliances",
		"27_52":"Manufacture_of_non_electric_domestic_appliances",
		"27_9":"Manufacture_of_other_electrical_equipment",
		"27_90":"Manufacture_of_other_electrical_equipment_x2",
		"28":"Manufacture_of_machinery_and_equipment_n_e_c",
		"28_1":"Manufacture_of_general_purpose_machinery",
		"28_11":"Manufacture_of_engines_and_turbines_except_aircraft_vehicle_and_cycle_engines",
		"28_12":"Manufacture_of_fluid_power_equipment",
		"28_13":"Manufacture_of_other_pumps_and_compressors",
		"28_14":"Manufacture_of_other_taps_and_valves",
		"28_15":"Manufacture_of_bearings_gears_gearing_and_driving_elements",
		"28_2":"Manufacture_of_other_general_purpose_machinery",
		"28_21":"Manufacture_of_ovens_furnaces_and_furnace_burners",
		"28_22":"Manufacture_of_lifting_and_handling_equipment",
		"28_23":"Manufacture_of_office_machinery_and_equipment_except_computers_and_peripheral_equipment",
		"28_24":"Manufacture_of_power_driven_hand_tools",
		"28_25":"Manufacture_of_non_domestic_cooling_and_ventilation_equipment",
		"28_29":"Manufacture_of_other_general_purpose_machinery_n_e_c",
		"28_3":"Manufacture_of_agricultural_and_forestry_machinery",
		"28_30":"Manufacture_of_agricultural_and_forestry_machinery_x2",
		"28_4":"Manufacture_of_metal_forming_machinery_and_machine_tools",
		"28_41":"Manufacture_of_metal_forming_machinery",
		"28_49":"Manufacture_of_other_machine_tools",
		"28_9":"Manufacture_of_other_special_purpose_machinery",
		"28_91":"Manufacture_of_machinery_for_metallurgy",
		"28_92":"Manufacture_of_machinery_for_mining_quarrying_and_construction",
		"28_93":"Manufacture_of_machinery_for_food_beverage_and_tobacco_processing",
		"28_94":"Manufacture_of_machinery_for_textile_apparel_and_leather_production",
		"28_95":"Manufacture_of_machinery_for_paper_and_paperboard_production",
		"28_96":"Manufacture_of_plastics_and_rubber_machinery",
		"28_99":"Manufacture_of_other_special_purpose_machinery_n_e_c",
		"29":"Manufacture_of_motor_vehicles_trailers_and_semi_trailers",
		"29_1":"Manufacture_of_motor_vehicles",
		"29_10":"Manufacture_of_motor_vehicles_x2",
		"29_2":"Manufacture_of_bodies_coachwork_for_motor_vehicles_manufacture_of_trailers_and_semi_trailers",
		"29_20":"Manufacture_of_bodies_coachwork_for_motor_vehicles_manufacture_of_trailers_and_semi_trailers_x2",
		"29_3":"Manufacture_of_parts_and_accessories_for_motor_vehicles",
		"29_31":"Manufacture_of_electrical_and_electronic_equipment_for_motor_vehicles",
		"29_32":"Manufacture_of_other_parts_and_accessories_for_motor_vehicles",
		"30":"Manufacture_of_other_transport_equipment",
		"30_1":"Building_of_ships_and_boats",
		"30_11":"Building_of_ships_and_floating_structures",
		"30_12":"Building_of_pleasure_and_sporting_boats",
		"30_2":"Manufacture_of_railway_locomotives_and_rolling_stock",
		"30_20":"Manufacture_of_railway_locomotives_and_rolling_stock_x2",
		"30_3":"Manufacture_of_air_and_spacecraft_and_related_machinery",
		"30_30":"Manufacture_of_air_and_spacecraft_and_related_machinery_x2",
		"30_4":"Manufacture_of_military_fighting_vehicles",
		"30_40":"Manufacture_of_military_fighting_vehicles_x2",
		"30_9":"Manufacture_of_transport_equipment_n_e_c",
		"30_91":"Manufacture_of_motorcycles",
		"30_92":"Manufacture_of_bicycles_and_invalid_carriages",
		"30_99":"Manufacture_of_other_transport_equipment_n_e_c",
		"31":"Manufacture_of_furniture",
		"31_0":"Manufacture_of_furniture_x2",
		"31_01":"Manufacture_of_office_and_shop_furniture",
		"31_02":"Manufacture_of_kitchen_furniture",
		"31_03":"Manufacture_of_mattresses",
		"31_09":"Manufacture_of_other_furniture",
		"32":"Other_manufacturing",
		"32_1":"Manufacture_of_jewellery_bijouterie_and_related_articles",
		"32_11":"Striking_of_coins",
		"32_12":"Manufacture_of_jewellery_and_related_articles",
		"32_13":"Manufacture_of_imitation_jewellery_and_related_articles",
		"32_2":"Manufacture_of_musical_instruments",
		"32_20":"Manufacture_of_musical_instruments_x2",
		"32_3":"Manufacture_of_sports_goods",
		"32_30":"Manufacture_of_sports_goods_x2",
		"32_4":"Manufacture_of_games_and_toys",
		"32_40":"Manufacture_of_games_and_toys_x2",
		"32_5":"Manufacture_of_medical_and_dental_instruments_and_supplies",
		"32_50":"Manufacture_of_medical_and_dental_instruments_and_supplies_x2",
		"32_9":"Manufacturing_n_e_c",
		"32_91":"Manufacture_of_brooms_and_brushes",
		"32_99":"Other_manufacturing_n_e_c",
		"33":"Repair_and_installation_of_machinery_and_equipment",
		"33_1":"Repair_of_fabricated_metal_products_machinery_and_equipment",
		"33_11":"Repair_of_fabricated_metal_products",
		"33_12":"Repair_of_machinery",
		"33_13":"Repair_of_electronic_and_optical_equipment",
		"33_14":"Repair_of_electrical_equipment",
		"33_15":"Repair_and_maintenance_of_ships_and_boats",
		"33_16":"Repair_and_maintenance_of_aircraft_and_spacecraft",
		"33_17":"Repair_and_maintenance_of_other_transport_equipment",
		"33_19":"Repair_of_other_equipment",
		"33_2":"Installation_of_industrial_machinery_and_equipment",
		"33_20":"Installation_of_industrial_machinery_and_equipment_x2",
		"35":"Electricity_gas_steam_and_air_conditioning_supply",
		"35_1":"Electric_power_generation_transmission_and_distribution",
		"35_11":"Production_of_electricity",
		"35_12":"Transmission_of_electricity",
		"35_13":"Distribution_of_electricity",
		"35_14":"Trade_of_electricity",
		"35_2":"Manufacture_of_gas_distribution_of_gaseous_fuels_through_mains",
		"35_21":"Manufacture_of_gas",
		"35_22":"Distribution_of_gaseous_fuels_through_mains",
		"35_23":"Trade_of_gas_through_mains",
		"35_3":"Steam_and_air_conditioning_supply",
		"35_30":"Steam_and_air_conditioning_supply_x2",
		"36":"Water_collection_treatment_and_supply",
		"36_0":"Water_collection_treatment_and_supply_x2",
		"36_00":"Water_collection_treatment_and_supply_x3",
		"37":"Sewerage",
		"37_0":"Sewerage_x2",
		"37_00":"Sewerage_x3",
		"38":"Waste_collection_treatment_and_disposal_activities_materials_recovery",
		"38_1":"Waste_collection",
		"38_11":"Collection_of_non_hazardous_waste",
		"38_12":"Collection_of_hazardous_waste",
		"38_2":"Waste_treatment_and_disposal",
		"38_21":"Treatment_and_disposal_of_non_hazardous_waste",
		"38_22":"Treatment_and_disposal_of_hazardous_waste",
		"38_3":"Materials_recovery",
		"38_31":"Dismantling_of_wrecks",
		"38_32":"Recovery_of_sorted_materials",
		"39":"Remediation_activities_and_other_waste_management_services",
		"39_0":"Remediation_activities_and_other_waste_management_services_x2",
		"39_00":"Remediation_activities_and_other_waste_management_services_x3",
		"41":"Construction_of_buildings",
		"41_1":"Development_of_building_projects",
		"41_10":"Development_of_building_projects_x2",
		"41_2":"Construction_of_residential_and_non_residential_buildings",
		"41_20":"Construction_of_residential_and_non_residential_buildings_x2",
		"42":"Civil_engineering",
		"42_1":"Construction_of_roads_and_railways",
		"42_11":"Construction_of_roads_and_motorways",
		"42_12":"Construction_of_railways_and_underground_railways",
		"42_13":"Construction_of_bridges_and_tunnels",
		"42_2":"Construction_of_utility_projects",
		"42_21":"Construction_of_utility_projects_for_fluids",
		"42_22":"Construction_of_utility_projects_for_electricity_and_telecommunications",
		"42_9":"Construction_of_other_civil_engineering_projects",
		"42_91":"Construction_of_water_projects",
		"42_99":"Construction_of_other_civil_engineering_projects_n_e_c",
		"43":"Specialised_construction_activities",
		"43_1":"Demolition_and_site_preparation",
		"43_11":"Demolition",
		"43_12":"Site_preparation",
		"43_13":"Test_drilling_and_boring",
		"43_2":"Electrical_plumbing_and_other_construction_installation_activities",
		"43_21":"Electrical_installation",
		"43_22":"Plumbing_heat_and_air_conditioning_installation",
		"43_29":"Other_construction_installation",
		"43_3":"Building_completion_and_finishing",
		"43_31":"Plastering",
		"43_32":"Joinery_installation",
		"43_33":"Floor_and_wall_covering",
		"43_34":"Painting_and_glazing",
		"43_39":"Other_building_completion_and_finishing",
		"43_9":"Other_specialised_construction_activities",
		"43_91":"Roofing_activities",
		"43_99":"Other_specialised_construction_activities_n_e_c",
		"45":"Wholesale_and_retail_trade_and_repair_of_motor_vehicles_and_motorcycles",
		"45_1":"Sale_of_motor_vehicles",
		"45_11":"Sale_of_cars_and_light_motor_vehicles",
		"45_19":"Sale_of_other_motor_vehicles",
		"45_2":"Maintenance_and_repair_of_motor_vehicles",
		"45_20":"Maintenance_and_repair_of_motor_vehicles_x2",
		"45_3":"Sale_of_motor_vehicle_parts_and_accessories",
		"45_31":"Wholesale_trade_of_motor_vehicle_parts_and_accessories",
		"45_32":"Retail_trade_of_motor_vehicle_parts_and_accessories",
		"45_4":"Sale_maintenance_and_repair_of_motorcycles_and_related_parts_and_accessories",
		"45_40":"Sale_maintenance_and_repair_of_motorcycles_and_related_parts_and_accessories_x2",
		"46":"Wholesale_trade_except_of_motor_vehicles_and_motorcycles",
		"46_1":"Wholesale_on_a_fee_or_contract_basis",
		"46_11":"Agents_involved_in_the_sale_of_agricultural_raw_materials_live_animals_textile_raw_materials_and_semi_finished_goods",
		"46_12":"Agents_involved_in_the_sale_of_fuels_ores_metals_and_industrial_chemicals",
		"46_13":"Agents_involved_in_the_sale_of_timber_and_building_materials",
		"46_14":"Agents_involved_in_the_sale_of_machinery_industrial_equipment_ships_and_aircraft",
		"46_15":"Agents_involved_in_the_sale_of_furniture_household_goods_hardware_and_ironmongery",
		"46_16":"Agents_involved_in_the_sale_of_textiles_clothing_fur_footwear_and_leather_goods",
		"46_17":"Agents_involved_in_the_sale_of_food_beverages_and_tobacco",
		"46_18":"Agents_specialised_in_the_sale_of_other_particular_products",
		"46_19":"Agents_involved_in_the_sale_of_a_variety_of_goods",
		"46_2":"Wholesale_of_agricultural_raw_materials_and_live_animals",
		"46_21":"Wholesale_of_grain_unmanufactured_tobacco_seeds_and_animal_feeds",
		"46_22":"Wholesale_of_flowers_and_plants",
		"46_23":"Wholesale_of_live_animals",
		"46_24":"Wholesale_of_hides_skins_and_leather",
		"46_3":"Wholesale_of_food_beverages_and_tobacco",
		"46_31":"Wholesale_of_fruit_and_vegetables",
		"46_32":"Wholesale_of_meat_and_meat_products",
		"46_33":"Wholesale_of_dairy_products_eggs_and_edible_oils_and_fats",
		"46_34":"Wholesale_of_beverages",
		"46_35":"Wholesale_of_tobacco_products",
		"46_36":"Wholesale_of_sugar_and_chocolate_and_sugar_confectionery",
		"46_37":"Wholesale_of_coffee_tea_cocoa_and_spices",
		"46_38":"Wholesale_of_other_food_including_fish_crustaceans_and_molluscs",
		"46_39":"Non_specialised_wholesale_of_food_beverages_and_tobacco",
		"46_4":"Wholesale_of_household_goods",
		"46_41":"Wholesale_of_textiles",
		"46_42":"Wholesale_of_clothing_and_footwear",
		"46_43":"Wholesale_of_electrical_household_appliances",
		"46_44":"Wholesale_of_china_and_glassware_and_cleaning_materials",
		"46_45":"Wholesale_of_perfume_and_cosmetics",
		"46_46":"Wholesale_of_pharmaceutical_goods",
		"46_47":"Wholesale_of_furniture_carpets_and_lighting_equipment",
		"46_48":"Wholesale_of_watches_and_jewellery",
		"46_49":"Wholesale_of_other_household_goods",
		"46_5":"Wholesale_of_information_and_communication_equipment",
		"46_51":"Wholesale_of_computers_computer_peripheral_equipment_and_software",
		"46_52":"Wholesale_of_electronic_and_telecommunications_equipment_and_parts",
		"46_6":"Wholesale_of_other_machinery_equipment_and_supplies",
		"46_61":"Wholesale_of_agricultural_machinery_equipment_and_supplies",
		"46_62":"Wholesale_of_machine_tools",
		"46_63":"Wholesale_of_mining_construction_and_civil_engineering_machinery",
		"46_64":"Wholesale_of_machinery_for_the_textile_industry_and_of_sewing_and_knitting_machines",
		"46_65":"Wholesale_of_office_furniture",
		"46_66":"Wholesale_of_other_office_machinery_and_equipment",
		"46_69":"Wholesale_of_other_machinery_and_equipment",
		"46_7":"Other_specialised_wholesale",
		"46_71":"Wholesale_of_solid_liquid_and_gaseous_fuels_and_related_products",
		"46_72":"Wholesale_of_metals_and_metal_ores",
		"46_73":"Wholesale_of_wood_construction_materials_and_sanitary_equipment",
		"46_74":"Wholesale_of_hardware_plumbing_and_heating_equipment_and_supplies",
		"46_75":"Wholesale_of_chemical_products",
		"46_76":"Wholesale_of_other_intermediate_products",
		"46_77":"Wholesale_of_waste_and_scrap",
		"46_9":"Non_specialised_wholesale_trade",
		"46_90":"Non_specialised_wholesale_trade_x2",
		"47":"Retail_trade_except_of_motor_vehicles_and_motorcycles",
		"47_1":"Retail_sale_in_non_specialised_stores",
		"47_11":"Retail_sale_in_non_specialised_stores_with_food_beverages_or_tobacco_predominating",
		"47_19":"Other_retail_sale_in_non_specialised_stores",
		"47_2":"Retail_sale_of_food_beverages_and_tobacco_in_specialised_stores",
		"47_21":"Retail_sale_of_fruit_and_vegetables_in_specialised_stores",
		"47_22":"Retail_sale_of_meat_and_meat_products_in_specialised_stores",
		"47_23":"Retail_sale_of_fish_crustaceans_and_molluscs_in_specialised_stores",
		"47_24":"Retail_sale_of_bread_cakes_flour_confectionery_and_sugar_confectionery_in_specialised_stores",
		"47_25":"Retail_sale_of_beverages_in_specialised_stores",
		"47_26":"Retail_sale_of_tobacco_products_in_specialised_stores",
		"47_29":"Other_retail_sale_of_food_in_specialised_stores",
		"47_3":"Retail_sale_of_automotive_fuel_in_specialised_stores",
		"47_30":"Retail_sale_of_automotive_fuel_in_specialised_stores_x2",
		"47_4":"Retail_sale_of_information_and_communication_equipment_in_specialised_stores",
		"47_41":"Retail_sale_of_computers_peripheral_units_and_software_in_specialised_stores",
		"47_42":"Retail_sale_of_telecommunications_equipment_in_specialised_stores",
		"47_43":"Retail_sale_of_audio_and_video_equipment_in_specialised_stores",
		"47_5":"Retail_sale_of_other_household_equipment_in_specialised_stores",
		"47_51":"Retail_sale_of_textiles_in_specialised_stores",
		"47_52":"Retail_sale_of_hardware_paints_and_glass_in_specialised_stores",
		"47_53":"Retail_sale_of_carpets_rugs_wall_and_floor_coverings_in_specialised_stores",
		"47_54":"Retail_sale_of_electrical_household_appliances_in_specialised_stores",
		"47_59":"Retail_sale_of_furniture_lighting_equipment_and_other_household_articles_in_specialised_stores",
		"47_6":"Retail_sale_of_cultural_and_recreation_goods_in_specialised_stores",
		"47_61":"Retail_sale_of_books_in_specialised_stores",
		"47_62":"Retail_sale_of_Newspapers_and_stationery_in_specialised_stores",
		"47_63":"Retail_sale_of_music_and_video_recordings_in_specialised_stores",
		"47_64":"Retail_sale_of_sporting_equipment_in_specialised_stores",
		"47_65":"Retail_sale_of_games_and_toys_in_specialised_stores",
		"47_7":"Retail_sale_of_other_goods_in_specialised_stores",
		"47_71":"Retail_sale_of_clothing_in_specialised_stores",
		"47_72":"Retail_sale_of_footwear_and_leather_goods_in_specialised_stores",
		"47_73":"Dispensing_chemist_in_specialised_stores",
		"47_74":"Retail_sale_of_medical_and_orthopaedic_goods_in_specialised_stores",
		"47_75":"Retail_sale_of_cosmetic_and_toilet_articles_in_specialised_stores",
		"47_76":"Retail_sale_of_flowers_plants_seeds_fertilisers_pet_animals_and_pet_food_in_specialised_stores",
		"47_77":"Retail_sale_of_watches_and_jewellery_in_specialised_stores",
		"47_78":"Other_retail_sale_of_New_goods_in_specialised_stores",
		"47_79":"Retail_sale_of_second_hand_goods_in_stores",
		"47_8":"Retail_sale_via_stalls_and_markets",
		"47_81":"Retail_sale_via_stalls_and_markets_of_food_beverages_and_tobacco_products",
		"47_82":"Retail_sale_via_stalls_and_markets_of_textiles_clothing_and_footwear",
		"47_89":"Retail_sale_via_stalls_and_markets_of_other_goods",
		"47_9":"Retail_trade_not_in_stores_stalls_or_markets",
		"47_91":"Retail_sale_via_mail_order_houses_or_via_Internet",
		"47_99":"Other_retail_sale_not_in_stores_stalls_or_markets",
		"49":"Land_transport_and_transport_via_pipelines",
		"49_1":"Passenger_rail_transport_interurban",
		"49_10":"Passenger_rail_transport_interurban_x2",
		"49_2":"Freight_rail_transport",
		"49_20":"Freight_rail_transport_x2",
		"49_3":"Other_passenger_land_transport",
		"49_31":"Urban_and_suburban_passenger_land_transport",
		"49_32":"Taxi_operation",
		"49_39":"Other_passenger_land_transport_n_e_c",
		"49_4":"Freight_transport_by_road_and_removal_services",
		"49_41":"Freight_transport_by_road",
		"49_42":"Removal_services",
		"49_5":"Transport_via_pipeline",
		"49_50":"Transport_via_pipeline_x2",
		"50":"Water_transport",
		"50_1":"Sea_and_coastal_passenger_water_transport",
		"50_10":"Sea_and_coastal_passenger_water_transport_x2",
		"50_2":"Sea_and_coastal_freight_water_transport",
		"50_20":"Sea_and_coastal_freight_water_transport_x2",
		"50_3":"Inland_passenger_water_transport",
		"50_30":"Inland_passenger_water_transport_x2",
		"50_4":"Inland_freight_water_transport",
		"50_40":"Inland_freight_water_transport_x2",
		"51":"Air_transport",
		"51_1":"Passenger_air_transport",
		"51_10":"Passenger_air_transport_x2",
		"51_2":"Freight_air_transport_and_space_transport",
		"51_21":"Freight_air_transport",
		"51_22":"Space_transport",
		"52":"Warehousing_and_support_activities_for_transportation",
		"52_1":"Warehousing_and_storage",
		"52_10":"Warehousing_and_storage_x2",
		"52_2":"Support_activities_for_transportation",
		"52_21":"Service_activities_incidental_to_land_transportation",
		"52_22":"Service_activities_incidental_to_water_transportation",
		"52_23":"Service_activities_incidental_to_air_transportation",
		"52_24":"Cargo_handling",
		"52_29":"Other_transportation_support_activities",
		"53":"Postal_and_courier_activities",
		"53_1":"Postal_activities_under_universal_service_obligation",
		"53_10":"Postal_activities_under_universal_service_obligation_x2",
		"53_2":"Other_postal_and_courier_activities",
		"53_20":"Other_postal_and_courier_activities_x2",
		"55":"Accommodation",
		"55_1":"Hotels_and_similar_accommodation",
		"55_10":"Hotels_and_similar_accommodation_x2",
		"55_2":"Holiday_and_other_short_stay_accommodation",
		"55_20":"Holiday_and_other_short_stay_accommodation_x2",
		"55_3":"Camping_grounds_recreational_vehicle_parks_and_trailer_parks",
		"55_30":"Camping_grounds_recreational_vehicle_parks_and_trailer_parks_x2",
		"55_9":"Other_accommodation",
		"55_90":"Other_accommodation_x2",
		"56":"Food_and_beverage_service_activities",
		"56_1":"Restaurants_and_mobile_food_service_activities",
		"56_10":"Restaurants_and_mobile_food_service_activities_x2",
		"56_2":"Event_catering_and_other_food_service_activities",
		"56_21":"Event_catering_activities",
		"56_29":"Other_food_service_activities",
		"56_3":"Beverage_serving_activities",
		"56_30":"Beverage_serving_activities_x2",
		"58":"Publishing_activities",
		"58_1":"Publishing_of_books_periodicals_and_other_publishing_activities",
		"58_11":"Book_publishing",
		"58_12":"Publishing_of_directories_and_mailing_lists",
		"58_13":"Publishing_of_Newspapers",
		"58_14":"Publishing_of_journals_and_periodicals",
		"58_19":"Other_publishing_activities",
		"58_2":"Software_publishing",
		"58_21":"Publishing_of_computer_games",
		"58_29":"Other_software_publishing",
		"59":"Motion_picture_video_and_television_programme_production_sound_recording_and_music_publishing_activities",
		"59_1":"Motion_picture_video_and_television_programme_activities",
		"59_11":"Motion_picture_video_and_television_programme_production_activities",
		"59_12":"Motion_picture_video_and_television_programme_post_production_activities",
		"59_13":"Motion_picture_video_and_television_programme_distribution_activities",
		"59_14":"Motion_picture_projection_activities",
		"59_2":"Sound_recording_and_music_publishing_activities",
		"59_20":"Sound_recording_and_music_publishing_activities_x2",
		"60":"Programming_and_broadcasting_activities",
		"60_1":"Radio_broadcasting",
		"60_10":"Radio_broadcasting_x2",
		"60_2":"Television_programming_and_broadcasting_activities",
		"60_20":"Television_programming_and_broadcasting_activities_x2",
		"61":"Telecommunications",
		"61_1":"Wired_telecommunications_activities",
		"61_10":"Wired_telecommunications_activities_x2",
		"61_2":"Wireless_telecommunications_activities",
		"61_20":"Wireless_telecommunications_activities_x2",
		"61_3":"Satellite_telecommunications_activities",
		"61_30":"Satellite_telecommunications_activities_x2",
		"61_9":"Other_telecommunications_activities",
		"61_90":"Other_telecommunications_activities_x2",
		"62":"Computer_programming_consultancy_and_related_activities",
		"62_0":"Computer_programming_consultancy_and_related_activities_x2",
		"62_01":"Computer_programming_activities",
		"62_02":"Computer_consultancy_activities",
		"62_03":"Computer_facilities_management_activities",
		"62_09":"Other_information_technology_and_computer_service_activities",
		"63":"Information_service_activities",
		"63_1":"Data_processing_hosting_and_related_activities_web_portals",
		"63_11":"Data_processing_hosting_and_related_activities",
		"63_12":"Web_portals",
		"63_9":"Other_information_service_activities",
		"63_91":"News_agency_activities",
		"63_99":"Other_information_service_activities_n_e_c",
		"64":"Financial_service_activities_except_insurance_and_pension_funding",
		"64_1":"Monetary_intermediation",
		"64_11":"Central_banking",
		"64_19":"Other_monetary_intermediation",
		"64_2":"Activities_of_holding_companies",
		"64_20":"Activities_of_holding_companies_x2",
		"64_3":"Trusts_funds_and_similar_financial_entities",
		"64_30":"Trusts_funds_and_similar_financial_entities_x2",
		"64_9":"Other_financial_service_activities_except_insurance_and_pension_funding",
		"64_91":"Financial_leasing",
		"64_92":"Other_credit_granting",
		"64_99":"Other_financial_service_activities_except_insurance_and_pension_funding_n_e_c",
		"65":"Insurance_reinsurance_and_pension_funding_except_compulsory_social_security",
		"65_1":"Insurance",
		"65_11":"Life_insurance",
		"65_12":"Non_life_insurance",
		"65_2":"Reinsurance",
		"65_20":"Reinsurance_x2",
		"65_3":"Pension_funding",
		"65_30":"Pension_funding_x2",
		"66":"Activities_auxiliary_to_financial_services_and_insurance_activities",
		"66_1":"Activities_auxiliary_to_financial_services_except_insurance_and_pension_funding",
		"66_11":"Administration_of_financial_markets",
		"66_12":"Security_and_commodity_contracts_brokerage",
		"66_19":"Other_activities_auxiliary_to_financial_services_except_insurance_and_pension_funding",
		"66_2":"Activities_auxiliary_to_insurance_and_pension_funding",
		"66_21":"Risk_and_damage_evaluation",
		"66_22":"Activities_of_insurance_agents_and_brokers",
		"66_29":"Other_activities_auxiliary_to_insurance_and_pension_funding",
		"66_3":"Fund_management_activities",
		"66_30":"Fund_management_activities_x2",
		"68":"Real_estate_activities",
		"68_1":"Buying_and_selling_of_own_real_estate",
		"68_10":"Buying_and_selling_of_own_real_estate_x2",
		"68_2":"Renting_and_operating_of_own_or_leased_real_estate",
		"68_20":"Renting_and_operating_of_own_or_leased_real_estate_x2",
		"68_3":"Real_estate_activities_on_a_fee_or_contract_basis",
		"68_31":"Real_estate_agencies",
		"68_32":"Management_of_real_estate_on_a_fee_or_contract_basis",
		"69":"Legal_and_accounting_activities",
		"69_1":"Legal_activities",
		"69_10":"Legal_activities_x2",
		"69_2":"Accounting_bookkeeping_and_auditing_activities_tax_consultancy",
		"69_20":"Accounting_bookkeeping_and_auditing_activities_tax_consultancy_x2",
		"70":"Activities_of_head_offices_management_consultancy_activities",
		"70_1":"Activities_of_head_offices",
		"70_10":"Activities_of_head_offices_x2",
		"70_2":"Management_consultancy_activities",
		"70_21":"Public_relations_and_communication_activities",
		"70_22":"Business_and_other_management_consultancy_activities",
		"71":"Architectural_and_engineering_activities_technical_testing_and_analysis",
		"71_1":"Architectural_and_engineering_activities_and_related_technical_consultancy",
		"71_11":"Architectural_activities",
		"71_12":"Engineering_activities_and_related_technical_consultancy",
		"71_2":"Technical_testing_and_analysis",
		"71_20":"Technical_testing_and_analysis_x2",
		"72":"Scientific_research_and_development",
		"72_1":"Research_and_experimental_development_on_natural_sciences_and_engineering",
		"72_11":"Research_and_experimental_development_on_biotechnology",
		"72_19":"Other_research_and_experimental_development_on_natural_sciences_and_engineering",
		"72_2":"Research_and_experimental_development_on_social_sciences_and_humanities",
		"72_20":"Research_and_experimental_development_on_social_sciences_and_humanities_x2",
		"73":"Advertising_and_market_research",
		"73_1":"Advertising",
		"73_11":"Advertising_agencies",
		"73_12":"Media_representation",
		"73_2":"Market_research_and_public_opinion_polling",
		"73_20":"Market_research_and_public_opinion_polling_x2",
		"74":"Other_professional_scientific_and_technical_activities",
		"74_1":"Specialised_design_activities",
		"74_10":"Specialised_design_activities_x2",
		"74_2":"Photographic_activities",
		"74_20":"Photographic_activities_x2",
		"74_3":"Translation_and_interpretation_activities",
		"74_30":"Translation_and_interpretation_activities_x2",
		"74_9":"Other_professional_scientific_and_technical_activities_n_e_c",
		"74_90":"Other_professional_scientific_and_technical_activities_n_e_c_x2",
		"75":"Veterinary_activities",
		"75_0":"Veterinary_activities_x2",
		"75_00":"Veterinary_activities_x3",
		"77":"Rental_and_leasing_activities",
		"77_1":"Renting_and_leasing_of_motor_vehicles",
		"77_11":"Renting_and_leasing_of_cars_and_light_motor_vehicles",
		"77_12":"Renting_and_leasing_of_trucks",
		"77_2":"Renting_and_leasing_of_personal_and_household_goods",
		"77_21":"Renting_and_leasing_of_recreational_and_sports_goods",
		"77_22":"Renting_of_video_tapes_and_disks",
		"77_29":"Renting_and_leasing_of_other_personal_and_household_goods",
		"77_3":"Renting_and_leasing_of_other_machinery_equipment_and_tangible_goods",
		"77_31":"Renting_and_leasing_of_agricultural_machinery_and_equipment",
		"77_32":"Renting_and_leasing_of_construction_and_civil_engineering_machinery_and_equipment",
		"77_33":"Renting_and_leasing_of_office_machinery_and_equipment_including_computers",
		"77_34":"Renting_and_leasing_of_water_transport_equipment",
		"77_35":"Renting_and_leasing_of_air_transport_equipment",
		"77_39":"Renting_and_leasing_of_other_machinery_equipment_and_tangible_goods_n_e_c",
		"77_4":"Leasing_of_intellectual_property_and_similar_products_except_copyrighted_works",
		"77_40":"Leasing_of_intellectual_property_and_similar_products_except_copyrighted_works_x2",
		"78":"Employment_activities",
		"78_1":"Activities_of_employment_placement_agencies",
		"78_10":"Activities_of_employment_placement_agencies_x2",
		"78_2":"Temporary_employment_agency_activities",
		"78_20":"Temporary_employment_agency_activities_x2",
		"78_3":"Other_human_resources_provision",
		"78_30":"Other_human_resources_provision_x2",
		"79":"Travel_agency_tour_operator_and_other_reservation_service_and_related_activities",
		"79_1":"Travel_agency_and_tour_operator_activities",
		"79_11":"Travel_agency_activities",
		"79_12":"Tour_operator_activities",
		"79_9":"Other_reservation_service_and_related_activities",
		"79_90":"Other_reservation_service_and_related_activities_x2",
		"80":"Security_and_investigation_activities",
		"80_1":"Private_security_activities",
		"80_10":"Private_security_activities_x2",
		"80_2":"Security_systems_service_activities",
		"80_20":"Security_systems_service_activities_x2",
		"80_3":"Investigation_activities",
		"80_30":"Investigation_activities_x2",
		"81":"Services_to_buildings_and_landscape_activities",
		"81_1":"Combined_facilities_support_activities",
		"81_10":"Combined_facilities_support_activities_x2",
		"81_2":"Cleaning_activities",
		"81_21":"General_cleaning_of_buildings",
		"81_22":"Other_building_and_industrial_cleaning_activities",
		"81_29":"Other_cleaning_activities",
		"81_3":"Landscape_service_activities",
		"81_30":"Landscape_service_activities_x2",
		"82":"Office_administrative_office_support_and_other_business_support_activities",
		"82_1":"Office_administrative_and_support_activities",
		"82_11":"Combined_office_administrative_service_activities",
		"82_19":"Photocopying_document_preparation_and_other_specialised_office_support_activities",
		"82_2":"Activities_of_call_centres",
		"82_20":"Activities_of_call_centres_x2",
		"82_3":"Organisation_of_conventions_and_trade_shows",
		"82_30":"Organisation_of_conventions_and_trade_shows_x2",
		"82_9":"Business_support_service_activities_n_e_c",
		"82_91":"Activities_of_collection_agencies_and_credit_bureaus",
		"82_92":"Packaging_activities",
		"82_99":"Other_business_support_service_activities_n_e_c",
		"84":"Public_administration_and_defence_compulsory_social_security",
		"84_1":"Administration_of_the_State_and_the_economic_and_social_policy_of_the_community",
		"84_11":"General_public_administration_activities",
		"84_12":"Regulation_of_the_activities_of_providing_health_care_education_cultural_services_and_other_social_services_excluding_social_security",
		"84_13":"Regulation_of_and_contribution_to_more_efficient_operation_of_businesses",
		"84_2":"Provision_of_services_to_the_community_as_a_whole",
		"84_21":"Foreign_affairs",
		"84_22":"Defence_activities",
		"84_23":"Justice_and_judicial_activities",
		"84_24":"Public_order_and_safety_activities",
		"84_25":"Fire_service_activities",
		"84_3":"Compulsory_social_security_activities",
		"84_30":"Compulsory_social_security_activities_x2",
		"85":"Education",
		"85_1":"Pre_primary_education",
		"85_10":"Pre_primary_education_x2",
		"85_2":"Primary_education",
		"85_20":"Primary_education_x2",
		"85_3":"Secondary_education",
		"85_31":"General_secondary_education",
		"85_32":"Technical_and_vocational_secondary_education",
		"85_4":"Higher_education",
		"85_41":"Post_secondary_non_tertiary_education",
		"85_42":"Tertiary_education",
		"85_5":"Other_education",
		"85_51":"Sports_and_recreation_education",
		"85_52":"Cultural_education",
		"85_53":"Driving_school_activities",
		"85_59":"Other_education_n_e_c",
		"85_6":"Educational_support_activities",
		"85_60":"Educational_support_activities_x2",
		"86":"Human_health_activities",
		"86_1":"Hospital_activities",
		"86_10":"Hospital_activities_x2",
		"86_2":"Medical_and_dental_practice_activities",
		"86_21":"General_medical_practice_activities",
		"86_22":"Specialist_medical_practice_activities",
		"86_23":"Dental_practice_activities",
		"86_9":"Other_human_health_activities",
		"86_90":"Other_human_health_activities_x2",
		"87":"Residential_care_activities",
		"87_1":"Residential_nursing_care_activities",
		"87_10":"Residential_nursing_care_activities_x2",
		"87_2":"Residential_care_activities_for_mental_retardation_mental_health_and_substance_abuse",
		"87_20":"Residential_care_activities_for_mental_retardation_mental_health_and_substance_abuse_x2",
		"87_3":"Residential_care_activities_for_the_elderly_and_disabled",
		"87_30":"Residential_care_activities_for_the_elderly_and_disabled_x2",
		"87_9":"Other_residential_care_activities",
		"87_90":"Other_residential_care_activities_x2",
		"88":"Social_work_activities_without_accommodation",
		"88_1":"Social_work_activities_without_accommodation_for_the_elderly_and_disabled",
		"88_10":"Social_work_activities_without_accommodation_for_the_elderly_and_disabled_x2",
		"88_9":"Other_social_work_activities_without_accommodation",
		"88_91":"Child_day_care_activities",
		"88_99":"Other_social_work_activities_without_accommodation_n_e_c",
		"90":"Creative_arts_and_entertainment_activities",
		"90_0":"Creative_arts_and_entertainment_activities_x2",
		"90_01":"Performing_arts",
		"90_02":"Support_activities_to_performing_arts",
		"90_03":"Artistic_creation",
		"90_04":"Operation_of_arts_facilities",
		"91":"Libraries_archives_museums_and_other_cultural_activities",
		"91_0":"Libraries_archives_museums_and_other_cultural_activities_x2",
		"91_01":"Library_and_archives_activities",
		"91_02":"Museums_activities",
		"91_03":"Operation_of_historical_sites_and_buildings_and_similar_visitor_attractions",
		"91_04":"Botanical_and_zoological_gardens_and_nature_reserves_activities",
		"92":"Gambling_and_betting_activities",
		"92_0":"Gambling_and_betting_activities_x2",
		"92_00":"Gambling_and_betting_activities_x3",
		"93":"Sports_activities_and_amusement_and_recreation_activities",
		"93_1":"Sports_activities",
		"93_11":"Operation_of_sports_facilities",
		"93_12":"Activities_of_sport_clubs",
		"93_13":"Fitness_facilities",
		"93_19":"Other_sports_activities",
		"93_2":"Amusement_and_recreation_activities",
		"93_21":"Activities_of_amusement_parks_and_theme_parks",
		"93_29":"Other_amusement_and_recreation_activities",
		"94":"Activities_of_membership_organisations",
		"94_1":"Activities_of_business_employers_and_professional_membership_organisations",
		"94_11":"Activities_of_business_and_employers_membership_organisations",
		"94_12":"Activities_of_professional_membership_organisations",
		"94_2":"Activities_of_trade_unions",
		"94_20":"Activities_of_trade_unions_x2",
		"94_9":"Activities_of_other_membership_organisations",
		"94_91":"Activities_of_religious_organisations",
		"94_92":"Activities_of_political_organisations",
		"94_99":"Activities_of_other_membership_organisations_n_e_c",
		"95":"Repair_of_computers_and_personal_and_household_goods",
		"95_1":"Repair_of_computers_and_communication_equipment",
		"95_11":"Repair_of_computers_and_peripheral_equipment",
		"95_12":"Repair_of_communication_equipment",
		"95_2":"Repair_of_personal_and_household_goods",
		"95_21":"Repair_of_consumer_electronics",
		"95_22":"Repair_of_household_appliances_and_home_and_garden_equipment",
		"95_23":"Repair_of_footwear_and_leather_goods",
		"95_24":"Repair_of_furniture_and_home_furnishings",
		"95_25":"Repair_of_watches_clocks_and_jewellery",
		"95_29":"Repair_of_other_personal_and_household_goods",
		"96":"Other_personal_service_activities",
		"96_0":"Other_personal_service_activities_x2",
		"96_01":"Washing_and_dry_cleaning_of_textile_and_fur_products",
		"96_02":"Hairdressing_and_other_beauty_treatment",
		"96_03":"Funeral_and_related_activities",
		"96_04":"Physical_well_being_activities",
		"96_09":"Other_personal_service_activities_n_e_c",
		"97":"Activities_of_households_as_employers_of_domestic_personnel",
		"97_0":"Activities_of_households_as_employers_of_domestic_personnel_x2",
		"97_00":"Activities_of_households_as_employers_of_domestic_personnel_x3",
		"98":"Undifferentiated_goods_and_services_producing_activities_of_private_households_for_own_use",
		"98_1":"Undifferentiated_goods_producing_activities_of_private_households_for_own_use",
		"98_10":"Undifferentiated_goods_producing_activities_of_private_households_for_own_use_x2",
		"98_2":"Undifferentiated_service_producing_activities_of_private_households_for_own_use",
		"98_20":"Undifferentiated_service_producing_activities_of_private_households_for_own_use_x2",
		"99":"Activities_of_extraterritorial_organisations_and_bodies",
		"99_0":"Activities_of_extraterritorial_organisations_and_bodies_x2",
		"99_00":"Activities_of_extraterritorial_organisations_and_bodies_x3",
}

	ECNMC_ACTVTY = models.CharField("ECNMC_ACTVTY",max_length=255, choices=NACE_LVLS2TO4_STGNG_domain,default=None, blank=True, null=True, db_comment="NACE_LVLS2TO4_STGNG_domain")

	ENTRPRS_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Enterprise",
		"2":"Not_enterprise",
}

	ENTRPRS_INDCTR = models.CharField("ENTRPRS_INDCTR",max_length=255, choices=ENTRPRS_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="ENTRPRS_INDCTR_INPT_domain")

	SZ_RIAD_CLLCTN_domain = {		"1":"Large_enterprise_Enterprise_not_qualifying_as_a_micro_small_or_medium_sized_enterprise_SME_in_accordance_with_the_Annex_to_Recommendation_2003_361_EC",
		"2":"Medium_enterprise_Enterprise_qualifying_as_an_SME_but_not_as_a_small_or_micro_enterprise_in_accordance_with_the_Annex_to_Recommendation_2003_361_EC",
		"3":"Small_enterprise_Enterprise_qualifying_as_a_small_enterprise_in_accordance_with_the_Annex_to_Recommendation_2003_361_EC",
		"4":"Micro_enterprise_Enterprise_qualifying_as_a_micro_enterprise_in_accordance_with_the_Annex_to_Recommendation_2003_361_EC",
}

	ENTRPRS_SZ = models.CharField("ENTRPRS_SZ",max_length=255, choices=SZ_RIAD_CLLCTN_domain,default=None, blank=True, null=True, db_comment="SZ_RIAD_CLLCTN_domain")

	FRST_NM = models.CharField("FRST_NM",max_length=255,default=None, blank=True, null=True)

	ISO3166_domain = {		"AD":"Andorra",
		"AE":"United_Arab_Emirates_the",
		"AF":"Afghanistan",
		"AG":"Antigua_and_Barbuda",
		"AI":"Anguilla",
		"AL":"Albania",
		"AM":"Armenia",
		"AO":"Angola",
		"AQ":"Antarctica",
		"AR":"Argentina",
		"AS":"American_Samoa",
		"AT":"Austria",
		"AU":"Australia",
		"AW":"Aruba",
		"AX":"Aland_Islands",
		"AZ":"Azerbaijan",
		"BA":"Bosnia_and_Herzegovina",
		"BB":"Barbados",
		"BD":"Bangladesh",
		"BE":"Belgium",
		"BF":"Burkina_Faso",
		"BG":"Bulgaria",
		"BH":"Bahrain",
		"BI":"Burundi",
		"BJ":"Benin",
		"BL":"Saint_Barthelemy",
		"BM":"Bermuda",
		"BN":"Brunei_Darussalam",
		"BO":"Bolivia_Plurinational_State_of",
		"BQ":"Bonaire_Saint_Eustatius_and_Saba",
		"BR":"Brazil",
		"BS":"Bahamas_the",
		"BT":"Bhutan",
		"BV":"Bouvet_Island",
		"BW":"Botswana",
		"BY":"Belarus",
		"BZ":"Belize",
		"CA":"Canada",
		"CC":"Cocos_Keeling_Islands_the",
		"CD":"Congo_the_Democratic_Republic_of_the",
		"CF":"Central_African_Republic_the",
		"CG":"Congo_the",
		"CH":"Switzerland",
		"CI":"Cote_d_Ivoire",
		"CK":"Cook_Islands_the",
		"CL":"Chile",
		"CM":"Cameroon",
		"CN":"China_China_excluding_Taiwan_TW_Hong_Kong_HK_Macao_MO",
		"CO":"Colombia",
		"CR":"Costa_Rica",
		"CU":"Cuba",
		"CV":"Cabo_Verde",
		"CW":"Curacao",
		"CX":"Christmas_Island",
		"CY":"Cyprus",
		"CZ":"Czechia",
		"DE":"Germany",
		"DJ":"Djibouti",
		"DK":"Denmark",
		"DM":"Dominica",
		"DO":"Dominican_Republic_the",
		"DZ":"Algeria",
		"EC":"Ecuador",
		"EE":"Estonia",
		"EG":"Egypt",
		"EH":"Western_Sahara",
		"ER":"Eritrea",
		"ES":"Spain",
		"ET":"Ethiopia",
		"FI":"Finland_Finland_excluding_Aland_AX",
		"FJ":"Fiji",
		"FK":"Falkland_Islands_the_Malvinas",
		"FM":"Micronesia_Federated_States_of",
		"FO":"Faroe_Islands_the",
		"FR":"France_France_excluding_Guadeloupe_GP_Guyane_GF_La_Reunion_RE_Martinique_MQ_Mayotte_YT_Nouvelle_Caledonie_NC_Polynesie_francaise_PF_Saint_Barthelemy_BL_Saint_Martin_MF_Saint_Pierre_et_Miquelon_PM_Terres_australes_francaises_TF_Wallis_et_Futuna_WF",
		"GA":"Gabon",
		"GB":"United_Kingdom_of_Great_Britain_and_Northern_Ireland_the",
		"GD":"Grenada",
		"GE":"Georgia",
		"GF":"French_Guiana",
		"GG":"Guernsey",
		"GH":"Ghana",
		"GI":"Gibraltar",
		"GL":"Greenland",
		"GM":"Gambia_the",
		"GN":"Guinea",
		"GP":"Guadeloupe",
		"GQ":"Equatorial_Guinea",
		"GR":"Greece",
		"GS":"South_Georgia_and_the_South_Sandwich_Islands",
		"GT":"Guatemala",
		"GU":"Guam",
		"GW":"Guinea_Bissau",
		"GY":"Guyana",
		"HK":"Hong_Kong",
		"HM":"Heard_Island_and_McDonald_Islands",
		"HN":"Honduras",
		"HR":"Croatia",
		"HT":"Haiti",
		"HU":"Hungary",
		"ID":"Indonesia",
		"IE":"Ireland",
		"IL":"Israel",
		"IM":"Isle_of_Man",
		"IN":"India",
		"IO":"British_Indian_Ocean_Territory_the",
		"IQ":"Iraq",
		"IR":"Iran_Islamic_Republic_of",
		"IS":"Iceland",
		"IT":"Italy",
		"JE":"Jersey",
		"JM":"Jamaica",
		"JO":"Jordan",
		"JP":"Japan",
		"KE":"Kenya",
		"KG":"Kyrgyzstan",
		"KH":"Cambodia",
		"KI":"Kiribati",
		"KM":"Comoros_the",
		"KN":"Saint_Kitts_and_Nevis",
		"KP":"Korea_the_Democratic_People_s_Republic_of",
		"KR":"Korea_the_Republic_of",
		"KW":"Kuwait",
		"KY":"Cayman_Islands_the",
		"KZ":"Kazakhstan",
		"LA":"Lao_People_s_Democratic_Republic_the",
		"LB":"Lebanon",
		"LC":"Saint_Lucia",
		"LI":"Liechtenstein",
		"LK":"Sri_Lanka",
		"LR":"Liberia",
		"LS":"Lesotho",
		"LT":"Lithuania",
		"LU":"Luxembourg",
		"LV":"Latvia",
		"LY":"Libya",
		"MA":"Morocco",
		"MC":"Monaco",
		"MD":"Moldova_the_Republic_of",
		"ME":"Montenegro",
		"MF":"Saint_Martin_French_part",
		"MG":"Madagascar",
		"MH":"Marshall_Islands_the",
		"MK":"Macedonia_the_former_Yugoslav_Republic_of",
		"ML":"Mali",
		"MM":"Myanmar",
		"MN":"Mongolia",
		"MO":"Macao",
		"MP":"Northern_Mariana_Islands_the",
		"MQ":"Martinique",
		"MR":"Mauritania",
		"MS":"Montserrat",
		"MT":"Malta",
		"MU":"Mauritius",
		"MV":"Maldives",
		"MW":"Malawi",
		"MX":"Mexico",
		"MY":"Malaysia",
		"MZ":"Mozambique",
		"NA":"Namibia",
		"NC":"New_Caledonia",
		"NE":"Niger_the",
		"NF":"Norfolk_Island",
		"NG":"Nigeria",
		"NI":"Nicaragua",
		"NL":"Netherlands_the_Netherlands_excluding_Aruba_AW_Bonaire_Saint_Eustatius_and_Saba_BQ_Curacao_CW_Sint_Maarten_SX",
		"NO":"Norway_Norway_excluding_Svalbard_and_Jan_Mayen_SJ",
		"NP":"Nepal",
		"NR":"Nauru",
		"NU":"Niue",
		"NZ":"New_Zealand",
		"OM":"Oman",
		"PA":"Panama",
		"PE":"Peru",
		"PF":"French_Polynesia",
		"PG":"Papua_New_Guinea",
		"PH":"Philippines_the",
		"PK":"Pakistan",
		"PL":"Poland",
		"PM":"Saint_Pierre_and_Miquelon",
		"PN":"Pitcairn",
		"PR":"Puerto_Rico",
		"PS":"Palestine_State_of",
		"PT":"Portugal",
		"PW":"Palau",
		"PY":"Paraguay",
		"QA":"Qatar",
		"RE":"Reunion",
		"RO":"Romania",
		"RS":"Serbia",
		"RU":"Russian_Federation_the",
		"RW":"Rwanda",
		"SA":"Saudi_Arabia",
		"SB":"Solomon_Islands",
		"SC":"Seychelles",
		"SD":"Sudan_the",
		"SE":"Sweden",
		"SG":"Singapore",
		"SH":"Saint_Helena_Ascension_and_Tristan_da_Cunha",
		"SI":"Slovenia",
		"SJ":"Svalbard_and_Jan_Mayen",
		"SK":"Slovakia",
		"SL":"Sierra_Leone",
		"SM":"San_Marino",
		"SN":"Senegal",
		"SO":"Somalia",
		"SR":"Suriname",
		"SS":"South_Sudan",
		"ST":"Sao_Tome_and_Principe",
		"SV":"El_Salvador",
		"SX":"Sint_Maarten_Dutch_part",
		"SY":"Syrian_Arab_Republic",
		"SZ":"Swaziland",
		"TC":"Turks_and_Caicos_Islands_the",
		"TD":"Chad",
		"TF":"French_Southern_Territories_the",
		"TG":"Togo",
		"TH":"Thailand",
		"TJ":"Tajikistan",
		"TK":"Tokelau",
		"TL":"Timor_Leste",
		"TM":"Turkmenistan",
		"TN":"Tunisia",
		"TO":"Tonga",
		"TR":"Turkey",
		"TT":"Trinidad_and_Tobago",
		"TV":"Tuvalu",
		"TW":"Taiwan_Province_of_China",
		"TZ":"Tanzania_United_Republic_of",
		"UA":"Ukraine",
		"UG":"Uganda",
		"UM":"United_States_Minor_Outlying_Islands_the",
		"US":"United_States_of_America_the_United_States_excluding_American_Samoa_AS_Guam_GU_Northern_Mariana_Islands_MP_Puerto_Rico_PR_United_States_Minor_Outlying_Islands_UM_Virgin_Islands_U_S_VI",
		"UY":"Uruguay",
		"UZ":"Uzbekistan",
		"VA":"Holy_See_the",
		"VC":"Saint_Vincent_and_the_Grenadines",
		"VE":"Venezuela_Bolivarian_Republic_of",
		"VG":"Virgin_Islands_British",
		"VI":"Virgin_Islands_U_S",
		"VN":"Viet_Nam",
		"VU":"Vanuatu",
		"WF":"Wallis_and_Futuna",
		"WS":"Samoa",
		"YE":"Yemen",
		"YT":"Mayotte",
		"ZA":"South_Africa",
		"ZM":"Zambia",
		"ZW":"Zimbabwe",
}

	GVRND_CNTRY_CD = models.CharField("GVRND_CNTRY_CD",max_length=255, choices=ISO3166_domain,default=None, blank=True, null=True, db_comment="ISO3166_domain")

	INSTTTNL_SCTR_domain = {		"S11":"Non_financial_corporations_It_corresponds_to_sector_S_11_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_45_to_2_50_of_Annex_A_extended_to_the_rest_of_the_world",
		"S121":"Central_banks_It_corresponds_to_subsector_S_121_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_72_to_2_74_of_Annex_A_extended_to_the_rest_of_the_world",
		"S122_A":"Credit_institutions_Credit_institutions_as_defined_in_Article_4_1_1_of_Regulation_EU_No_575_2013",
		"S122_A_1":"Credit_institutions_not_including_entities_according_to_the_article_2_5_Directive_2013_36_EU",
		"S122_A_2":"Credit_institutions_according_to_the_article_2_5_Directive_2013_36_EU",
		"S122_B1":"Electronic_money_institutions_principally_engaged_in_financial_intermediation_Electronic_money_institutions_as_defined_in_Directive_2009_110_EC_article_2_1_that_are_principally_engaged_in_financial_intermediation_as_defined_in_Regulation_EU_no_549_2013_paragraph_2_56_of_Annex_A",
		"S122_B2":"Deposit_taking_corporations_except_the_central_bank_other_than_credit_institutions_and_electronic_money_institutions_It_corresponds_to_subsector_S_122_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_75_to_2_78_of_Annex_A_extended_to_the_rest_of_the_world_other_than_credit_institutions_as_defined_in_Article_4_1_1_of_Regulation_EU_No_575_2013_and_electronic_money_institutions_as_defined_in_Directive_2009_110_EC_article_2_1",
		"S123":"Money_Market_Funds_MMFs_It_corresponds_to_subsector_S_123_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_79_to_2_81_of_Annex_A_extended_to_the_rest_of_the_world",
		"S124":"Non_MMF_investment_funds_It_corresponds_to_subsector_S_124_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_82_to_2_85_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_A":"Financial_Vehicle_Corporations_FVCs_FVCs_as_defined_in_Article_1_of_Regulation_EU_No_1075_2013",
		"S125_B":"Security_and_derivative_dealers_Security_and_derivative_dealers_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_91_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_C":"Financial_corporations_engaged_in_lending_Financial_corporations_engaged_in_lending_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_92_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_D":"Specialised_financial_corporations_other_than_CCPs_Specialised_financial_corporations_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_93_of_Annex_A_extended_to_the_rest_of_the_world_other_than_CCPs_as_defined_in_point_1_of_Article_2_of_Regulation_EU_No_648_2012",
		"S125_E":"Central_Counterparties_CCPs_CCPs_as_defined_in_point_1_of_Article_2_of_Regulation_EU_No_648_2012",
		"S125_I":"Other_financial_intermediaries_except_insurance_corporations_and_pension_funds_other_than_CCPs_FVCs_security_and_derivative_dealers_financial_corporations_engaged_in_lending_and_specialised_financial_corporations_It_corresponds_to_subsector_S_125_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_86_to_2_94_of_Annex_A_extended_to_the_rest_of_the_world_other_than_CCPs_as_defined_in_point_1_of_Article_2_of_Regulation_EU_No_648_2012_FVCs_as_defined_in_Article_1_of_Regulation_EU_No_1075_2013_and_security_and_derivative_dealers_financial_corporations_engaged_in_lending_and_specialised_financial_corporations_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_91_2_92_and_2_93_respectively_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_W":"Other_financial_corporations_excluding_financial_vehicle_corporations",
		"S126":"Financial_auxiliaries_It_corresponds_to_subsector_S_126_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_63_and_2_95_to_2_97_of_Annex_A_extended_to_the_rest_of_the_world",
		"S127":"Captive_financial_institutions_and_money_lenders_It_corresponds_to_subsector_S_127_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_98_to_2_99_of_Annex_A_extended_to_the_rest_of_the_world",
		"S128":"Insurance_corporations_It_corresponds_to_subsector_S_128_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_100_to_2_104_of_Annex_A_extended_to_the_rest_of_the_world",
		"S129":"Pension_funds_It_corresponds_to_subsector_S_129_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_105_to_2_110_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1311":"Central_government_excluding_social_security_funds_It_corresponds_to_subsector_S_1311_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_114_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1312":"State_government_excluding_social_security_funds_It_corresponds_to_subsector_S_1312_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_115_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1313":"Local_government_excluding_social_security_funds_It_corresponds_to_subsector_S_1313_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_116_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1314":"Social_security_funds_It_corresponds_to_subsector_S_1314_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_117_of_Annex_A_extended_to_the_rest_of_the_world",
		"S14":"Households_extended_to_the_rest_of_the_world",
		"S14_A":"Households_that_are_sole_proprietorships_partnerships_without_legal_status_Sole_proprietorships_and_partnerships_without_legal_status_included_in_the_sector_S_14_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_118_to_2_121_of_Annex_A_extended_to_the_rest_of_the_world",
		"S14_B":"Households_other_than_sole_proprietorships_partnerships_without_legal_status_It_corresponds_to_sector_S_14_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_118_to_2_121_of_Annex_A_extended_to_the_rest_of_the_world_other_than_sole_proprietorships_and_partnerships_without_legal_status",
		"S15":"Non_profit_institutions_serving_households_It_corresponds_to_sector_S_15_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_129_to_2_130_of_Annex_A_extended_to_the_rest_of_the_world",
}

	INSTTNL_SCTR_EBA_ITS = models.CharField("INSTTNL_SCTR_EBA_ITS",max_length=255, choices=INSTTTNL_SCTR_domain,default=None, blank=True, null=True, db_comment="INSTTTNL_SCTR_domain")

	INSTTTNL_SCTR_domain = {		"S11":"Non_financial_corporations_It_corresponds_to_sector_S_11_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_45_to_2_50_of_Annex_A_extended_to_the_rest_of_the_world",
		"S121":"Central_banks_It_corresponds_to_subsector_S_121_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_72_to_2_74_of_Annex_A_extended_to_the_rest_of_the_world",
		"S122_A":"Credit_institutions_Credit_institutions_as_defined_in_Article_4_1_1_of_Regulation_EU_No_575_2013",
		"S122_A_1":"Credit_institutions_not_including_entities_according_to_the_article_2_5_Directive_2013_36_EU",
		"S122_A_2":"Credit_institutions_according_to_the_article_2_5_Directive_2013_36_EU",
		"S122_B1":"Electronic_money_institutions_principally_engaged_in_financial_intermediation_Electronic_money_institutions_as_defined_in_Directive_2009_110_EC_article_2_1_that_are_principally_engaged_in_financial_intermediation_as_defined_in_Regulation_EU_no_549_2013_paragraph_2_56_of_Annex_A",
		"S122_B2":"Deposit_taking_corporations_except_the_central_bank_other_than_credit_institutions_and_electronic_money_institutions_It_corresponds_to_subsector_S_122_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_75_to_2_78_of_Annex_A_extended_to_the_rest_of_the_world_other_than_credit_institutions_as_defined_in_Article_4_1_1_of_Regulation_EU_No_575_2013_and_electronic_money_institutions_as_defined_in_Directive_2009_110_EC_article_2_1",
		"S123":"Money_Market_Funds_MMFs_It_corresponds_to_subsector_S_123_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_79_to_2_81_of_Annex_A_extended_to_the_rest_of_the_world",
		"S124":"Non_MMF_investment_funds_It_corresponds_to_subsector_S_124_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_82_to_2_85_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_A":"Financial_Vehicle_Corporations_FVCs_FVCs_as_defined_in_Article_1_of_Regulation_EU_No_1075_2013",
		"S125_B":"Security_and_derivative_dealers_Security_and_derivative_dealers_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_91_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_C":"Financial_corporations_engaged_in_lending_Financial_corporations_engaged_in_lending_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_92_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_D":"Specialised_financial_corporations_other_than_CCPs_Specialised_financial_corporations_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_93_of_Annex_A_extended_to_the_rest_of_the_world_other_than_CCPs_as_defined_in_point_1_of_Article_2_of_Regulation_EU_No_648_2012",
		"S125_E":"Central_Counterparties_CCPs_CCPs_as_defined_in_point_1_of_Article_2_of_Regulation_EU_No_648_2012",
		"S125_I":"Other_financial_intermediaries_except_insurance_corporations_and_pension_funds_other_than_CCPs_FVCs_security_and_derivative_dealers_financial_corporations_engaged_in_lending_and_specialised_financial_corporations_It_corresponds_to_subsector_S_125_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_86_to_2_94_of_Annex_A_extended_to_the_rest_of_the_world_other_than_CCPs_as_defined_in_point_1_of_Article_2_of_Regulation_EU_No_648_2012_FVCs_as_defined_in_Article_1_of_Regulation_EU_No_1075_2013_and_security_and_derivative_dealers_financial_corporations_engaged_in_lending_and_specialised_financial_corporations_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_91_2_92_and_2_93_respectively_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_W":"Other_financial_corporations_excluding_financial_vehicle_corporations",
		"S126":"Financial_auxiliaries_It_corresponds_to_subsector_S_126_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_63_and_2_95_to_2_97_of_Annex_A_extended_to_the_rest_of_the_world",
		"S127":"Captive_financial_institutions_and_money_lenders_It_corresponds_to_subsector_S_127_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_98_to_2_99_of_Annex_A_extended_to_the_rest_of_the_world",
		"S128":"Insurance_corporations_It_corresponds_to_subsector_S_128_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_100_to_2_104_of_Annex_A_extended_to_the_rest_of_the_world",
		"S129":"Pension_funds_It_corresponds_to_subsector_S_129_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_105_to_2_110_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1311":"Central_government_excluding_social_security_funds_It_corresponds_to_subsector_S_1311_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_114_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1312":"State_government_excluding_social_security_funds_It_corresponds_to_subsector_S_1312_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_115_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1313":"Local_government_excluding_social_security_funds_It_corresponds_to_subsector_S_1313_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_116_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1314":"Social_security_funds_It_corresponds_to_subsector_S_1314_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_117_of_Annex_A_extended_to_the_rest_of_the_world",
		"S14":"Households_extended_to_the_rest_of_the_world",
		"S14_A":"Households_that_are_sole_proprietorships_partnerships_without_legal_status_Sole_proprietorships_and_partnerships_without_legal_status_included_in_the_sector_S_14_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_118_to_2_121_of_Annex_A_extended_to_the_rest_of_the_world",
		"S14_B":"Households_other_than_sole_proprietorships_partnerships_without_legal_status_It_corresponds_to_sector_S_14_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_118_to_2_121_of_Annex_A_extended_to_the_rest_of_the_world_other_than_sole_proprietorships_and_partnerships_without_legal_status",
		"S15":"Non_profit_institutions_serving_households_It_corresponds_to_sector_S_15_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_129_to_2_130_of_Annex_A_extended_to_the_rest_of_the_world",
}

	INSTTNL_SCTR_SHS = models.CharField("INSTTNL_SCTR_SHS",max_length=255, choices=INSTTTNL_SCTR_domain,default=None, blank=True, null=True, db_comment="INSTTTNL_SCTR_domain")

	INSTTTNL_SCTR_domain = {		"S11":"Non_financial_corporations_It_corresponds_to_sector_S_11_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_45_to_2_50_of_Annex_A_extended_to_the_rest_of_the_world",
		"S121":"Central_banks_It_corresponds_to_subsector_S_121_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_72_to_2_74_of_Annex_A_extended_to_the_rest_of_the_world",
		"S122_A":"Credit_institutions_Credit_institutions_as_defined_in_Article_4_1_1_of_Regulation_EU_No_575_2013",
		"S122_A_1":"Credit_institutions_not_including_entities_according_to_the_article_2_5_Directive_2013_36_EU",
		"S122_A_2":"Credit_institutions_according_to_the_article_2_5_Directive_2013_36_EU",
		"S122_B1":"Electronic_money_institutions_principally_engaged_in_financial_intermediation_Electronic_money_institutions_as_defined_in_Directive_2009_110_EC_article_2_1_that_are_principally_engaged_in_financial_intermediation_as_defined_in_Regulation_EU_no_549_2013_paragraph_2_56_of_Annex_A",
		"S122_B2":"Deposit_taking_corporations_except_the_central_bank_other_than_credit_institutions_and_electronic_money_institutions_It_corresponds_to_subsector_S_122_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_75_to_2_78_of_Annex_A_extended_to_the_rest_of_the_world_other_than_credit_institutions_as_defined_in_Article_4_1_1_of_Regulation_EU_No_575_2013_and_electronic_money_institutions_as_defined_in_Directive_2009_110_EC_article_2_1",
		"S123":"Money_Market_Funds_MMFs_It_corresponds_to_subsector_S_123_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_79_to_2_81_of_Annex_A_extended_to_the_rest_of_the_world",
		"S124":"Non_MMF_investment_funds_It_corresponds_to_subsector_S_124_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_82_to_2_85_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_A":"Financial_Vehicle_Corporations_FVCs_FVCs_as_defined_in_Article_1_of_Regulation_EU_No_1075_2013",
		"S125_B":"Security_and_derivative_dealers_Security_and_derivative_dealers_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_91_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_C":"Financial_corporations_engaged_in_lending_Financial_corporations_engaged_in_lending_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_92_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_D":"Specialised_financial_corporations_other_than_CCPs_Specialised_financial_corporations_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_93_of_Annex_A_extended_to_the_rest_of_the_world_other_than_CCPs_as_defined_in_point_1_of_Article_2_of_Regulation_EU_No_648_2012",
		"S125_E":"Central_Counterparties_CCPs_CCPs_as_defined_in_point_1_of_Article_2_of_Regulation_EU_No_648_2012",
		"S125_I":"Other_financial_intermediaries_except_insurance_corporations_and_pension_funds_other_than_CCPs_FVCs_security_and_derivative_dealers_financial_corporations_engaged_in_lending_and_specialised_financial_corporations_It_corresponds_to_subsector_S_125_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_86_to_2_94_of_Annex_A_extended_to_the_rest_of_the_world_other_than_CCPs_as_defined_in_point_1_of_Article_2_of_Regulation_EU_No_648_2012_FVCs_as_defined_in_Article_1_of_Regulation_EU_No_1075_2013_and_security_and_derivative_dealers_financial_corporations_engaged_in_lending_and_specialised_financial_corporations_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_91_2_92_and_2_93_respectively_of_Annex_A_extended_to_the_rest_of_the_world",
		"S125_W":"Other_financial_corporations_excluding_financial_vehicle_corporations",
		"S126":"Financial_auxiliaries_It_corresponds_to_subsector_S_126_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_63_and_2_95_to_2_97_of_Annex_A_extended_to_the_rest_of_the_world",
		"S127":"Captive_financial_institutions_and_money_lenders_It_corresponds_to_subsector_S_127_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_98_to_2_99_of_Annex_A_extended_to_the_rest_of_the_world",
		"S128":"Insurance_corporations_It_corresponds_to_subsector_S_128_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_100_to_2_104_of_Annex_A_extended_to_the_rest_of_the_world",
		"S129":"Pension_funds_It_corresponds_to_subsector_S_129_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_105_to_2_110_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1311":"Central_government_excluding_social_security_funds_It_corresponds_to_subsector_S_1311_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_114_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1312":"State_government_excluding_social_security_funds_It_corresponds_to_subsector_S_1312_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_115_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1313":"Local_government_excluding_social_security_funds_It_corresponds_to_subsector_S_1313_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_116_of_Annex_A_extended_to_the_rest_of_the_world",
		"S1314":"Social_security_funds_It_corresponds_to_subsector_S_1314_as_defined_in_Regulation_EU_No_549_2013_paragraph_2_117_of_Annex_A_extended_to_the_rest_of_the_world",
		"S14":"Households_extended_to_the_rest_of_the_world",
		"S14_A":"Households_that_are_sole_proprietorships_partnerships_without_legal_status_Sole_proprietorships_and_partnerships_without_legal_status_included_in_the_sector_S_14_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_118_to_2_121_of_Annex_A_extended_to_the_rest_of_the_world",
		"S14_B":"Households_other_than_sole_proprietorships_partnerships_without_legal_status_It_corresponds_to_sector_S_14_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_118_to_2_121_of_Annex_A_extended_to_the_rest_of_the_world_other_than_sole_proprietorships_and_partnerships_without_legal_status",
		"S15":"Non_profit_institutions_serving_households_It_corresponds_to_sector_S_15_as_defined_in_Regulation_EU_No_549_2013_paragraphs_2_129_to_2_130_of_Annex_A_extended_to_the_rest_of_the_world",
}

	INSTTTNL_SCTR = models.CharField("INSTTTNL_SCTR",max_length=255, choices=INSTTTNL_SCTR_domain,default=None, blank=True, null=True, db_comment="INSTTTNL_SCTR_domain")

	CNTRLLD_NTNL_FRGN_BDS_INPT_domain = {		"0":"Not_applicable",
		"2":"National_private",
		"3":"Foreign_controlled",
}

	INSTTTNL_SCTR_CNTRL = models.CharField("INSTTTNL_SCTR_CNTRL",max_length=255, choices=CNTRLLD_NTNL_FRGN_BDS_INPT_domain,default=None, blank=True, null=True, db_comment="CNTRLLD_NTNL_FRGN_BDS_INPT_domain")

	INTRNTNL_ORGNSTNS_INPT_domain = {		"0":"Not_applicable",
		"1C":"IMF_International_Monetary_Fund",
		"1D":"WTO_World_Trade_Organization",
		"1E":"IBRD_International_Bank_for_Reconstruction_and_Development",
		"1F":"IDA_International_Development_Association",
		"1G":"ICSID_International_Centre_for_Settlement_of_Investment_Disputes",
		"1H":"UNESCO_United_Nations_Educational_Scientific_and_Cultural_Organisation",
		"1J":"FAO_Food_and_Agriculture_Organisation",
		"1K":"WHO_World_Health_Organisation",
		"1L":"IFAD_International_Fund_for_Agricultural_Development",
		"1M":"IFC_International_Finance_Corporation",
		"1N":"MIGA_Multilateral_Investment_Guarantee_Agency",
		"1O":"UNICEF_United_Nations_Children_Fund",
		"1P":"UNHCR_United_Nations_High_Commissioner_for_Refugees",
		"1Q":"UNRWA_United_Nations_Relief_and_Works_Agency_for_Palestine",
		"1R":"IAEA_International_Atomic_Energy_Agency",
		"1S":"ILO_International_Labour_Organisation",
		"1T":"ITU_International_Telecommunication_Union",
		"1U":"Rest_of_UN_Organisations_n_i_e",
		"4B":"EMS_European_Monetary_System",
		"4C":"EIB_European_Investment_Bank",
		"4D":"EC_European_Commission",
		"4E":"EDF_European_Development_Fund",
		"4F":"ECB_European_Central_Bank",
		"4G":"EIF_European_Investment_Fund",
		"4H":"ECSC_European_Community_of_Steel_and_Coal",
		"4I":"NIF_Neighbourhood_Investment_Facility",
		"4J1":"EP_European_Parliament",
		"4J2":"CEU_Council_of_the_European_Union",
		"4J3":"CJEU_Court_of_Justice",
		"4J4":"ECA_Court_of_Auditors",
		"4J5":"European_Council",
		"4J6":"ESC_Economic_and_Social_Committee",
		"4J7":"CR_Committee_of_Regions",
		"4J8":"Other_small_European_Union_Institutions_Ombudsman_Data_Protection_Supervisor_etc",
		"4M":"SRB_Single_Resolution_Board",
		"4R":"EU_Africa_Infrastructure_Trust_Fund",
		"4S":"ESM_European_Stability_Mechanism",
		"4T1":"EBA_European_Banking_Authority",
		"4T2":"ESMA_European_Securities_and_Markets_Authority",
		"4T3":"EIOPA_European_Insurance_and_Occupational_Pensions_Authority",
		"4U":"EURATOM_European_Atomic_Energy_Community",
		"4V":"FEMIP_Facility_for_Euro_Mediterranean_Investment_and_Partnership",
		"5B":"BIS_Bank_for_International_Settlements",
		"5C":"IADB_Inter_American_Development_Bank",
		"5D":"AfDB_African_Development_Bank",
		"5E":"AsDB_Asian_Development_Bank",
		"5F":"EBRD_European_Bank_for_Reconstruction_and_Development",
		"5G":"IIC_Inter_American_Investment_Corporation",
		"5H":"NIB_Nordic_Investment_Bank",
		"5I":"ECCB_Eastern_Caribbean_Central_Bank",
		"5J":"IBEC_International_Bank_for_Economic_Co_operation",
		"5K":"IIB_International_Investment_Bank",
		"5L":"CDB_Caribbean_Development_Bank",
		"5M":"AMF_Arab_Monetary_Fund",
		"5N":"BADEA_Banque_arabe_pour_le_developpement_economique_en_Afrique_Arab_Bank_for_Economic_Development_in_Africa",
		"5O":"BCEAO_Banque_Centrale_des_Etats_de_l_Afrique_de_l_Ouest_West_African_Central_Bank",
		"5P":"CASDB_Central_African_States_Development_Bank",
		"5Q":"AfDF_African_Development_Fund",
		"5R":"AsDF_Asian_Development_Fund",
		"5S":"SDF_Fonds_special_unifie_de_developpement_Special_Development_Fund_related_to_the_Caribbean_Development_Bank",
		"5T":"CABEI_Central_American_Bank_for_Economic_Integration",
		"5U":"ADC_Andean_Development_Corporation",
		"5W":"BEAC_Banque_des_Etats_de_l_Afrique_Centrale",
		"5Z":"Other_International_Financial_Organisations_n_i_e",
		"6B":"NATO_North_Atlantic_Treaty_Organisation",
		"6C":"CE_Council_of_Europe",
		"6D":"ICRC_International_Committee_of_the_Red_Cross",
		"6E":"ESA_European_Space_Agency",
		"6F":"EPO_European_Patent_Office",
		"6G":"EUROCONTROL_European_Organisation_for_the_Safety_of_Air_Navigation",
		"6H":"EUTELSAT_European_Telecommunications_Satellite_Organisation",
		"6I":"EMBL_European_Molecular_Biology_Laboratory",
		"6J":"INTELSAT_International_Telecommunications_Satellite_Organisation",
		"6K":"EBU_UER_European_Broadcasting_Union_Union_europeenne_de_radio_television",
		"6L":"EUMETSAT_European_Organisation_for_the_Exploitation_of_Meteorological_Satellites",
		"6M":"ESO_European_Southern_Observatory",
		"6N":"ECMWF_European_Centre_for_Medium_Range_Weather_Forecasts",
		"6O":"OECD_Organisation_for_Economic_Co_operation_and_Development",
		"6P":"CERN_European_Organisation_for_Nuclear_Research",
		"6Q":"IOM_International_Organisation_for_Migration",
		"6Z":"Other_International_Non_Financial_Organisations_n_i_e",
		"7A":"WAEMU_West_African_Economic_and_Monetary_Union",
		"7B":"IDB_Islamic_Development_Bank",
		"7C":"EDB_Eurasian_Development_Bank",
		"7D":"Paris_Club_Creditor_Institutions",
		"7E":"CEB_Council_of_Europe_Development_Bank",
		"7F":"International_Union_of_Credit_and_Investment_Insurers",
		"7G":"BSTDB_Black_Sea_Trade_and_Development_Bank",
		"7H":"AFREXIMBANK_African_Export_Import_Bank",
		"7I":"BLADEX_Banco_Latino_Americano_De_Comercio_Exterior_Foreign_Trade_Bank_of_Latin_America",
		"7J":"FLAR_Fondo_Latino_Americano_de_Reservas_LARF_Latin_American_Reserve_Fund",
		"7K":"RDC_Fonds_Belgo_Congolais_d_Amortissement_et_de_Gestion",
		"7L":"IFFIm_International_finance_Facility_for_Immunisation",
		"7M":"EUROFIMA_European_Company_for_the_Financing_of_Railroad_Rolling_Stock",
}

	INTRNTNL_ORGNSTN_CD = models.CharField("INTRNTNL_ORGNSTN_CD",max_length=255, choices=INTRNTNL_ORGNSTNS_INPT_domain,default=None, blank=True, null=True, db_comment="INTRNTNL_ORGNSTNS_INPT_domain")

	LDNG_BRNCH_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"46":"Leading_branch",
		"47":"Non_leading_branch",
}

	LDNG_BRNCH_ANCRDT_RPRTNG_INDCTR = models.CharField("LDNG_BRNCH_ANCRDT_RPRTNG_INDCTR",max_length=255, choices=LDNG_BRNCH_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="LDNG_BRNCH_INDCTR_INPT_domain")

	LEI = models.CharField("LEI",max_length=255,default=None, blank=True, null=True)

	LGL_FRM_INPT_domain = {		"0":"Not_applicable",
		"AT102":"OG_Offene_Gesellschaft_General_partnership",
		"AT103":"KG_Kommanditgesellschaft_Limited_partnership",
		"AT201":"AG_Aktiengesellschaft_Plc_UK",
		"AT202":"GmbH_Gesellschaft_mit_beschrankter_Haftung_Ltd_UK",
		"AT401":"GEN_Erwerbs_und_Wirtschaftsgenossenschaft_Cooperative",
		"AT501":"V_Versicherungsverein_auf_Gegenseitigkeit_Mutual_Insurance_Corporation",
		"AT601":"EUNT_Einzelunternehmen_Sole_trader_UK_individual_enterprise",
		"AT603":"P_Privatstiftung_Private_foundation",
		"AT604":"S_Sparkasse_Mutual_Savings_Bank",
		"AT605":"SR_Sonstiger_Rechtstrager_Other_Legal_Entity",
		"AT607":"Sonstige_Rechtsform_Other_legal_forms",
		"AT609":"GesbR_Gesellschaft_des_burgerlichen_Rechts_Partnership_under_civil_code",
		"AT610":"OrK_Offentlich_rechtliche_Korperschaften_public_corporation_corporation_of_public_law",
		"AT611":"OrS_Offentlich_rechtliche_Stiftungen_public_trust_corporation_of_public_law",
		"AT612":"VER_Vereine_registered_association_corporation_of_public_law",
		"AT613":"EG_Eigentumergemeinschaft_owner_association",
		"BE000":"Old_or_dismissed_legal_forms_no_longer_applicable_Anciennes_formes_juridiques_plus_applicable_Oude_rechtsvormen_niet_langer_van_toepassing_Alte_Rechtsformen_nicht_mehr_anwendbar",
		"BE002":"OFP_OFP_OFP_Organisation_for_financing_pensions_Organisme_de_financement_de_pensions_Organisme_voor_de_Financiering_van_Pensioenen_Organismus_fur_die_Finanzierung_von_Pensionen",
		"BE003":"UTVA_BTWE_MWSE_Unite_TVA_BTW_eenheid_Mehrwertsteuereinheit_Organisme_de_financement_de_pensions_Organisme_voor_de_Financiering_van_Pensioenen_Organismus_fur_die_Finanzierung_von_Pensionen",
		"BE006":"SCRI_CVOA_Gen_mubH_Cooperative_partnership_with_unlimited_liability_Societe_cooperative_a_responsabilite_illimitee_Cooperatieve_vennootschap_met_onbeperkte_aansprakelijkheid_Genossenschaft_mit_unbeschrankter_Haftung",
		"BE008":"SCRL_CVBA_Gen_mbH_Cooperative_company_with_limited_liability_Societe_cooperative_a_responsabilite_limitee_Cooperatieve_vennootschap_met_beperkte_aansprakelijkheid_Genossenschaft_mit_beschrankter_Haftung",
		"BE011":"SNC_V_O_F_OHG_General_partnership_Societe_en_nom_collectif_Vennootschap_onder_firma_Offene_Handelsgesellschaft",
		"BE012":"SCS_Comm_V_EKG_Ordinary_limited_partnership_Societe_en_commandite_simple_Gewone_commanditaire_vennootschap_Einfache_Kommanditgesellschaft",
		"BE013":"SCA_Comm_VA_KGaA_Partnership_limited_by_shares_Societe_en_commandite_par_actions_Commanditaire_vennootschap_op_aandelen_Kommanditgesellschaft_auf_Aktien",
		"BE014":"SA_NV_AG_Public_limited_company_Societe_anonyme_Naamloze_vennootschap_Aktiengesellschaft",
		"BE015":"SPRL_BVBA_PGmbH_Private_limited_liability_company_Societe_privee_a_responsabilite_limitee_Besloten_vennootschap_met_beperkte_aansprakelijkheid_Privatgesellschaft_mit_beschrankter_Haftung",
		"BE017":"ASBL_VZW_VoG_Non_profit_association_Association_sans_but_lucratif_Vereniging_zonder_winstoogmerk_Vereinigung_ohne_Gewinnerzielungsabsicht",
		"BE019":"MUTU_ZIEK_F_Kankenka_Mutual_health_fund_Mutual_Benefit_Society_National_Union_of_mutual_health_funds_Mutualite_Societe_Mutualiste_Union_nationale_de_mutualites_Ziekenfonds_Maatschappij_van_onderlinge_bijstand_Landsbond_van_ziekenfondsen_Krankenkasse_Gesellschaft_auf_Gegenseitigkeit_Krankenkassenlandesverband",
		"BE020":"UP_BV_BV_Professional_association_Union_professionnelle_Beroepsvereniging_Berufsvereinigung",
		"BE021":"AAM_OVV_PRVGaG_Mutual_insurance_association_Mutual_insurance_fund_under_private_law_Association_d_assurances_mutuelles_Caisse_commune_d_assurances_de_droit_prive_Onderlinge_verzekeringsvereniging_Gemeenschappelijke_verzekeringskas_van_privaat_recht_Versicherungsvereinigung_auf_Gegenseitigkeit_Privatrechtliche_Versicherungsgesellschaft",
		"BE023":"AEP_BPR_PRaV_Foreign_private_associations_with_establishment_in_Belgium_Associations_etrangeres_privees_avec_etablissement_agence_bureau_succursale_en_Belgique_Buitenlandse_privaatrechtelijke_verenigingen_met_vestiging_agentschap_kantoor_of_bijhuis_in_Belgie_Privatrechtliche_auslandische_Vereinigungen_mit_Niederlassung_Geschaftsstelle_Buro_oder_Zweigstelle_in_Belgien",
		"BE025":"S_Agr_LV_LG_Agricultural_company_Societe_agricole_Landbouwvennootschap_Landwirtschaftliche_Gesellschaft",
		"BE026":"FONDPRIV_PRIV_ST_PrSt_Private_Foundation_Fondation_privee_Private_stichting_Privatstiftung",
		"BE028":"ISBL_IZW_EoG_Non_profit_institution_Institution_sans_but_lucratif_Instelling_zonder_winstoogmerk_Einrichtung_ohne_Gewinnerzielungsabsicht",
		"BE029":"FUP_SON_gnS_Public_utility_foundation_Fondation_d_utilite_publique_Stichting_van_openbaar_nut_Gemeinnutzige_Stiftung",
		"BE030":"ENT_E_BO_AGes_Foreign_company_Entreprise_etrangere_Buitenlandse_onderneming_Auslandische_Gesellschaft",
		"BE051":"FDP_PJ_PRV_PRRFmRP_Other_private_law_form_with_legal_personality_Autre_forme_de_droit_prive_avec_personnalite_juridique_Andere_privaatrechtelijke_vorm_met_rechtspersoonlijkheid_Andere_privatrechtliche_Rechtsform_mit_Rechtspersonlichkeit",
		"BE060":"GIE_ESV_WIV_Economic_interest_grouping_Groupement_d_interet_economique_Economisch_samenwerkingsverband_Wirtschaftliche_Interessenvereinigung",
		"BE070":"ACP_VME_MEV_Joint_owners_association_Association_des_coproprietaires_Vereniging_van_mede_eigenaars_Miteigentumervereinigung",
		"BE107":"SCRI_CP_CVOA_CD_GmuHGB_Cooperative_company_with_unlimited_liability_Participating_cooperative_governed_by_public_law_Cooperative_a_responsabilite_illimitee_cooperative_de_participation_de_droit_public_Cooperatieve_vennootschap_met_onbeperkte_aansprakelijkheid_bij_wijze_van_deelneming_van_publiek_recht_Offentlich_rechtliche_Genossenschaft_mit_unbeschrankter_Haftung_Genossenschaft_auf_Beteiligung",
		"BE108":"SCRL_DPU_CVBA_PR_OfrGmbH_Cooperative_company_with_limited_liability_governed_by_public_law_Societe_cooperative_a_responsabilite_limitee_de_droit_public_Cooperatieve_vennootschap_met_beperkte_aansprakelijkheid_van_publiek_recht_Offentlich_rechtliche_Genossenschaft_mit_beschrankter_Haftung",
		"BE114":"SA_DPU_NV_PR_O_r_AG_Public_limited_company_governed_by_public_law_Societe_anonyme_de_droit_public_Naamloze_vennootschap_van_publiek_recht_Offentlich_rechtliche_Aktiengesellschaft",
		"BE117":"ASBL_DPU_VZW_PR_OrVohGza_Non_profit_association_governed_by_public_law_Association_sans_but_lucratif_de_droit_public_Vereniging_zonder_winstoogmerk_van_publiek_recht_Offentlich_rechtliche_Vereinigung_ohne_Gewinnerzielungsabsicht",
		"BE121":"SAM_DPU_OVV_PR_OrVgGe_Mutual_insurance_association_governed_by_public_law_Association_d_assurances_mutuelles_de_droit_public_Onderlinge_verzekeringsvereniging_van_publiek_recht_Offentlich_rechtliche_Versicherungsvereinigung_auf_Gegenseitigkeit",
		"BE124":"ETSPUBLI_OI_OE_Public_institution_Etablissement_public_Openbare_instelling_Offentliche_Einrichtung",
		"BE125":"AISBL_IVZW_IVoG_International_non_profit_association_Association_internationale_sans_but_lucratif_Internationale_vereniging_zonder_winstoogmerk_Internationale_Vereinigung_ohne_Gewinnerzielungsabsicht",
		"BE127":"PIETE_BVB_LH_Pawnshop_Monts_de_Piete_Berg_van_Barmhartigheid_Pfandleihhaus",
		"BE129":"PW_PW_Ewg_Bwg_Polder_watering_Polder_wateringue_Polder_Watering_Entwasserungsgenossenschaft_Bewasserungsgenossenschaft",
		"BE151":"AFJ_AV_ARF_Other_legal_form_active_Autre_forme_juridique_Andere_rechtsvorm_Andere_Rechtsform",
		"BE160":"OPEI_BIPO_AIOE_Foreign_or_international_public_institution_Organisme_public_etranger_ou_international_Buitenlandse_of_internationale_publieke_organisatie_Auslandische_oder_internationale_offentliche_Einrichtungen",
		"BE200":"SF_VV_GbG_Company_under_formation_Societe_en_formation_Vennootschap_in_oprichting_In_Grundung_befindliche_Gesellschaft",
		"BE206":"SC_SCRI_BV_CVOA_ZvGGugcH_Non_trading_company_in_the_form_of_a_cooperative_company_with_unlimited_liability_Societe_civile_sous_forme_de_societe_cooperative_a_responsabilite_illimitee_Burgerlijke_vennootschap_onder_vorm_van_cooperatieve_vennootschap_met_onbeperkte_aansprakelijkheid_Zivilrechtliche_Gesellschaft_in_der_Rechtsform_einer_Genossenschaft_mit_unbeschrankter_Haftung",
		"BE208":"SC_SCRL_BV_CVBA_ZvGGbH_Non_trading_company_in_the_form_of_a_cooperative_company_with_limited_liability_Societe_civile_sous_forme_de_societe_cooperative_a_responsabilite_limitee_Burgerlijke_vennootschap_onder_vorm_van_cooperatieve_vennootschap_met_beperkte_aansprakelijkheid_Zivilrechtliche_Gesellschaft_in_der_Rechtsform_einer_Genossenschaft_mit_beschrankter_Haftung",
		"BE211":"SC_SNC_BV_VOF_ZRG_OHG_Non_trading_company_in_the_form_of_a_general_partnership_Societe_civile_sous_forme_de_societe_en_nom_collectif_Burgerlijke_vennootschap_onder_vorm_van_vennootschap_onder_firma_Zivilrechtliche_Gesellschaft_in_der_Rechtsform_einer_offenen_Handelsgesellschaft",
		"BE212":"SC_SCS_BV_GCV_ZRG_EKG_Non_trading_company_in_the_form_of_an_ordinary_limited_partnership_Societe_civile_sous_forme_de_societe_en_commandite_simple_Burgerlijke_vennootschap_onder_vorm_van_gewone_commanditaire_vennootschap_Zivilrechtliche_Gesellschaft_in_der_Rechtsform_einer_einfachen_Kommanditgesellschaft",
		"BE213":"SC_SCA_BV_CVA_ZRG_KGaA_Non_trading_company_in_the_form_of_a_partnership_limited_by_shares_Societe_civile_sous_forme_de_societe_en_commandite_par_actions_Burgerlijke_vennootschap_onder_vorm_van_commanditaire_vennootschap_op_aandelen_Zivilrechtliche_Gesellschaft_in_der_Rechtsform_einer_Kommanditgesellschaft_auf_Aktien",
		"BE214":"SC_SA_BV_NV_ZRG_AG_Non_trading_company_in_the_form_of_a_public_limited_company_Societe_civile_sous_forme_de_societe_anonyme_Burgerlijke_vennootschap_onder_vorm_van_naamloze_vennootschap_Zivilrechtliche_Gesellschaft_in_der_Rechtsform_einer_Aktiengesellschaft",
		"BE215":"SC_SPRL_BV_BVBA_ZvGPgbH_Non_trading_company_in_the_form_of_a_private_limited_liability_company_Societe_civile_sous_forme_de_societe_privee_a_responsabilite_limitee_Burgerlijke_vennootschap_onder_vorm_van_besloten_vennootschap_met_beperkte_aansprakelijkheid_Zivilrechtliche_Gesellschaft_in_der_Rechtsform_einer_Privatgesellschaft_mit_beschrankter_Haftung",
		"BE217":"PPEU_PPEU_EUPP_European_political_party_Parti_politique_europeen_Europese_politieke_partij_Europaische_politische_Partei",
		"BE218":"FPEU_FPEU_EUPS_European_political_foundation_Fondation_politique_europeenne_Europese_politieke_stichting_Europaische_politische_Stiftung",
		"BE225":"SC_SAGR_BV_LV_ZRG_LG_Non_trading_company_in_the_form_of_an_agricultural_company_Societe_civile_sous_forme_de_societe_agricole_Burgerlijke_Vennootschap_onder_vorm_van_Landbouwvennootschap_BV_LV_Zivilrechtliche_Gesellschaft_in_der_Rechtsform_einer_landwirtschaftlichen_Gesellschaft",
		"BE301":"SPF_FOD_FOD_Federal_Public_Service_Service_public_federal_Federale_overheidsdienst_Foderaler_offentlicher_Dienst",
		"BE302":"SPP_POD_FOP_Federal_Public_Planning_Service_Service_public_federal_de_programmation_Programmatorische_federale_overheidsdienst_Foderaler_offentlicher_Programmierungsdienst",
		"BE303":"SERVFEDE_FEDEDIEN_FodD_Other_federal_service_Autre_service_federal_Andere_federale_dienst_Anderer_foderale_Dienst",
		"BE310":"REGCOMNL_VLGEWGEM_FlRG_Authorities_of_the_Flemish_Region_and_the_Flemish_Community_Autorite_de_la_Region_flamande_et_de_la_Communaute_flamande_Overheid_van_het_Vlaamse_Gewest_en_van_de_Vlaamse_Gemeenschap_Behorde_der_Flamischen_Region_und_der_Flamischen_Gemeinschaft",
		"BE320":"RW_WG_WR_Authorities_of_the_Walloon_Region_Autorite_de_la_Region_wallonne_Overheid_van_het_Waalse_Gewest_Behorde_der_Wallonischen_Region",
		"BE325":"AISBL_DPU_IVZW_PR_OrIVoG_International_non_profit_association_governed_by_public_law_Internationale_vereniging_zonder_winstoogmerk_van_publiek_recht_Offentlich_rechtliche_Internationale_Vereinigung_ohne_Gewinnerzielungsabsicht_AISBL_DPU",
		"BE330":"REGBRXCA_BRUHOOGE_RBH_Authorities_of_the_Brussels_Capital_Region_Autorite_de_la_Region_de_Bruxelles_Capitale_Overheid_van_het_Brusselse_Hoofdstedelijk_Gewest_Behorde_der_Region_Brussel_Hauptstadt",
		"BE340":"COMMFRAN_FRAGEMEE_FrG_Authorities_of_the_French_Community_Autorite_de_la_Communaute_francaise_Overheid_van_de_Franse_Gemeenschap_Behorde_der_Franzosischen_Gemeinschaft",
		"BE350":"COMGERMA_DUITGEME_DG_Authorities_of_the_German_speaking_Community_Autorite_de_la_Communaute_germanophone_Overheid_van_de_Duitstalige_Gemeenschap_Behorde_der_Deutschsprachigen_Gemeinschaft",
		"BE400":"AUTOPROV_PROVOVER_Provbeho_Provincial_Authority_Autorite_provinciale_Provinciale_overheid_Provinzialbehorde",
		"BE411":"COMMUNES_GEMEENTE_Gemeinde_City_municipality_Ville_commune_Stad_gemeente_Stadt_Gemeinde",
		"BE412":"CPAS_OCMW_OSHZ_Public_social_welfare_centre_Centre_public_d_action_sociale_Openbaar_centrum_voor_maatschappelijk_welzijn_Offentliches_Sozialhilfezentrum",
		"BE413":"POLLOC_LOKPOL_LP_Local_Police_Police_locale_Lokale_politiezone_Lokale_Polizeizone",
		"BE414":"IC_IC_IK_Intermunicipal_company_Intercommunale_Intercommunale_Interkommunale",
		"BE415":"APROJ_PROJ_V_Prjverng_Project_association_Association_de_projet_Projectvereniging_Projektvereinigung",
		"BE416":"ASS_SERV_DIENSTV_DlvFL_Services_provider_association_Flemish_Region_Association_prestataire_de_services_Region_flamande_Dienstverlenende_vereniging_Vlaams_Gewest_Dienstleistungsvereinigung_Flamische_Region",
		"BE417":"ACMISS_OPDRAVER_BVerFL_Project_entrusted_association_Flemish_Region_Association_chargee_de_mission_Region_flamande_Opdrachthoudende_vereniging_Vlaams_Gewest_Beauftragte_Vereinigung_Flamische_Region",
		"BE418":"RCOMAUT_AUTOGEMB_AutGemRg_Autonomous_municipal_company_Regie_communale_autonome_Autonoom_gemeentebedrijf_Autonome_Gemeinderegie",
		"BE419":"RPROVAUT_AUTOPRB_AutPrvRg_Autonomous_provincial_company_Regie_provinciale_autonome_Autonoom_provinciebedrijf_Autonome_Provinzialregie",
		"BE420":"Ass_CPAS_Ver_OCMW_VOSHZ_Association_of_public_centres_for_social_welfare_Association_de_CPAS_Vereniging_van_OCMW_s_Vereinigung_von_offentlichen_Sozialhilfezentren",
		"BE422":"ZDS_HVZ_HLZ_Relief_zone_Zone_de_secours_Hulpverleningszone_Hilfeleistungszone",
		"BE506":"SCRI_FS_CVOA_SO_GuHsZ_Cooperative_company_with_unlimited_liability_with_a_social_purpose_Societe_cooperative_a_responsabilite_illimitee_a_finalite_sociale_Cooperatieve_vennootschap_met_onbeperkte_aansprakelijkheid_met_een_sociaal_oogmerk_Genossenschaft_mit_unbeschrankter_Haftung_mit_sozialer_Zielsetzung",
		"BE508":"SCRL_FS_CVBA_SO_GbHsZ_Cooperative_company_with_limited_liability_with_a_social_purpose_Societe_cooperative_a_responsabilite_limitee_a_finalite_sociale_Cooperatieve_vennootschap_met_beperkte_aansprakelijkheid_met_een_sociaal_oogmerk_Genossenschaft_mit_beschrankter_Haftung_mit_sozialer_Zielsetzung",
		"BE511":"SNC_FS_VOF_SO_OHGmsZ_General_partnership_with_a_social_purpose_Societe_en_nom_collectif_a_finalite_sociale_Vennootschap_onder_firma_met_een_sociaal_oogmerk_Offene_Handelsgesellschaft_mit_sozialer_Zielsetzung",
		"BE512":"SCS_FS_GCW_SO_EKGmsZ_Ordinary_limited_partnership_with_a_social_purpose_Societe_en_commandite_simple_a_finalite_sociale_Gewone_commanditaire_vennootschap_met_een_sociaal_oogmerk_Einfache_Kommanditgesellschaft_mit_sozialer_Zielsetzung",
		"BE513":"SCA_FS_CVA_SO_KGaAmsZ_Partnership_limited_by_shares_with_a_social_purpose_Societe_en_commandite_par_actions_a_finalite_sociale_Commanditaire_vennootschap_op_aandelen_met_een_sociaal_oogmerk_Kommanditgesellschaft_auf_Aktien_mit_sozialer_Zielsetzung",
		"BE514":"SA_FS_NV_SO_AGmsZ_Public_limited_company_with_a_social_purpose_Societe_anonyme_a_finalite_sociale_Naamloze_vennootschap_met_een_sociaal_oogmerk_Aktiengesellschaft_mit_sozialer_Zielsetzung",
		"BE515":"SPRL_FS_BVBA_SO_PmbHsZ_Private_limited_liability_company_with_a_social_purpose_Societe_privee_a_responsabilite_limitee_a_finalite_sociale_Besloten_vennootschap_met_beperkte_aansprakelijkheid_met_een_sociaal_oogmerk_Privatgesellschaft_mit_beschrankter_Haftung_mit_sozialer_Zielsetzung",
		"BE560":"GIE_FS_ESV_SO_WIVmsZ_Economic_interest_grouping_with_a_social_purpose_Groupement_d_interet_economique_a_finalite_sociale_Economisch_samenwerkingsverband_met_een_sociaal_oogmerk_Wirtschaftliche_Interessenvereinigung_mit_sozialer_Zielsetzung",
		"BE610":"SRL_BV_GmbH_Limited_liability_company_Societe_a_responsabilite_limitee_Besloten_Vennootschap_Gesellschaft_mit_beschrankter_Haftung",
		"BE612":"Scomm_CommV_KommG_Limited_partnership_Societe_en_commandite_Commanditaire_vennootschap_Kommanditgesellschaft",
		"BE616":"SRL_DPU_BV_PR_SDPU_Limited_liability_company_governed_by_public_law_Societe_a_responsabilite_limitee_de_droit_public_Besloten_Vennootschap_van_publiek_recht_Offentlich_rechtliche_Gesellschaft_mit_beschrankter_Haftung",
		"BE617":"SCommDPU_CommV_PR_SDPU_Limited_partnership_governed_by_public_law_SCommDPU_CommV_PR_SDPU_Societe_en_commandite_de_droit_public_Commanditaire_vennootschap_van_publiek_recht_Offentlich_rechtliche_Kommanditgesellschaft",
		"BE651":"FORME_FS_VORM_SO_RFmsZ_Other_form_with_a_social_purpose_governed_by_public_law_Autre_forme_a_finalite_sociale_de_droit_public_Andere_vorm_met_een_sociaal_oogmerk_van_publiek_recht_Andere_offentlich_rechtliche_Rechtsform_mit_sozialer_Zielsetzung",
		"BE702":"SDC_MS_GaR_Partnership_Societe_de_droit_commun_Maatschap_Gesellschaft_des_allgemeinen_Rechts",
		"BE706":"SC_CV_SC_Cooperative_partnership_Societe_cooperative_Cooperatieve_vennootschap_Offentlich_rechtliche_Kommanditgesellschaft",
		"BE716":"SC_DPU_CV_PR_SDPU_Cooperative_partnership_governed_by_public_law_Societe_cooperative_de_droit_public_Cooperatieve_vennootschap_van_publiek_recht_Genossenschaft",
		"BE721":"SASPJ_VVZRL_GVoRP_Company_or_association_without_legal_personality_Societe_ou_association_sans_personnalite_juridique_Vennootschap_of_vereniging_zonder_rechtspersoonlijkheid_Gesellschaften_oder_Vereinigungen_ohne_Rechtspersonlichkeit",
		"BG101":"AD_Joint_stock_company",
		"BG102":"OOD_Limited_liability_company",
		"BG103":"KDA_Partnership_limited_by_shares",
		"BG104":"EAD_Single_person_joint_stock_company",
		"BG105":"EOOD_Single_person_limited_liability_company",
		"BG106":"KD_Limited_partnership",
		"BG107":"SD_S_ie_General_partnership",
		"BG1539":"ADSIC_Joint_Stock_Special_Investment_Company",
		"BG462":"ET_Sole_proprietor",
		"BG466":"Coop_Cooperation_Cooperative_society",
		"BG472":"DZZD_Partnership_by_Law_of_Obligations_And_Contracts",
		"CY102":"LTD_Private_limited_company_Ltd",
		"CY103":"PLC_Public_limited_company_Plc",
		"CY109":"P_Partnership",
		"CY111":"COOP_Cooperative_Societies",
		"CY112":"SP_Sole_proprietorship",
		"CY113":"SF_Societies_Foundations",
		"CY114":"PUBLaw_Entities_governed_by_public_law",
		"CY115":"B_E_Business_Name",
		"CY116":"PF_Pension_Provident_Funds",
		"CY117":"OTH_Other_legal_form",
		"CZ100":"Podnikajici_fyzicka_osoba_tuzemska_Natural_person_in_business_sole_proprietor",
		"CZ111":"v_o_s_Ve_ejna_obchodni_spole_nost_General_partnership",
		"CZ112":"s_r_o_Spole_nost_s_ru_enim_omezenym_Ltd_UK",
		"CZ113":"k_s_Spole_nost_komanditni_Limited_partnership",
		"CZ115":"Spole_ny_podnik_Joint_venture",
		"CZ116":"Zajmove_sdruzeni_Special_interest_club",
		"CZ117":"Nadace_Foundation",
		"CZ118":"Nada_ni_fond_Foundation_fund",
		"CZ121":"a_s_Akciova_spole_nost_Plc_UK",
		"CZ141":"o_p_s_Obecn_prosp_sna_spole_nost_One_of_the_legal_forms_for_non_governmental_non_profit_organizations",
		"CZ145":"svj_Spole_enstvi_vlastnik_jednotek_Owners_association_apartment_owners_association",
		"CZ151":"Komoditni_burza_Commodity_exchange",
		"CZ152":"Garan_ni_fond_obchodnik_s_cennymi_papiry_Guarantee_Fund_of_Investment_Firms",
		"CZ161":"Ustav_Institute",
		"CZ205":"Druzstvo_Cooperative",
		"CZ301":"s_p_Statni_podnik_State_enterprise",
		"CZ313":"_eska_narodni_banka_Czech_National_Bank",
		"CZ325":"Organiza_ni_slozka_statu_Organisational_unit_of_the_state",
		"CZ326":"Staly_rozhod_i_soud_Permanent_Court_of_Arbitration",
		"CZ331":"P_isp_vkova_organizace_Subsidised_organisation_semi_budgetary_organisation",
		"CZ352":"Sprava_zelezni_ni_dopravni_cesty_statni_organizace_Railway_Transport_Route_Administration_state_organisation",
		"CZ353":"Rada_pro_ve_ejny_dohled_nad_auditem_Council_for_Public_Audit_Supervision",
		"CZ361":"Ve_ejnopravni_instituce_T_Ro_TK_Public_law_institution_Czech_Television_Czech_Radio_Czech_Press_Agency",
		"CZ381":"Fond_ze_zakona_Fund_statutory",
		"CZ391":"Zdravotni_pojis_ovna_Health_insurance_company",
		"CZ421":"Odst_pny_zavod_zahrani_ni_pravnicke_osoby_Branch_of_the_foreign_legal_entity",
		"CZ422":"Organiza_ni_slozka_zahrani_niho_nada_niho_fondu_Organisational_unit_of_a_foreign_foundation_fund",
		"CZ424":"Zahrani_ni_fyzicka_osoba_Foreign_natural_person",
		"CZ521":"Samostatna_drobna_provozovna_obecniho_u_adu_Independent_small_office_of_a_municipal_office",
		"CZ541":"Podilovy_nebo_penzijni_fond_Unit_trust_or_pension_fund",
		"CZ601":"Vysoka_skola_University_college",
		"CZ641":"Skolska_pravnicka_osoba_Educational_legal_entity",
		"CZ661":"Ve_ejna_vyzkumna_instituce_Public_research_institution",
		"CZ703":"Odborova_organizace_a_organizace_zam_stnavatel_Trade_union_organisation_and_emloyers_organisation",
		"CZ704":"Zvlastni_organizace_pro_zastoupeni_eskych_zajm_v_mezinarodnich_nevladnich_organizacich_Special_organisation_to_represent_Czech_interests_in_international_non_governmental_organisations",
		"CZ705":"Podnik_nebo_hospoda_ske_za_izeni_sdruzeni_Enterprise_or_economic_organisation_of_an_association",
		"CZ706":"Spolek_Society",
		"CZ707":"Odborova_organizace_Trade_union_organisation",
		"CZ708":"Organizace_zam_stnavatel_Employers_organisation",
		"CZ711":"Politicka_strana_politicke_hnuti_Political_party_political_movement",
		"CZ715":"Podnik_nebo_hospoda_ske_za_izeni_politicke_strany_Enterprise_or_economic_organisation_of_a_political_party",
		"CZ721":"Cirkevni_organizace_a_nabozenske_spole_nosti_Church_organisation_and_religious_societes",
		"CZ722":"Evidovane_cirkevni_pravnicke_osoby_Registered_church_legal_entity",
		"CZ723":"Svazy_cirkvi_a_nabozenskych_spole_nosti_Unions_of_churches_and_religious_societies",
		"CZ731":"Organiza_ni_jednotka_sdruzeni_Organisational_unit_of_an_association",
		"CZ732":"Organiza_ni_jednotka_politicke_strany_nebo_politickeho_hnuti_Organisational_unit_of_a_political_party_or_political_movement",
		"CZ733":"Organiza_ni_jednotka_odborove_organizace_a_organizace_zam_stnavatel_Organisational_unit_of_a_trade_union_organisation_and_emloyers_organisation",
		"CZ734":"Organiza_ni_jednotka_zvlastni_organizace_pro_zastoupeni_eskych_zajm_v_mezinarodnich_nevladnich_organizacich_Special_organisation_to_represent_Czech_interests_in_international_non_governmental_organisations",
		"CZ736":"Pobo_ny_spolek_Subsidiary_society",
		"CZ741":"Stavovska_organizace_profesni_komora_Professional_chamber",
		"CZ745":"Komora_s_vyjimkou_profesnich_komor_Chamber_excluding_professional_chambers",
		"CZ751":"Zajmove_sdruzeni_pravnickych_osob_Special_interest_club_of_legal_entities",
		"CZ761":"Honebni_spole_enstvo_Hunting_society",
		"CZ771":"Svazek_obci_Union_of_municipalities",
		"CZ801":"Obec_nebo_m_stska_ast_hlavniho_m_sta_Prahy_Municipality_or_city_district_of_Prague",
		"CZ804":"Kraj_a_hlavni_m_sto_Praha_Region_or_capital_city_Prague",
		"CZ805":"Regionalni_rada_regionu_soudrznosti_Regional_Council_of_a_cohesion_region",
		"CZ901":"Zastupitelsky_organ_jinych_stat_Representative_office_of_another_state",
		"CZ906":"Zahrani_ni_spolek_Foreign_society",
		"CZ907":"Mezinarodni_odborova_organizace_International_trade_union_organisation",
		"CZ908":"Mezinarodni_organizace_zam_stnavatel_International_organisation_of_employers",
		"CZ911":"Zahrani_ni_kulturni_informa_ni_st_edisko_rozhlasova_tiskova_a_televizni_agentura_Foreign_cultural_or_information_centre_radio_press_or_television_agency",
		"CZ921":"Mezinarodni_nevladni_organizace_International_non_governmental_organisation",
		"CZ922":"Organiza_ni_jednotka_mezinarodni_nevladni_organizace_Organisational_unit_of_the_international_non_governmental_organisation",
		"CZ936":"Zahrani_ni_pobo_ny_spolek_Foreign_subsidiary_society",
		"CZ937":"Pobo_na_mezinarodni_odborova_organizace_Subsidiary_international_trade_union_organisation",
		"CZ938":"Pobo_na_mezinarodni_organizace_zam_stnavatel_Subsidiary_international_organisation_of_employers",
		"CZ950":"Subjekt_pravnim_adem_vyslovn_neupraveny_Entity_not_explicitly_defined_by_law",
		"CZ960":"Pravnicka_osoba_z_izena_zvlastnim_zakonem_zapisovana_do_ve_ejneho_rejst_iku_Legal_entity_of_an_public_register_established_by_the_special_law",
		"CZ961":"Sv_ensky_fond_Trust_fund",
		"CZ962":"Zahrani_ni_sv_ensky_fond_Foreign_trust_fund",
		"DE101":"GbR_Gesellschaft_burgerlichen_Rechts_BGB_Gesellschaft_Partnership_under_civil_law",
		"DE102":"OHG_Offene_Handelsgesellschaft_General_partnership",
		"DE103":"KG_Kommanditgesellschaft_Limited_partnership_x2",
		"DE104":"eK_Eingetragener_Kaufmann_Eingetragene_Kauffrau_Sole_proprietorship",
		"DE105":"PartG_Partnerschaftsgesellschaft_Registered_partnership_company",
		"DE108":"_Co_KG_Kommanditgesellschaft_mit_haftungsbeschranktem_Komplementar_Limited_partnership_fully_limited",
		"DE109":"_Co_KGaA_Kommanditgesellschaft_auf_Aktien_mit_haftungsbeschranktem_Komplementar_Partnership_limited_by_shares_fully_lmited",
		"DE110":"_Co_OHG_Offene_Handelsgesellschaft_mit_haftungsbeschranktem_Gesellschafter_General_partnership_partially_limited",
		"DE201":"AG_Aktiengesellschaft_Public_limited_company",
		"DE202":"KGaA_Kommanditgesellschaft_auf_Aktien_Partnership_limited_by_shares",
		"DE206":"GmbH_Gesellschaft_mit_beschrankter_Haftung_Private_limited_company",
		"DE207":"UG_haftungsbeschrankt_Unternehmergesellschaft_haftungsbeschrankt_Entrepreneurial_company_limited_liability",
		"DE210":"OPP_Offentlich_private_Partnerschaft_Public_private_Partnership",
		"DE301":"eG_Eingetragene_Genossenschaft_Registered_cooperative_company",
		"DE401":"VVaG_Versicherungsverein_auf_Gegenseitigkeit_Mutual_insurance_company",
		"DE501":"G_Gebietskorperschaft_Regional_Authority",
		"DE502":"AoR_Anstalt_des_offentlichen_Rechts_Institution_established_under_public_law",
		"DE503":"KoR_Korperschaft_des_offentlichen_Rechts_Public_body_statutory_company",
		"DE504":"SoR_Stiftung_des_offentlichen_Rechts_Public_foundation",
		"DE505":"BeG_Betriebe_der_Gebietskorperschaften_Municipal_undertaking",
		"DE507":"ZweckV_Zweckverband_Special_purpose_association",
		"DE601":"SpR_Stiftung_des_privaten_Rechts_Private_foundation",
		"DE602":"e_V_Eingetragener_Verein_Registered_association",
		"DE605":"SnP_Sonstige_nichtrechtsfahige_Personenvereinigung_Other_association_of_individuals_without_legal_capacity",
		"DE606":"P_Privatperson_Private_individual",
		"DE701":"Sonstige_Rechtsformen_Other_legal_form",
		"DK100":"Erhvervsdrivende_fond_Commercial_foundation",
		"DK110":"Forening_Association",
		"DK115":"Frivillig_forening_Voluntary_association",
		"DK130":"Andelsselskab_forening_Cooperative_society",
		"DK140":"a_m_b_a_Andelsselskab_forening_begr_ansvar_Limited_liability_cooperative_society",
		"DK150":"Forening_eller_selskab_med_begr_ansvar_Limited_liability_association",
		"DK151":"s_m_b_a_Selskab_med_begraenset_ansvar_Limited_liability_company",
		"DK152":"f_m_b_a_Forening_med_begraenset_ansvar_Limited_liability_association",
		"DK20":"Dodsbo_Estate_of_deceased_person",
		"DK230":"Statslig_administrativ_enhed_Entitiy_of_central_government",
		"DK235":"Selvstaendig_offentlig_virksomhed_Independent_public_company",
		"DK240":"Amtskommune_County",
		"DK245":"Region",
		"DK250":"Primaerkommune_Municipality",
		"DK260":"Folkekirkelige_Institutioner_Establishmentarian_church_institution",
		"DK280":"Ovrige_virksomhedsformer_Other_legal_form",
		"DK285":"Saerlig_Finansiel_virksomhed_Special_financial_company",
		"DK30":"I_S_Interessentskab_General_partnership",
		"DK40":"K_S_Kommanditselskab_Limited_partnership",
		"DK45":"Medarbejderinvesteringsselskab_Employee_investment_company",
		"DK50":"Partrederi_Shipping_partnership",
		"DK60":"A_S_Aktieselskab_Limited_company",
		"DK70":"Kommanditaktieselskab_Partnerselskab_Limited_partnership",
		"DK80":"ApS_Anpartselskab_Private_limited_company",
		"DK81":"IVS_Ivaerksaetterselskab_Entrepreneurial_limited_company",
		"DK90":"Fonde_og_andre_selvejende_institutioner_Self_governing_institution_association_foundation_etc",
		"EE101":"AS_Aktsiaselts_Public_limited_company",
		"EE102":"OU_Osauhing_Private_limited_company",
		"EE201":"TU_Taisuhing_General_partnership",
		"EE202":"UU_Usaldusuhing_Limited_partnership",
		"EE203":"MTU_Mittetulundusuhing_Non_profit_association",
		"EE204":"TuU_Tulundusuhistu_Commercial_association",
		"EE205":"SA_Sihtasutus_Foundation",
		"EE206":"RKOA_Riigi_ja_kohaliku_omavalitsuse_asutused_Central_and_local_government_authorities",
		"EE207":"KU_Korteriuhistu_Apartment_association",
		"ESC04":"SA_Sociedad_Anonima_Public_limited_company",
		"ESC05":"SAU_Sociedad_Anonima_Unipersonal_Single_member_public_limited_company",
		"ESC06":"SAL_SA_LABORAL_Sociedad_Anonima_Laboral_Worker_owned_public_limited_company",
		"ESC07":"SL_SRL_Sociedad_de_responsabilidad_limitada_Private_limited_company",
		"ESC08":"SLU_SRLU_Sociedad_Limitada_Unipersonal_Single_member_private_limited_company",
		"ESC09":"SLL_SL_LABORAL_Sociedad_Limitada_Laboral_Worker_owned_private_limited_company",
		"ESC10":"SLNE_Sociedad_Limitada_Nueva_Empresa_New_firm_private_limited_company",
		"ESC11":"SC_SRC_Sociedad_colectiva_General_partnerships",
		"ESC12":"S_EN_C_o_S_COM_Sociedad_Comanditaria_Simple_Simple_limited_partnership",
		"ESC13":"S_COM_P_A_Sociedad_Comanditaria_por_acciones_Limited_stock_partnership",
		"ESC14":"S_COOP_Sociedad_Cooperativa_Cooperative_company",
		"ESC16":"SGR_Sociedad_de_garantia_reciproca_Mutual_Guarantee_Company",
		"ESC17":"SAT_Sociedad_agraria_de_transformacion_Farming_partnerships",
		"ESC19":"Sociedad_Civil_con_personalidad_juridica_Non_commercial_partnership_with_independent_legal_status",
		"ESC20":"Mutua_Mutual_company",
		"ESC21":"AIE_Agrupacion_de_Interes_economico_Economic_interest_grouping",
		"ESC25":"Otras_formas_juridicas_Other_legal_forms",
		"ESC30":"SP_Sociedad_profesional_Private_company_of_professional_members",
		"ESC31":"Fundacion_Foundation",
		"ESC32":"Asociaciones_y_otras_instituciones_sin_fines_de_lucro_a_servicio_de_los_hogares_Associations_and_other_non_profit_institutions_serving_households",
		"ESC33":"Entidad_de_derecho_publico_Public_law_entity",
		"ESC34":"Fondo_de_inversion_sin_personalidad_juridica_Investment_funds_without_independent_legal_status",
		"EU100":"SE_Societas_Europea_European_company_a_type_of_public_limited_liability_company_regulated_under_EU_law",
		"EU200":"SCE_Societas_Cooperativa_Europea_European_cooperative_society",
		"EU300":"EEIG_European_Economic_Interest_Grouping_European_economic_interest_grouping",
		"EU400":"EGTC_European_Grouping_of_Territorial_cooperation_European_Grouping_of_Territorial_cooperation",
		"FBRANCH":"Conventional_legal_form_for_the_branch_of_a_foreign_entity_Optional_legal_form_is_normally_not_applicable_for_a_forerign_branch",
		"FI10":"Avoin_yhtio_General_partnership",
		"FI11":"ky_kb_Kommandiittiyhtio_Limited_partnership",
		"FI12":"oy_oyj_ab_abp_Osakeyhtio_Limited_company",
		"FI13":"as_oy_Asunto_osakeyhtio_Housing_company",
		"FI14":"Laivanisannistoyhtio_Shipping_company_under_joint_ownership",
		"FI16":"Keskinainen_kiinteisto_Oy_Mutual_joint_stock_property_company",
		"FI17":"Muu_kiinteisto_Oy_ei_keskinainen_Other_joint_stock_property_company_not_mutual",
		"FI19":"Muu_yhtio_Other_enterprise",
		"FI20":"Aatteellinen_yhdistys_Voluntary_association",
		"FI21":"Erityislainsaadantoon_perustuva_yhdistys_Association_based_on_separate_legislation",
		"FI22":"Keskinainen_vahinkovakuutusyhdistys_Mutual_indemnity_insurance_association",
		"FI23":"Metsanhoitoyhdistys_Forestry_society",
		"FI24":"op_Osuuspankki_Cooperative_bank",
		"FI25":"osk_Osuuskunta_Co_operative_society",
		"FI26":"Avustuskassa_Mutual_benefit_society",
		"FI27":"Tyottomyyskassa_Unemployment_fund",
		"FI28":"Muu_taloudellinen_yhdistys_Other_economic_association",
		"FI29":"Muu_yhdistys_Other_association",
		"FI30":"sr_Saatio_saatiolain_mukainen_Foundation_according_to_the_Foundations_Act",
		"FI31":"sp_Saastopankki_Savings_bank",
		"FI32":"Elakesaatio_saadekirjalla_perustettu_Pension_foundation_founded_by_a_charter_of_foundation",
		"FI33":"Tyoelakekassa_Pension_fund",
		"FI35":"Hypoteekkiyhdistys_Mortgage_society",
		"FI39":"Muu_saatio_Other_foundation",
		"FI40":"Valtio_ja_sen_laitokset_State_and_its_agencies",
		"FI41":"Kunta_Municipality",
		"FI42":"Kuntayhtyma_Joint_municipal_board",
		"FI43":"Ahvenanmaan_maakunta_ja_sen_virastot_Region_of_Aland_and_its_agencies",
		"FI44":"Evankelis_luterilainen_kirkko_Evangelical_Lutheran_Church",
		"FI45":"Ortodoksinen_kirkko_Greek_Orthodox_Church",
		"FI46":"Rekisteroity_uskonnollinen_yhdyskunta_Registered_religious_community",
		"FI47":"Ylioppilaskunta_tai_osakunta_Students_union_or_association",
		"FI48":"Erillishallinnollinen_valtion_laitos_Governmental_institution_with_separate_administration",
		"FI49":"Muu_julkisoikeudellinen_oikeushenkilo_Other_legal_person_subject_to_public_law",
		"FI50":"Yhteisetuudet_esim_kalastuskunta_Mutual_interest_bodies_e_g_fishery_collectives",
		"FI51":"Verotusyhtyma_Corporation_subject_to_taxation",
		"FI52":"Yhteisvastuullinen_pidatysvelvollinen_Body_jointly_and_severally_liable_for_tax_withholding",
		"FI54":"Konkurssipesa_Bankrupt_s_estate",
		"FI55":"Yhteismetsa_Jointly_owned_forest",
		"FI57":"Elinkeinoyhtyma_Trade_association",
		"FI59":"Muu_verotuksen_yksikko_Other_units_subject_to_taxation",
		"FI60":"Valtion_liikelaitos_State_owned_company",
		"FI61":"Kunnallinen_liikelaitos_Municipally_owned_company",
		"FI62":"Kuntainliiton_kuntayhtyman_liikelaitos_Joint_local_authority_company",
		"FI63":"Ahvenanmaan_liikelaitos_Company_owned_by_the_Regional_Government_of_Aland",
		"FI99":"Muut_esim_tilapainen_oikeudellinen_muoto_Others_e_g_temporary_legal_form",
		"FR0000":"Organisme_de_placement_collectif_en_valeurs_mobilieres_sans_personnalite_morale",
		"FR001":"SARL_SARL_Societe_a_responsabilite_limitee_Limited_Liability_UK",
		"FR002":"SA_Societe_anonyme_Public_Limited_Company_Plc_UK",
		"FR003":"SCA_Societe_en_commandite_par_actions_Publicly_traded_partnership",
		"FR004":"SICAV_Societe_d_investissement_a_capital_variable_Investment_company_with_variable_capital_icvc_open_ended_investment_company_oeic_UK",
		"FR005":"Societe_d_investissement_a_capital_fixe_Investment_trust_UK",
		"FR006":"EURL_Entreprise_unipersonnelle_a_responsabilite_limitee_Single_shareholder_limited_company_sme_pvt_UK",
		"FR007":"SCOP_Societe_cooperative_de_production_Cooperative_corporation",
		"FR008":"SEM_Societe_d_economie_mixte_Government_owned_corporation",
		"FR009":"SAS_Societe_par_actions_simplifiee_Unlisted_public_company",
		"FR010":"Micro_entreprise_Special_framework_for_minute_businesses_a_recent_addition_to_french_business_law_with_both_revenue_and_pre_tax_net_income_caps_of_which_auto_entrepreneur_below_is_a_special_case",
		"FR011":"Auto_entrepreneur_Self_employed_UK",
		"FR0110":"FCP_Fonds_commun_de_placement_denues_de_personnalite_morale",
		"FR012":"Profession_liberale_Sole_proprietorship",
		"FR0120":"OT_Organismes_de_titrisation_denues_de_personnalite_morale",
		"FR013":"Societes_d_exercice_liberal_The_incorporated_equivalent_of_the_latter_sole_shareholder_limited_liability_being_key",
		"FR014":"EI_Entreprise_individuelle_entreprise_en_nom_personnel_please_add_english_description",
		"FR015":"EURL_SASU_U_unipersonnelle_Limited_liability_sole_shareholder_ltd_company_UK",
		"FR016":"FCP_Fond_commun_de_placement_Unincorporated_investment_fund",
		"FR017":"GIE_Groupement_d_interet_economique_Economic_interest_grouping",
		"FR018":"Association_Nonprofit_association",
		"FR019":"Association_non_declaree_Unincorporated_association_UK",
		"FR020":"Association_declaree_Incorporated_association",
		"FR021":"SEP_Societe_en_participation_Equity_partnership",
		"FR022":"SNC_Societe_en_nom_collectif_General_partnership",
		"FR024":"Association_cooperative_de_droit_local_0",
		"FR025":"Etablissement_de_credit_sans_but_lucratif_a_conseil_d_administration_outre_mer_0",
		"FR026":"Etablissement_de_credit_sans_but_lucratif_a_conseil_d_orientation_et_de_surveillance_Loi_du_1er_juillet_1983_0",
		"FR027":"Etablissement_de_credit_sans_but_lucratif_a_conseil_d_orientation_et_de_surveillance_Outre_mer_0",
		"FR028":"Etablissement_de_credit_sans_but_lucratif_conseil_d_orientation_et_de_surveillance_et_directoire_Loi_du_1er_juillet_1983_0",
		"FR029":"Etablissement_public_communal_a_caractere_industriel_ou_commercial_0",
		"FR030":"Etablissement_public_communal_administratif_0",
		"FR031":"Etablissement_public_communal_de_credit_et_d_aide_sociale_0",
		"FR032":"Etablissement_public_industriel_et_commercial_0",
		"FR033":"Etablissement_public_national_a_caractere_industriel_ou_commercial_0",
		"FR034":"Etablissement_public_national_administratif_0",
		"FR035":"Etablissement_public_national_administratif_a_conseil_de_surveillance_0",
		"FR036":"Societe_anonyme_a_capital_variable_0",
		"FR037":"Societe_anonyme_cooperative_a_capital_fixe_0",
		"FR038":"Societe_anonyme_cooperative_a_capital_variable_a_conseil_d_administration_0",
		"FR039":"Societe_anonyme_cooperative_a_capital_variable_a_directoire_et_a_conseil_de_surveillance_0",
		"FR040":"Societe_anonyme_cooperative_de_banque_a_conseil_d_administration_0",
		"FR041":"Societe_anonyme_cooperative_de_banque_a_directoire_et_a_conseil_de_surveillance_0",
		"FR042":"Forme_mutuelle_avec_intermediaires_0",
		"FR043":"Forme_mutuelle_sans_intermediaires_0",
		"FR044":"Mutuelle_locale_et_professionnelle_0",
		"FR045":"Mutuelle_agricole_0",
		"FR046":"Tontine_0",
		"FR047":"Societe_anonyme_cooperative_de_banque_populaire_a_capital_fixe_Art_L512_2_3_et_4_0",
		"FR048":"Pools_controles_0",
		"FR049":"Institution_de_prevoyance_0",
		"FR050":"Origine_CCMIP_mutuelles_0",
		"FR051":"Societe_anonyme_cooperative_de_banque_populaire_a_capital_variable_Art_L512_2_et_suivants_0",
		"FR052":"Societe_anonyme_cooperative_de_caution_mutuelle_a_capital_variable_Art_L515_4_a_L515_12_0",
		"FR053":"Societe_anonyme_d_economie_mixte_0",
		"FR054":"Societe_civile_0",
		"FR055":"Societe_cooperative_a_capital_variable_Art_L512_20_a_L512_54_0",
		"FR056":"Societe_cooperative_a_capital_variable_Art_L512_68_a_L512_84_0",
		"FR057":"Societe_cooperative_de_banque_populaire_a_capital_fixe_Art_L512_2_3_et_4_0",
		"FR058":"Societe_cooperative_de_banque_populaire_a_capital_variable_Art_L512_2_3_et_4_0",
		"FR059":"Societe_cooperative_de_caution_mutuelle_a_capital_variable_Art_L515_4_a_L515_12_0",
		"FR060":"Societe_cooperative_conseil_d_orientation_et_de_surveillance_et_directoire_Art_L512_85_a_104_a_capital_fixe_0",
		"FR061":"Societe_professionnelle_Loi_du_17_novembre_1943_0",
		"FR062":"Union_de_societes_cooperatives_a_capital_variable_0",
		"FR063":"Union_de_societes_cooperatives_a_capital_variable_Art_L512_20_a_L512_54_0",
		"FR064":"Societe_en_commandite_simple_0",
		"FR065":"Societe_cooperative_a_capital_fixe_0",
		"FR066":"Societe_cooperative_a_capital_variable_0",
		"FR1100":"Artisan_commercant",
		"FR1200":"Commercant",
		"FR1300":"Artisan",
		"FR1400":"Officier_public_ou_ministeriel",
		"FR1500":"Profession_liberale",
		"FR1600":"Exploitant_agricole",
		"FR1700":"Agent_commercial",
		"FR1800":"Associe_gerant_de_Societe",
		"FR2110":"Indivision_entre_personnes_physiques",
		"FR2120":"Indivision_avec_personne_morale",
		"FR2210":"Societe_creee_de_fait_entre_personnes_physiques",
		"FR2220":"Societe_creee_de_fait_avec_personne_morale",
		"FR2310":"Societe_en_participation_entre_personnes_physiques",
		"FR2320":"Societe_en_participation_avec_personne_morale",
		"FR2385":"Societe_en_participation_de_professions_liberales",
		"FR2400":"Fiducie",
		"FR2700":"Paroisse_hors_zone_concordataire",
		"FR2900":"Autre_groupement_de_droit_prive_non_dote_de_la_personnalite_morale",
		"FR3110":"Representation_ou_agence_commerciale_d_etat_ou_organisme_public_etranger_immatricule_au_RCS",
		"FR3120":"Societe_commerciale_etrangere_immatriculee_au_RCS",
		"FR3205":"Organisation_internationale",
		"FR3210":"Etat_collectivite_ou_etablissement_public_etranger_State_community_or_Foreign_public_institution",
		"FR3220":"Societe_etrangere_non_immatriculee_au_RCS",
		"FR3290":"Autre_personne_morale_de_droit_etranger",
		"FR4110":"Etablissement_public_national_a_caractere_industriel_ou_commercial_dote_d_un_comptable_public",
		"FR4120":"Etablissement_public_national_a_caractere_industriel_ou_commercial_non_dote_d_un_comptable_public",
		"FR4130":"Exploitant_public",
		"FR4140":"Etablissement_public_local_a_caractere_industriel_ou_commercial",
		"FR4150":"Regie_d_une_collectivite_locale_a_caractere_industriel_ou_commercial",
		"FR4160":"Institution_Banque_de_France",
		"FR5191":"Societe_de_caution_mutuelle",
		"FR5192":"Societe_cooperative_de_banque_populaire",
		"FR5193":"Caisse_de_credit_maritime_mutuel",
		"FR5194":"Caisse_federale_de_credit_mutuel",
		"FR5195":"Association_cooperative_inscrite_droit_local_Alsace_Moselle",
		"FR5196":"Caisse_d_epargne_et_de_prevoyance_a_forme_cooperative",
		"FR5202":"Societe_en_nom_collectif",
		"FR5203":"Societe_en_nom_collectif_cooperative",
		"FR5306":"Societe_en_commandite_simple",
		"FR5307":"Societe_en_commandite_simple_cooperative",
		"FR5308":"Societe_en_commandite_par_actions",
		"FR5309":"Societe_en_commandite_par_actions_cooperative",
		"FR5310":"SLP_Societe_de_libre_partenariat",
		"FR5370":"SPFPL_SCA_Societe_de_Participations_Financieres_de_Profession_Liberale_Societe_en_commandite_par_actions",
		"FR5385":"Societe_d_exercice_liberal_en_commandite_par_actions",
		"FR5410":"SARL_nationale",
		"FR5415":"SARL_d_economie_mixte",
		"FR5422":"SARL_immobiliere_pour_le_commerce_et_l_industrie_SICOMI",
		"FR5426":"SARL_immobiliere_de_gestion",
		"FR5430":"SARL_d_amenagement_foncier_et_d_equipement_rural_SAFER",
		"FR5431":"SARL_mixte_d_interet_agricole_SMIA",
		"FR5432":"SARL_d_interet_collectif_agricole_SICA",
		"FR5442":"SARL_d_attribution",
		"FR5443":"SARL_cooperative_de_construction",
		"FR5451":"SARL_cooperative_de_consommation",
		"FR5453":"SARL_cooperative_artisanale",
		"FR5454":"SARL_cooperative_d_interet_maritime",
		"FR5455":"SARL_cooperative_de_transport",
		"FR5458":"SARL_cooperative_ouvriere_de_production_SCOP",
		"FR5459":"SARL_union_de_societes_cooperatives",
		"FR5460":"Autre_SARL_cooperative",
		"FR5470":"SPFPL_SARL_Societe_de_Participations_Financieres_de_Profession_Liberale_Societe_a_responsabilite_limitee",
		"FR5485":"Societe_d_exercice_liberal_a_responsabilite_limitee",
		"FR5499":"Societe_a_responsabilite_limitee_sans_autre_indication",
		"FR5505":"SA_a_participation_ouvriere_a_conseil_d_administration",
		"FR5510":"SA_nationale_a_conseil_d_administration",
		"FR5515":"SA_d_economie_mixte_a_conseil_d_administration",
		"FR5520":"Societe_d_investissement_a_capital_variable_SICAV_a_conseil_d_administration",
		"FR5522":"SA_immobiliere_pour_le_commerce_et_l_industrie_SICOMI_a_conseil_d_administration",
		"FR5525":"SA_immobiliere_d_investissement_a_conseil_d_administration",
		"FR5530":"SA_d_amenagement_foncier_et_d_equipement_rural_SAFER_a_conseil_d_administration",
		"FR5531":"Societe_anonyme_mixte_d_interet_agricole_SMIA_a_conseil_d_administration",
		"FR5532":"SA_d_interet_collectif_agricole_SICA_a_conseil_d_administration",
		"FR5542":"SA_d_attribution_a_conseil_d_administration",
		"FR5543":"SA_cooperative_de_construction_a_conseil_d_administration",
		"FR5546":"SA_de_HLM_a_conseil_d_administration",
		"FR5547":"SA_cooperative_de_production_de_HLM_a_conseil_d_administration",
		"FR5548":"SA_de_credit_immobilier_a_conseil_d_administration",
		"FR5551":"SA_cooperative_de_consommation_a_conseil_d_administration",
		"FR5552":"SA_cooperative_de_commercants_detaillants_a_conseil_d_administration",
		"FR5553":"SA_cooperative_artisanale_a_conseil_d_administration",
		"FR5554":"SA_cooperative_d_interet_maritime_a_conseil_d_administration",
		"FR5555":"SA_cooperative_de_transport_a_conseil_d_administration",
		"FR5558":"SA_cooperative_ouvriere_de_production_SCOP_a_conseil_d_administration",
		"FR5559":"SA_union_de_societes_cooperatives_a_conseil_d_administration",
		"FR5560":"Autre_SA_cooperative_a_conseil_d_administration",
		"FR5570":"Societe_de_Participations_Financieres_de_Profession_Liberale_Societe_anonyme_a_conseil_d_administration_SPFPL_SA_a_conseil_d_administration",
		"FR5585":"Societe_d_exercice_liberal_a_forme_anonyme_a_conseil_d_administration",
		"FR5599":"SA_a_conseil_d_administration_s_a_i",
		"FR5605":"SA_a_participation_ouvriere_a_directoire",
		"FR5610":"SA_nationale_a_directoire",
		"FR5615":"SA_d_economie_mixte_a_directoire",
		"FR5620":"Societe_d_investissement_a_capital_variable_SICAV_a_directoire",
		"FR5622":"SA_immobiliere_pour_le_commerce_et_l_industrie_SICOMI_a_directoire",
		"FR5625":"SA_immobiliere_d_investissement_a_directoire",
		"FR5630":"Safer_anonyme_a_directoire",
		"FR5631":"SA_mixte_d_interet_agricole_SMIA",
		"FR5632":"SA_d_interet_collectif_agricole_SICA",
		"FR5642":"SA_d_attribution_a_directoire",
		"FR5643":"SA_cooperative_de_construction_a_directoire",
		"FR5646":"SA_de_HLM_a_directoire",
		"FR5647":"Societe_cooperative_de_production_de_HLM_anonyme_a_directoire",
		"FR5648":"SA_de_credit_immobilier_a_directoire",
		"FR5651":"SA_cooperative_de_consommation_a_directoire",
		"FR5652":"SA_cooperative_de_commercants_detaillants_a_directoire",
		"FR5653":"SA_cooperative_artisanale_a_directoire",
		"FR5654":"SA_cooperative_d_interet_maritime_a_directoire",
		"FR5655":"SA_cooperative_de_transport_a_directoire",
		"FR5658":"SA_cooperative_ouvriere_de_production_SCOP_a_directoire",
		"FR5659":"SA_union_de_societes_cooperatives_a_directoire",
		"FR5660":"Autre_SA_cooperative_a_directoire",
		"FR5670":"Societe_de_Participations_Financieres_de_Profession_Liberale_Societe_anonyme_a_Directoire_SPFPL_SA_a_directoire",
		"FR5685":"Societe_d_exercice_liberal_a_forme_anonyme_a_directoire",
		"FR5699":"SA_a_directoire_s_a_i",
		"FR5710":"SAS_societe_par_actions_simplifiee",
		"FR5770":"SPFPL_SAS_Societe_de_Participations_Financieres_de_Profession_Liberale_Societe_par_actions_simplifiee",
		"FR5785":"Societe_d_exercice_liberal_par_action_simplifiee",
		"FR6100":"Caisse_d_Epargne_et_de_Prevoyance",
		"FR6220":"GIE_Groupement_d_interet_economique",
		"FR6316":"CUMA_Cooperative_d_utilisation_de_materiel_agricole_en_commun",
		"FR6317":"Societe_cooperative_agricole",
		"FR6318":"Union_de_societes_cooperatives_agricoles",
		"FR6411":"Societe_d_assurance_a_forme_mutuelle",
		"FR6511":"Societes_Interprofessionnelles_de_Soins_Ambulatoires",
		"FR6521":"SCPI_Societe_civile_de_placement_collectif_immobilier",
		"FR6532":"Societe_civile_d_interet_collectif_agricole_SICA",
		"FR6533":"GAEC_Groupement_agricole_d_exploitation_en_commun",
		"FR6534":"Groupement_foncier_agricole",
		"FR6535":"Groupement_agricole_foncier",
		"FR6536":"Groupement_forestier",
		"FR6537":"Groupement_pastoral",
		"FR6538":"Groupement_foncier_et_rural",
		"FR6539":"Societe_civile_fonciere",
		"FR6540":"Societe_civile_immobiliere",
		"FR6541":"Societe_civile_immobiliere_de_construction_vente",
		"FR6542":"Societe_civile_d_attribution",
		"FR6543":"Societe_civile_cooperative_de_construction",
		"FR6544":"Societe_civile_immobiliere_d_accession_progressive_a_la_propriete",
		"FR6551":"Societe_civile_cooperative_de_consommation",
		"FR6554":"Societe_civile_cooperative_d_interet_maritime",
		"FR6558":"Societe_civile_cooperative_entre_medecins",
		"FR6560":"Autre_societe_civile_cooperative",
		"FR6561":"SCP_d_avocats",
		"FR6562":"SCP_d_avocats_aux_conseils",
		"FR6563":"SCP_d_avoues_d_appel",
		"FR6564":"SCP_d_huissiers",
		"FR6565":"SCP_de_notaires",
		"FR6566":"SCP_de_commissaires_priseurs",
		"FR6567":"SCP_de_greffiers_de_tribunal_de_commerce",
		"FR6568":"SCP_de_conseils_juridiques",
		"FR6569":"SCP_de_commissaires_aux_comptes",
		"FR6571":"SCP_de_medecins",
		"FR6572":"SCP_de_dentistes",
		"FR6573":"SCP_d_infirmiers",
		"FR6574":"SCP_de_masseurs_kinesitherapeutes",
		"FR6575":"SCP_de_directeurs_de_laboratoire_d_analyse_medicale",
		"FR6576":"SCP_de_veterinaires",
		"FR6577":"SCP_de_geometres_experts",
		"FR6578":"SCP_d_architectes",
		"FR6585":"Autre_societe_civile_professionnelle",
		"FR6589":"Societe_civile_de_moyens",
		"FR6595":"Caisse_locale_de_credit_mutuel",
		"FR6596":"Caisse_de_credit_agricole_mutuel",
		"FR6597":"Societe_civile_d_exploitation_agricole",
		"FR6598":"Exploitation_agricole_a_responsabilite_limitee",
		"FR6599":"Autre_societe_civile",
		"FR6901":"Autre_personne_de_droit_prive_inscrite_au_registre_du_commerce_et_des_societes",
		"FR7111":"Autorite_constitutionnelle",
		"FR7112":"Autorite_administrative_independante",
		"FR7113":"Ministere",
		"FR7120":"Service_central_d_un_ministere",
		"FR7150":"Service_du_ministere_de_la_Defense",
		"FR7160":"Service_deconcentre_a_competence_nationale_d_un_ministere_hors_Defense",
		"FR7171":"Service_deconcentre_de_l_Etat_a_competence_inter_regionale",
		"FR7172":"Service_deconcentre_de_l_Etat_a_competence_inter_departementale",
		"FR7179":"_Autre_Service_deconcentre_de_l_Etat_a_competence_territoriale",
		"FR7190":"Ecole_nationale_non_dotee_de_la_personnalite_morale",
		"FR7210":"Commune_et_commune_nouvelle",
		"FR7220":"Departement",
		"FR7225":"Collectivite_et_territoire_d_Outre_Mer",
		"FR7229":"_Autre_Collectivite_territoriale",
		"FR7230":"Region_x2",
		"FR7312":"Commune_associee_et_commune_deleguee",
		"FR7313":"Section_de_commune",
		"FR7314":"Ensemble_urbain",
		"FR7321":"Association_syndicale_autorisee",
		"FR7322":"Association_fonciere_urbaine",
		"FR7323":"Association_fonciere_de_remembrement",
		"FR7331":"Etablissement_public_local_d_enseignement",
		"FR7340":"Pole_metropolitain",
		"FR7341":"Secteur_de_commune",
		"FR7342":"District_urbain",
		"FR7343":"Communaute_urbaine",
		"FR7344":"Metropole",
		"FR7345":"SIVOM_Syndicat_intercommunal_a_vocation_multiple",
		"FR7346":"Communaute_de_communes",
		"FR7347":"Communaute_de_villes",
		"FR7348":"Communaute_d_agglomeration",
		"FR7349":"Autre_etablissement_public_local_de_cooperation_non_specialise_ou_entente",
		"FR7351":"Institution_interdepartementale_ou_entente",
		"FR7352":"Institution_interregionale_ou_entente",
		"FR7353":"SIVU_Syndicat_intercommunal_a_vocation_unique",
		"FR7354":"Syndicat_mixte_ferme",
		"FR7355":"Syndicat_mixte_ouvert",
		"FR7356":"Commission_syndicale_pour_la_gestion_des_biens_indivis_des_communes",
		"FR7357":"PETR_Pole_d_equilibre_territorial_et_rural",
		"FR7361":"Centre_communal_d_action_sociale",
		"FR7362":"Caisse_des_ecoles",
		"FR7363":"Caisse_de_credit_municipal",
		"FR7364":"Etablissement_d_hospitalisation",
		"FR7365":"Syndicat_inter_hospitalier",
		"FR7366":"Etablissement_public_local_social_et_medico_social",
		"FR7367":"CIAS_Centre_Intercommunal_d_action_sociale",
		"FR7371":"OPHLM_Office_public_d_habitation_a_loyer_modere",
		"FR7372":"SDIS_Service_departemental_d_incendie_et_de_secours",
		"FR7373":"Etablissement_public_local_culturel",
		"FR7378":"Regie_d_une_collectivite_locale_a_caractere_administratif",
		"FR7379":"_Autre_Etablissement_public_administratif_local",
		"FR7381":"Organisme_consulaire",
		"FR7382":"Etablissement_public_national_ayant_fonction_d_administration_centrale",
		"FR7383":"Etablissement_public_national_a_caractere_scientifique_culturel_et_professionnel",
		"FR7384":"Autre_etablissement_public_national_d_enseignement",
		"FR7385":"Autre_etablissement_public_national_administratif_a_competence_territoriale_limitee",
		"FR7389":"Etablissement_public_national_a_caractere_administratif",
		"FR7410":"GIP_Groupement_d_interet_public",
		"FR7430":"Etablissement_public_des_cultes_d_Alsace_Lorraine",
		"FR7450":"Etablissement_public_administratif_cercle_et_foyer_dans_les_armees",
		"FR7470":"Groupement_de_cooperation_sanitaire_a_gestion_publique",
		"FR7490":"Autre_personne_morale_de_droit_administratif",
		"FR8110":"Regime_general_de_la_Securite_Sociale",
		"FR8120":"Regime_special_de_Securite_Sociale",
		"FR8130":"Institution_de_retraite_complementaire",
		"FR8140":"Mutualite_sociale_agricole",
		"FR8150":"Regime_maladie_des_non_salaries_non_agricoles",
		"FR8160":"Regime_vieillesse_ne_dependant_pas_du_regime_general_de_la_Securite_Sociale",
		"FR8170":"Regime_d_assurance_chomage",
		"FR8190":"Autre_regime_de_prevoyance_sociale",
		"FR8210":"Mutuelle",
		"FR8250":"Assurance_mutuelle_agricole",
		"FR8290":"Autre_organisme_mutualiste",
		"FR8310":"Comite_central_d_entreprise",
		"FR8311":"Comite_d_etablissement",
		"FR8410":"Syndicat_de_salaries",
		"FR8420":"Syndicat_patronal",
		"FR8450":"Ordre_professionnel_ou_assimile",
		"FR8470":"Centre_technique_industriel_ou_comite_professionnel_du_developpement_economique",
		"FR8490":"Autre_organisme_professionnel",
		"FR8510":"Institution_de_prevoyance",
		"FR8520":"Institution_de_retraite_supplementaire",
		"FR9110":"Syndicat_de_copropriete",
		"FR9150":"Association_syndicale_libre",
		"FR9210":"Association_non_declaree",
		"FR9220":"Association_declaree",
		"FR9221":"Association_declaree_d_insertion_par_l_economique",
		"FR9222":"Association_intermediaire",
		"FR9223":"Groupement_d_employeurs",
		"FR9224":"Association_d_avocats_a_responsabilite_professionnelle_individuelle",
		"FR9230":"Association_declaree_reconnue_d_utilite_publique",
		"FR9240":"Congregation",
		"FR9260":"Association_de_droit_local_Bas_Rhin_Haut_Rhin_et_Moselle",
		"FR9300":"Fondation",
		"FR9900":"Autre_personne_morale_de_droit_prive",
		"FR9970":"Groupement_de_cooperation_sanitaire_a_gestion_privee",
		"GB100":"Corporations",
		"GB200":"Cooperatives",
		"GB300":"Partnerships",
		"GB400":"Sole_traders",
		"GB500":"Limited_liability_company",
		"GB600":"Other_legal_form_Any_other_legal_form_not_included_in_the_list",
		"GR901":"SP_Astiki_Proswpiki_Eteria_Sole_Proprietorship_and_partnerships",
		"GR902":"OE_Omorithmi_Eteria_General_Partnership",
		"GR903":"EE_Eterorithmi_Eteria_Limited_partnership_partnership_company",
		"GR904":"SLP_Afanis_Eteria_Silent_Partnership",
		"GR905":"SA_Anonimi_Eteria_Public_Limited_Company_Societe_Anonyme_Incorporated_Company_Joint_stock_Company",
		"GR906":"EPE_Eteria_Periorismenis_Euthinis_Limited_Liability_Company",
		"GR907":"IKE_Idiotiki_kefaleouhiki_Eteria_Private_Capital_Company",
		"GR908":"JSO_Simplioktisia_Joint_Ship_ownership",
		"GR909":"SC_Naftiki_eteria_Shipping_Company",
		"GR910":"COOP_Sinetairismos_Cooperative_Company_Association",
		"GR911":"CLF_Somatia_Idrimata_Club_Union_Syndicate_Foundation",
		"GR912":"JV_Kinopraxia_Joint_Venture",
		"GR913":"PL_Nomika_Prosopa_Dimosiou_Dikeou_Legal_Entities_of_Public_Law",
		"GR999":"Other_Lipa_Other_Legal_Forms",
		"HR01":"d_d_Dioni_ko_drustvo_Joint_stock_company",
		"HR02":"d_o_o_Drustvo_s_ograni_enom_odgovornos_u_Limited_liability_company",
		"HR03":"j_t_d_Javno_trgova_ko_drustvo_Public_company",
		"HR04":"k_d_Komanditno_drustvo_Limited_partnership",
		"HR05":"Inozemni_osniva_Podruznice_inozemnih_trgova_kih_drustava_Foreign_founder_Non_resident_company_s_branches",
		"HR06":"Ustanova_Institution",
		"HR07":"Nedefinirano_Ostalo_Other_legal_form",
		"HR08":"j_d_o_o_Jednostavno_drustvo_s_ograni_enom_odgovornos_u_Simple_limited_liability_company",
		"HR09":"Druga_osoba_za_koje_je_upis_propisan_zakonom_Other_entities_as_prescribed_by_law",
		"HR10":"Drustvene_organizacije_Public_organisations",
		"HR13":"Fondovi_Funds",
		"HR14":"Fundacije_Foundations",
		"HR15":"Gospodarska_udruzenja_Economic_cooperations",
		"HR16":"GIU_Gospodarsko_interesno_udruzenje_Economic_interest_grouping",
		"HR17":"Grad_Town",
		"HR18":"Gradona_elnik_Mayor",
		"HR19":"Gradsko_poglavarstvo_City_government",
		"HR20":"Gradsko_vije_e_City_council",
		"HR21":"Hrvatska_narodna_banka_Croatian_National_Bank",
		"HR22":"Hrvatski_sabor_Croatian_Parliament",
		"HR23":"Investicijski_i_mirovinski_fondovi_Investment_and_pension_funds",
		"HR25":"Ministarstva_i_ostali_samostalni_organi_drzavne_uprave_Ministries_and_other_independent_bodies_of_government_administration",
		"HR26":"Mirovinski_fondovi_Pension_funds",
		"HR27":"Mjesni_odbor_gradski_kotar_i_gradska_etvrt_Local_committee_town_district_and_town_block",
		"HR28":"Nenov_ani_investicijski_fondovi_Non_money_market_investment_funds",
		"HR29":"Op_ina_Municipality",
		"HR30":"Op_inski_na_elnik_Municipal_prefect",
		"HR31":"Op_insko_poglavarstvo_Municipal_government",
		"HR32":"Op_insko_vije_e_Municipal_council",
		"HR34":"Ostale_organizacije_Other_organisations",
		"HR35":"Ostali_oblici_organiziranja_Other_organisational_forms",
		"HR37":"Politi_ke_stranke_Political_parties",
		"HR38":"Pravosu_e_Justice",
		"HR39":"Predsjednik_Republike_Hrvatske_President_of_the_Republic_of_Croatia",
		"HR40":"Privatno_poduze_e_Private_enterprise",
		"HR42":"Republika_Hrvatska_Republic_of_Croatia",
		"HR44":"Stru_ne_sluzbe_uredi_i_druga_tijela_Administrative_staffs_offices_and_other_bodies",
		"HR45":"s_d_d_Sportsko_dioni_ko_drustvo_Sport_joint_stock_company",
		"HR47":"Udruga_Association",
		"HR48":"Udruge_gra_ana_Civil_cooperatives",
		"HR49":"Udruge_vise_razine_Higher_level_association",
		"HR51":"Ustavni_sud_Republike_Hrvatske_Constitutional_Court_of_the_Republic_of_Croatia",
		"HR52":"Vlada_Republike_Hrvatske_Government_of_the_Republic_of_Croatia",
		"HR53":"Zadruga_Cooperative",
		"HR55":"Zajednica_ustanova_Communities_of_institutions",
		"HR57":"Zaklade_Trusts",
		"HR58":"Zupan_County_prefect",
		"HR59":"Zupanija_County",
		"HR60":"Zupanijska_skupstina_County_Assembly",
		"HR61":"Zupanijsko_poglavarstvo_County_government",
		"HR62":"Nov_ani_investicijski_fondovi_Money_market_investment_funds",
		"HU113":"Kft_Korlatolt_felelossegu_tarsasag_Private_limited_liability_company",
		"HU114":"Rt_Reszvenytarsasag_Limited_company",
		"HU116":"Kozkereseti_tarsasag_General_partnership",
		"HU117":"Beteti_tarsasag_Limited_partnership",
		"HU122":"Takarek_es_hitelszovetkezet_Savings_and_loan_association_savings_and_credit_cooperative",
		"HU129":"Egyeb_szovetkezet_Other_cooperative",
		"HU226":"Kulfoldi_szekhelyu_vallalkozas_fioktelepe_0",
		"HU524":"Kolcsonos_biztosito_egyesulet_Mutual_insurance_association",
		"HU529":"Egyeb_egyesulet_Other_association",
		"HU581":"Onkentes_kolcsonos_biztositopenztar_Voluntary_mutual_insurance_fund",
		"HU582":"Magannyugdijpenztar_Private_pension_fund",
		"HU611":"Kulfoldi_szekhelyu_vallalkozas_kereskedelmi_kepviselete_Commercial_agency_of_a_foreign_enterprise",
		"HU736":"Kozhasznu_tarsasag_Public_benefit_nonprofit_institution",
		"HU915":"Befektetesi_alap_Investment_fund",
		"HU916":"OBA_Orszagos_betetbiztositasi_alap_National_deposit_insurance_fund",
		"HU999":"Egyeb_jogi_forma_Other_legal_form",
		"IE01":"LTD_Private_Company_Limited_by_Shares_LTD_company_0",
		"IE02":"DAC_Designated_Activity_Company_DAC_limited_by_shares_0",
		"IE03":"DAC_Designated_Activity_Company_Limited_by_Guarantee_DAC_limited_by_guarantee_0",
		"IE04":"CLG_Company_Limited_by_Guarantee_CLG_limited_by_guarantee_not_having_a_share_capital_0",
		"IE05":"PLC_Public_Limited_Company_PLC_0",
		"IE06":"SMC_Single_Member_Company_0",
		"IE07":"UC_Unlimited_company_0",
		"IE08":"UCITS_Undertakings_for_Collective_Investment_in_Transferable_Securities_UCITS_0",
		"IE11":"Industrial_and_Provident_Society_0",
		"IE12":"Friendly_Society_0",
		"IE13":"Trade_union_0",
		"IE14":"Local_authority_0",
		"IE15":"Statutory_corporation_0",
		"IE16":"Other_legal_form_0",
		"IT101":"PA_PUBBLICA_AMMINISTRAZIONE_General_government",
		"IT201":"SNC_SOCIETA_IN_NOME_COLLETTIVO_General_partnership_commercial",
		"IT301":"SAS_SOCIETA_IN_ACCOMANDITA_SEMPLICE_Limited_partnership",
		"IT401":"SS_SOCIETA_SEMPLICE_General_partnership_non_commercial",
		"IT402":"SDF_SOCIETA_DI_FATTO_De_facto_corporation",
		"IT501":"AIMP_AZIENDA_PROVINCIALE_CONSORZIO_Consortium",
		"IT601":"COOP_SOCIETA_COOPERATIVA_Cooperative_society",
		"IT701":"SPA_SOCIETA_PER_AZIONI_Plc_UK",
		"IT702":"SAA_SOCIETA_IN_ACCOMANDITA_PER_AZIONI_Partnership_limited_by_shares",
		"IT703":"SRL_SOCIETA_A_RESPONSABILITA_LIMITATA_Ltd_UK",
		"IT999":"Altra_specie_giuridica_Other_legal_form",
		"LT101":"AB_Akcin_bendrov_Public_Company",
		"LT102":"UAB_Uzdaroji_akcin_bendrov_Private_Company",
		"LT103":"KO_Kooperatin_bendrov_kooperatyvas_Cooperative_Society_Cooperative",
		"LT104":"TUB_Tikroji_kin_bendrija_General_Partnership",
		"LT105":"KUB_Komanditin_kin_bendrija_Limited_Partnership",
		"LT106":"A_Asociacija_Association",
		"LT107":"MB_Mazoji_bendrija_Small_Partnership",
		"LT108":"ZUB_Zem_s_kio_bendrov_Agricultural_Company",
		"LT109":"II_Individuali_mon_Individual_Enterprise",
		"LT110":"APB_Advokat_profesin_bendrija_Lawyers_Professional_Partnership",
		"LT111":"PDB_Priva_i_detektyv_bendrija_Society_of_Private_Detectives",
		"LT201":"VI_Valstyb_s_mon_State_Enterprise",
		"LT202":"SI_Savivaldyb_s_mon_Municipal_Enterprise",
		"LT203":"VS_Viesoji_staiga_Public_Institution",
		"LT204":"BI_Biudzetin_staiga_Budgetary_Institution",
		"LT205":"LF_Labdaros_ir_paramos_fondas_Charity_and_Sponsorship_Fund",
		"LT206":"BN_Bendrija_Partnership",
		"LT207":"SD_Sodinink_bendrija_Gardeners_Partnership",
		"LT208":"PP_Politin_partija_Political_Party",
		"LT209":"TR_Tradicin_religin_bendruomen_ar_bendrija_Traditional_Lithuanian_Religious_Congregation_or_Community",
		"LT210":"RB_Religin_bendruomen_ar_bendrija_Religious_Community_and_Association",
		"LT211":"PS_Profesin_s_junga_ar_susivienijimas_Trade_Union",
		"LT212":"Nuolatin_komercinio_arbitrazo_institucija_Domicile_Arbitration_Institution",
		"LT213":"S_Seimyna_Foster_Family",
		"LT214":"PR_Prekybos_pramon_s_ir_amat_r_mai_Chamber_of_commerce_industry_and_crafts",
		"LT215":"LPRA_Lietuvos_prekybos_pramon_s_ir_amat_r_m_asociacija_The_Association_of_Lithuanian_Chambers_of_Commerce_Industry_and_Crafts",
		"LT216":"CRC_Bendras_valdymo_ir_pranesim_centras_Combined_Control_and_Reporting_Centre",
		"LT301":"CB_Centrinis_bankas_Central_Bank",
		"LU01":"EI_Entreprise_individuelle_Sole_proprietorship",
		"LU02":"SENC_Societe_en_nom_collectif_General_partnership",
		"LU03":"SARL_Societe_a_responsabilite_limitee_Limited_liability_company",
		"LU04":"SARLS_Societe_a_responsabilite_limitee_simplifiee_Simplified_limited_liability_company",
		"LU05":"SECS_Societe_en_commandite_simple_Limited_partnership",
		"LU06":"SECSP_Societe_en_commandite_speciale_Special_limited_partnership",
		"LU07":"SA_Societe_anonyme_Public_limited_company",
		"LU08":"SECA_Societe_en_commandite_par_actions_Partnership_limited_by_shares",
		"LU09":"SICAV_Societe_d_investissement_a_capital_variable_Open_ended_investment_company",
		"LU10":"SICAF_Societe_d_investissement_a_capital_fixe_Closed_ended_investment_company",
		"LU11":"SEPCAV_Societe_d_epargne_pension_a_capital_variable_Variable_Capital_Pension_Savings_Company",
		"LU12":"SCOP_Societe_cooperative_Cooperative_company",
		"LU13":"SC_Societe_civile_Civil_company",
		"LU14":"AM_Association_momentanee_Temporary_partnership",
		"LU15":"GIE_Groupement_d_interet_economique_Economic_interest_group",
		"LU16":"ASBL_Association_sans_but_lucratif_Non_profit_association",
		"LU17":"FON_Fondation_Foundation",
		"LU18":"ASSEP_Association_d_epargne_pension_Pensions_Savings_Association",
		"LU19":"AAM_Association_d_assurances_mutuelles_Mutual_Insurance_Association",
		"LU20":"AA_Association_agricole_Agricultural_association",
		"LU21":"EP_Etablissement_public_Public_establishment",
		"LU22":"SNC_Societe_en_nom_collectif_Partnership",
		"LU23":"SSC_Succursale_de_societe_commerciale_Company_branch",
		"LU24":"SSARLS_Succursale_de_societe_a_responsabilite_limitee_simplifiee_Branch_of_a_simplified_limited_liability_company",
		"LU26":"FCP_Fonds_commun_de_placement_Mutual_Funds",
		"LU27":"FIAR_Fonds_d_investissement_alternatif_reserve_Alternative_investment_funds_reserved",
		"LU32":"AUT_Autres_Formes_juridiques_Other_legal_form",
		"LU33":"SP_Secteur_public_Public_sector",
		"LU34":"SICAR_Societe_d_investissement_a_capital_risque_Risk_capital_investment_company",
		"LV101":"AS_Akciju_sabiedr_ba_Stock_company",
		"LV103":"SIA_Sabiedr_ba_ar_ierobezotu_atbild_bu_Limited_liability_company",
		"LV104":"VU_Valsts_uz_mums_State_enterprise",
		"LV105":"PSV_Pasvald_bas_uz_mums_Municipal_enterprise",
		"LV106":"UZN_Uz_m_jsabiedr_bas_uz_mums_Enterprise_of_the_company",
		"LV107":"PS_Pilnsabiedr_ba_General_partnership",
		"LV108":"KS_Komand_tsabiedr_ba_Limited_partnership",
		"LV109":"LIG_L_gumsabiedr_ba_ar_pilnu_atbild_bu_Partnership_with_full_responsibility",
		"LV110":"PAJ_Paju_sabiedr_ba_Joint_stock_company",
		"LV111":"PAP_Sabiedr_ba_ar_papildu_atbild_bu_Additional_liability_company",
		"LV301":"GIM_imenes_uz_mums_Sole_proprietorship",
		"LV302":"IK_Individu_lais_komersants_Individual_merchant",
		"LV303":"IND_Individu_lais_uz_mums_Sole_proprietorship",
		"LV401":"KB_Kooperat_v_sabiedr_ba_Cooperative_society",
		"LV402":"KBS_Kooperat_vo_biedr_bu_savien_ba_Union_of_cooperative_societies",
		"LV403":"KBU_Kooperat_vo_biedr_bu_uz_mums_Enterprise_of_cooperative_societies",
		"LV404":"KSS_Kooperat_vo_biedr_bu_savien_bas_uz_mums_Enterprise_of_union_of_cooperative_societies",
		"LV405":"ZEM_Zemnieku_saimniec_ba_Farm_farming_enterprise",
		"LV406":"ZVJ_Zvejnieku_saimniec_ba_Farm_fishing_enterprise",
		"LV701":"PPI_Publisk_s_personas_un_iest_des_Public_persons_and_authorities",
		"LV801":"REL_Reli_iskas_organiz_cijas_uz_mums_Enterprise_of_religious_organisation",
		"LV802":"SOU_Sabiedrisk_s_organiz_cijas_uz_mums_Enterprise_of_NGO",
		"LV803":"ARA_Arodbiedr_bu_apvien_ba",
		"LV804":"ARB_Arodbiedr_ba",
		"LV805":"ARV_Arodbiedr_bas_patst_v_g_vien_ba",
		"LV806":"ROROIG_Reli_isk_s_organiz_cijas_un_reli_isko_organiz_ciju_iest_des",
		"LV807":"BDR_Biedr_ba",
		"LV808":"NOD_Nodibin_jums",
		"LV809":"PP_Politisk_partija",
		"LV810":"PPA_Politisko_partiju_apvien_ba",
		"LV901":"AKF_rzemju_komersanta_fili_le_Branch_of_a_foreign_enterprise",
		"LV903":"PAR_P_rst_vniec_ba_Permanent_representative_office",
		"MT010":"Sole_proprietor_Sole_proprietors",
		"MT020":"PCOMM_En_commandite_A_limited_Partnership",
		"MT021":"P_En_nom_collectif_A_general_Partnership",
		"MT030":"LTD_Limited_Private_limited_company",
		"MT031":"OC_Overseas_Company_Overseas_Company",
		"MT033":"SV_SICAV_Societe_d_Investissement_a_Capital_Variable_Investment_companies_with_variable_share_capital",
		"MT040":"Voluntary_Non_for_profit_Organisations",
		"MT050":"General_Government",
		"MT060":"PLC_Public_limited_company_Public_limited_company",
		"MT070":"Corporations_x2",
		"MT080":"Cooperatives_x2",
		"NL101":"BV_Besloten_vennootschap_private_limited_company",
		"NL102":"NV_Naamloze_vennootschap_public_limited_company",
		"NL11":"CVA_Commanditaire_Vennootschap_met_rechtspersoonlijkheid",
		"NL201":"Cooperatie_cooperative",
		"NL202":"OWM_Onderlinge_waarborgmaatschappij_mutual_insurance_association",
		"NL203":"Vereniging_association_society",
		"NL204":"VVE_Vereniging_van_eigenaars_home_owners_association",
		"NL205":"Kerkgenootschap_church_or_spiritual_organisation",
		"NL206":"Stichting_foundation_trust",
		"NL207":"Overige_rechtsvorm_Other_legal_form",
		"NL301":"Eenmanszaak_Sole_proprietorship",
		"NL302":"Maatschap_partnership",
		"NL303":"CV_Commanditaire_vennootschap_limited_partnership",
		"NL304":"VOF_Vennootschap_onder_firma_general_partnership_partnership_firm",
		"NL401":"Publiekrechtelijke_rechtspersonen_op_basis_van_artikel_2_1_lid_1_BW_Legal_entities_governed_by_public_law_under_Section_2_1_1_of_the_Dutch_Civil_Code_legal_entities_under_public_law_as_referred_to_in_Section_2_1_1_of_the_DCC",
		"NL402":"Publiekrechtelijke_rechtspersonen_op_basis_van_artikel_2_1_lid_2_BW_Legal_entities_governed_by_public_law_under_Section_2_1_2_of_the_Dutch_Civil_Code_legal_entities_under_public_law_as_referred_to_in_Section_2_1_2_of_the_DCC",
		"NL501":"Rederij_shipping_company",
		"NL7":"BA_Cooperatie_met_Beperkte_Aansprakelijkheid",
		"NL9":"COV_Cooperatieve_Vereniging",
		"NL901":"Rechtspersoon_in_oprichting_legal_entity_in_formation",
		"NTRL_PRSN":"Natural_person",
		"PLA019":"s_c_spo_ki_cywilne_civil_law_partnership",
		"PLA044":"uczelnie_higher_education_institution",
		"PLA070":"partie_polityczne_political_party",
		"PLA085":"wspolnoty_mieszkaniowe_condominium",
		"PLA099":"osoby_fizyczne_prowadz_ce_dzia_alno_gospodarcz_Sole_proprietorship",
		"PLA115":"sp_p_spo_ki_partnerskie_professional_partnership",
		"PLA116":"S_A_spo_ki_akcyjne_joint_stock_company",
		"PLA117":"sp_z_o_o_spo_ki_z_ograniczon_odpowiedzialno_ci_limited_liability_company",
		"PLA118":"s_j_spo_ki_jawne_registered_partnership",
		"PLA120":"sp_k_spo_ki_komandytowe_limited_partnership",
		"PLA121":"S_K_A_spo_ki_komandytowo_akcyjne_limited_joint_stock_partnership",
		"PLA124":"przedsi_biorstwa_pa_stwowe_state_owned_enterprise_SOE",
		"PLA126":"TUW_towarzystwa_ubezpiecze_wzajemnych_mutual_insurance_society",
		"PLA132":"instytucje_gospodarki_bud_etowej_state_budget_entity",
		"PLA134":"towarzystwa_reasekuracji_wzajemnej_mutual_reinsurance_society",
		"PLA140":"spo_dzielnie_co_operative",
		"PLA146":"samodzielne_publiczne_zak_ady_opieki_zdrowotnej_independent_public_health_care_unit",
		"PLA148":"fundacje_foundation",
		"PLA177":"ko_ka_rolnicze_machinery_ring",
		"PLA180":"spo_dzielcze_kasy_oszcz_dno_ciowo_kredytowe_co_operative_savings_and_credit_union",
		"PLA403":"wspolnoty_samorz_dowe_self_governed_community",
		"PLA409":"Skarb_Pa_stwa_the_State_Treasury",
		"PLA428":"pa_stwowe_jednostki_organizacyjne_state_organizational_unit",
		"PLB050":"ko_cio_y_i_zwi_zki_wyznaniowe_churches_and_religious_unions",
		"PLB055":"stowarzyszenia_i_zwi_zki_stowarzysze_association_or_union_of_associations",
		"PLB060":"organizacje_spo_eczne_i_zawodowe_non_profit_or_professional_organisatoin",
		"PLB133":"zwi_zki_zawodowe_trade_union",
		"PLB137":"zrzeszenia_federation",
		"PLB138":"zwi_zki_inne_ni_zawodowe_union_other_than_a_trade_union",
		"PLB141":"instytuty_badawcze_research_institute",
		"PLB147":"cechy_i_izby_rzemie_lnicze_izby_gospodarcze_guild_and_craft_chamber_chamber_of_commerce",
		"PLB381":"placowki_systemu_o_wiaty_education_system_institution",
		"PLB401":"organy_w_adzy_administracji_rz_dowej_kontroli_pa_stwowej_i_ochrony_prawa_oraz_s_dy_i_trybuna_y_public_authority_body_government_administration_authority_state_inspection_authority",
		"PLB429":"samorz_dowe_jednostki_organizacyjne_self_government_organizational_unit",
		"PLC049":"fundusze_inwestycyjne_investment_fund",
		"PLD049":"OFE_otwarte_fundusze_emerytalne_open_pension_fund",
		"PLE049":"fundusze_inne_ni_inwestycyjne_i_inne_ni_otwarte_fundusze_emerytalne_fund_other_than_investment_fund_or_open_pension_fund",
		"PT111":"ACE_Agrupamento_Complementar_de_Empresas_ACE_Complementary_Grouping_of_Companies",
		"PT121":"Lda_Sociedade_por_Quotas_Private_limited_company",
		"PT122":"SUni_Sociedade_Unipessoal_Por_Quotas_Single_quotaholder_private_limited_company",
		"PT131":"SA_Sociedade_Anonima_Public_limited_company",
		"PT141":"Coman_Sociedades_em_comandita_Limited_partnership",
		"PT151":"SNC_Sociedades_em_nome_coletivo_Partnerships",
		"PT171":"SOCI_Sociedade_Civil_Civil_society",
		"PT181":"Sociedade_Irregular_Unregistered_company",
		"PT182":"EIRL_Estabelecimento_Individual_de_Responsabilidade_Limitada_Individual_business_with_limited_liability",
		"PT211":"Coop_Cooperativa_Cooperative",
		"PT221":"Assoc_Associacao_Association",
		"PT231":"Fund_Fundacao_Foundation",
		"PT311":"EPE_Empresa_Publica_Empresarial_Public_corporation",
		"PT312":"PCDP_Pessoa_Coletiva_de_Direito_Publico_Public_law_institution",
		"PT321":"EPMR_Entidade_Publica_Municipal_Intermunicipal_e_Regional_Municipal_Intermunicipal_and_Regional_public_company",
		"PT331":"OAP_Organismo_da_Administracao_Publica_Public_Institution",
		"PT411":"PCR_Pessoa_Colectiva_Religiosa_Religious_legal_person",
		"PT711":"Fundos_Trusts",
		"PT901":"OI_Organizacoes_Internacionais_Internacional_Organizations",
		"RO101":"SA_Societate_pe_ac_iuni_Joint_Stock_Company",
		"RO102":"SRL_Societate_cu_r_spundere_limitat_Limited_Liability_Company_Ltd",
		"RO103":"SCS_Societate_in_comandit_simpl_Limited_partnership",
		"RO104":"SCA_Societate_in_comandit_pe_ac_iuni_Limited_partnership_with_shares",
		"RO105":"Alte_forme_de_proprietate_Other_legal_forms",
		"RO107":"ONG_Organiza_ie_non_guvernamental_Non_Governmental_Organization_Non_Profit_institution",
		"RO108":"SNC_Societate_in_nume_colectiv_General_partnership",
		"RO110":"RA_Regie_autonom_Public_company",
		"RO111":"GIE_Grupul_de_interes_economic_Economic_interest_grouping",
		"RO114":"Cooperativ_de_consum_Consumer_cooperative",
		"RO115":"Cooperativ_de_credit_Credit_cooperative",
		"RO116":"Cooperativ_me_te_ug_reasc_Handicraft_cooperative",
		"RO117":"Reprezentanta_Representative_Office",
		"RO120":"Sucursala_Branch",
		"RO121":"Reprezentant_fiscal_Fiscal_representative",
		"RO122":"Societate_agricol_Agricultural_company",
		"RW100":"Corporations_x3",
		"RW200":"Cooperatives_x3",
		"RW300":"Partnerships_x2",
		"RW400":"Sole_traders_x2",
		"RW500":"Limited_liability_company_x2",
		"RW600":"Other_legal_form_Any_other_legal_form_not_included_in_the_list_x2",
		"SE21":"Enkelt_bolag_Regulated_partnership_between_two_parts",
		"SE22":"Partrederier_Limited_shipping_partnerships",
		"SE31":"HB_KB_Handelsbolag_kommanditbolag_HB_KB_Limited_partnership",
		"SE41":"AB_Bankaktiebolag_AB_Limited_banking_companies",
		"SE42":"AB_Forsakringsaktiebolag_AB_Limited_insurance_companies",
		"SE49":"AB_Ovriga_aktiebolag_AB_Other_limited_companies",
		"SE51":"Ek_for_Ekonomisk_forening_Ek_for_Economic_association_minimum_three_members",
		"SE53":"BRF_Bostadsrattsforening_BRF_Tenant_owners_associations",
		"SE54":"Kooperativ_hyresrattsforening_Cooperative_renting_rights_associations",
		"SE61":"Ideell_forening_Non_profit_organisation",
		"SE62":"Samfalligheter_Joint_ownership_associations",
		"SE63":"Registrerat_trossamfund_Registered_religious_communities",
		"SE71":"Familjestiftelser_Family_foundations",
		"SE72":"Ovriga_stiftelser_och_fonder_inkl_pensionsstiftelser_och_personalstiftelser_Other_foundations_and_funds",
		"SE81":"Statliga_enheter_Entities_of_central_government",
		"SE82":"Kommuner_Municipalities",
		"SE83":"Kommunalforbund_Federations_of_local_government_authorities",
		"SE84":"Landsting_County_councils",
		"SE87":"Offentliga_korporationer_och_anstalter_Public_corporate_bodies_and_institutions",
		"SE88":"Hypoteksforeningar_Mortgage_associations",
		"SE91":"Oskiftade_dodsbon_Estates_of_deceased_persons",
		"SE92":"Omsesidiga_forsakringsbolag_Mutual_insurance_corporations",
		"SE93":"Spb_Sparbanker_Spb_Savings_banks",
		"SE94":"Understodsforeningar_Forsakringsforeningar_Friendly_societies",
		"SE95":"Arbetsloshetskassor_Unemployment_benefit_funds",
		"SE98":"Ovriga_svenska_juridiska_personer_bildade_enligt_sarskild_lagstiftning_Other_Swedish_legal_persons_subject_to_special_legislation",
		"SI101":"d_n_o_Druzba_z_neomejeno_odgovornostjo_d_n_o_Unlimited_company_UK",
		"SI102":"k_d_Komanditna_druzba_k_d_Limited_partnership_UK",
		"SI103":"d_o_o_Druzba_z_omejeno_odgovornostjo_d_o_o_Ltd_UK",
		"SI104":"d_d_Delniska_druzba_d_d_Plc_UK",
		"SI105":"k_d_d_Komanditna_delniska_druzba_k_d_d_Limited_partnership_with_share_capital",
		"SI108":"GIZ_Gospodarsko_interesno_zdruzenje_GIZ_Economic_Interest_Grouping_EIG",
		"SI112":"z_o_o_Zadruga_z_o_o_Cooperative_z_o_o",
		"SI113":"z_b_o_Zadruga_z_b_o_Cooperative_z_b_o",
		"SI201":"Centralna_banka_Central_Bank",
		"SI210":"Sklad_Trust",
		"SI211":"d_v_z_Druzba_za_vzajemno_zavarovanje_d_v_z_Mutual_insurance_company_d_v_z",
		"SI213":"Javni_sklad_Public_Fund",
		"SI300":"Javna_agencija_Public_Agency",
		"SI301":"Republika_Slovenija_Republic_of_Slovenia",
		"SI302":"Predsednik_republike_President_of_the_Republic",
		"SI303":"Predstavniski_organ_DZ_DS_Representative_body_parliament_National_council",
		"SI304":"Varuh_lovekovih_pravic_Human_rights_ombudsman",
		"SI305":"Ustavno_sodis_e_Constitutional_Court",
		"SI306":"Ra_unsko_sodis_e_The_court_of_Auditors",
		"SI307":"Vlada_vladna_sluzba_Government_government_service",
		"SI308":"Ministrstvo_Ministry",
		"SI309":"Sodis_e_vrhovno_visja_okrozna_okrajna_Court_supreme_higher_district_county",
		"SI310":"Tozilstvo_The_prosecutor_s_office",
		"SI311":"Pravobranilstvo_Attorneys_Office",
		"SI313":"Upravni_organ_v_sestavi_Administrative_body",
		"SI315":"Upravna_enota_Administrative_unit",
		"SI316":"Organ_organizacija_sirse_lokalne_skupnosti_Authority_organization_wider_local_community",
		"SI318":"Lokalne_skupnosti_Local_communities",
		"SI319":"Krajevna_skupnost_druge_ozje_lokalne_skupnosti_The_local_community_other_local_community",
		"SI321":"Pooblas_enec_za_dostop_do_informacij_javnega_zna_aja_The_Commissioner_for_Access_to_Public_Information",
		"SI322":"Samostojni_in_neodvisni_drzavni_organ_Autonomous_and_independent_state_authority",
		"SI352":"Javni_gospodarski_zavod_Public_economic_institute",
		"SI354":"Zavod_Institute",
		"SI355":"Javni_zavod_Public_institute",
		"SI357":"Skupnost_zavodov_Community_of_institutes",
		"SI358":"Zbornica_Chamber",
		"SI359":"_lanica_univerze_University_member",
		"SI360":"Gospodarska_zbornica_Chamber_of_Commerce",
		"SI361":"Javni_raziskovalni_zavod_Public_research_institut",
		"SI362":"Skupnost_lastnikov_stanovanj_Community_of_homeowners",
		"SI401":"Ustanova_Institution_x2",
		"SI402":"Agrarne_pasne_in_vaske_skupnosti_Agriculture_grazing_and_village_communities",
		"SI403":"Druge_skupnosti_Other_communities",
		"SI404":"Mladinski_svet_Youth_Council",
		"SI405":"Narodnostna_skupnost_Ethnic_community",
		"SI406":"Studentska_organizacija_Student_organization",
		"SI407":"Nevladna_organizacija_Non_government_organization",
		"SI451":"Politi_na_stranka_Political_party",
		"SI452":"Sindikat_Union",
		"SI453":"Drustvo_zveza_drustev_Association_Federation",
		"SI458":"Verska_skupnost_in_podobne_verske_organizacije_Religious_community_and_religious_organizations",
		"SI703":"Obrtna_zadruga_Chamber_of_Crafts",
		"SI708":"Kmetijska_zadruga_Agricultural_cooperative",
		"SI713":"zavod_v_zaseb_last_Institute_in_private_property",
		"SI715":"Druzbeno_podj_p_o_Social_enterprise",
		"SI719":"zadruga_Cooperative_x2",
		"SI799":"Druge_oblike_poslovnih_subjektov_Other_forms_of_business_entities",
		"SI804":"Poslovna_enota_Business_unit",
		"SI899":"Druge_oblike_delov_poslovnih_subjektov_Other_forms_of_parts_of_business_entities",
		"SK111":"v_o_s_Verejna_obchodna_spolo_nos_Public_commercial_company",
		"SK112":"s_r_o_Spolo_nos_s_ru_enim_obmedzenym_Limited_liability_company",
		"SK113":"k_s_Komanditna_spolo_nos_Societe_commandite",
		"SK117":"Nadacia_Foundation",
		"SK118":"Neinvesti_ny_fond_Non_investment_fund",
		"SK119":"N_O_Neziskova_organizacia_Not_profitable_organization",
		"SK120":"Neziskova_organizacia_poskytujuca_vseobecne_prospesne_sluzby_Non_profit_organization_providing_community_services",
		"SK121":"a_s_Akciova_spolo_nos_Joint_stock_company",
		"SK125":"Jednoducha_spolo_nos_na_akcie_Simple_joint_stock_company",
		"SK141":"Po_ovnicka_organizacia",
		"SK205":"Druzstvo_Cooperative_x2",
		"SK271":"Spolo_enstva_vlastnikov_pozemkov_bytov_a_pod_Associations_of_land_owners_flats_owner_etc",
		"SK272":"Pozemkove_spolo_enstvo",
		"SK273":"Zdruzenie_u_astnikov_pozemkovych_uprav",
		"SK301":"s_p_Statny_podnik_State_enterprise",
		"SK311":"Narodna_banka_Slovenska_National_Bank_of_Slovakia",
		"SK312":"Banka_statny_pe_azny_ustav_Bank_state_monetary_institution",
		"SK321":"Rozpo_tova_organizacia_Budgetary_organization",
		"SK331":"Prispevkova_organizacia_Organization_based_on_state_contributions",
		"SK333":"Verejna_vyskumna_institucia_Public_research_institution",
		"SK381":"Fondy_Funds",
		"SK382":"Verejnopravna_institucia_Public_legal_institution",
		"SK383":"Ina_organizacia_verejnej_spravy_Other_organization_of_public_administration",
		"SK421":"Zahrani_na_osoba_pravnicka_osoba_so_sidlom_mimo_uzemia_SR_Foreign_person_legal_unit",
		"SK434":"Doplnkova_dochodkova_pois_ov_a_Complementary_pension_funding",
		"SK445":"Komoditna_burza_Commodity_Exchange",
		"SK701":"Zdruzenie_zvaz_spolok_spolo_nos_klub_ai_Association_league_union_society_club_etc",
		"SK711":"Politicka_strana_politicke_hnutie_Political_party_political_movement",
		"SK721":"Cirkevna_organizacia_Ecclesiastical_organization",
		"SK741":"Stavovska_organizacia_profesna_komora_Professional_organization_professional_chamber",
		"SK745":"Komora_s_vynimkou_profesnych_komor_Chamber_except_professional_chambers",
		"SK751":"Zaujmove_zdruzenie_pravnickych_osob_Interest_association_of_legal_persons",
		"SK801":"Obec_obecny_urad_mesto_mestsky_urad_Municipality_municipal_office",
		"SK803":"VUC_Samospravny_kraj_urad_samospravneho_kraja_Office_of_local_government_regional_level",
		"SK901":"Zastupite_ske_organy_inych_statov_Diplomatic_corps_of_foreign_country",
		"SK911":"Zahrani_ne_kulturne_informa_ne_stredisko_rozhlasova_tla_ova_a_televizna_agentura_Foreign_centre_for_culture_and_information_agency_for_radio_press_and_television",
		"SK921":"Medzinarodne_organizacie_a_zdruzenia_International_organization_and_association",
		"SK931":"Zastupenie_zahrani_nej_pravnickej_osoby_Representation_of_foreign_legal_unit",
		"SPFUND":"Conventional_legal_form_for_Special_funds_Special_funds_are_unincorporated_investment_funds_comprising_investment_portfolios_owned_by_the_group_of_participants_and_whose_management_is_undertaken_in_general_by_other_financial_corporations_Such_funds_are_institutional_units_that_are_separate_from_the_managing_financial_corporation",
}

	LGL_FRM = models.CharField("LGL_FRM",max_length=255, choices=LGL_FRM_INPT_domain,default=None, blank=True, null=True, db_comment="LGL_FRM_INPT_domain")

	LGL_PRCDNG_STTS_INPT_domain = {		"0":"Not_applicable",
		"1":"No_legal_actions_taken_Legal_actions_have_not_been_taken_concerning_the_solvency_or_indebtedness_of_a_counterparty",
		"2":"Under_judicial_administration_receivership_or_similar_measures_Any_proceeding_involving_the_intervention_of_a_judicial_body_or_similar_aimed_at_reaching_a_refinancing_agreement_among_the_creditors_with_the_exception_of_any_bankruptcy_or_insolvency_proceedings",
		"3":"Bankruptcy_insolvency_Collective_and_binding_bankruptcy_or_insolvency_proceedings_under_judicial_control_which_entail_the_partial_or_total_divestment_of_a_counterparty_and_the_appointment_of_a_liquidator",
		"4":"Other_legal_measures_Legal_measures_other_than_those_already_specified_including_bilateral_legal_measures_between_the_reporting_agent_and_the_counterparty",
}

	LGL_PRCDNG_STTS = models.CharField("LGL_PRCDNG_STTS",max_length=255, choices=LGL_PRCDNG_STTS_INPT_domain,default=None, blank=True, null=True, db_comment="LGL_PRCDNG_STTS_INPT_domain")

	LST_NM = models.CharField("LST_NM",max_length=255,default=None, blank=True, null=True)

	LST_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"F":"Non_listed",
		"T":"Listed",
}

	LSTD_CNTRL_BNK_PRVT_SCTR_CMPNY_INDCTR = models.CharField("LSTD_CNTRL_BNK_PRVT_SCTR_CMPNY_INDCTR",max_length=255, choices=LST_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="LST_INDCTR_INPT_domain")

	MLTLTRL_DVLPMNT_BNK_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Multilateral_development_bank",
		"2":"Not_a_Multilateral_development_bank",
}

	MLTLTRL_DVLPMNT_BNK_INDCTR = models.CharField("MLTLTRL_DVLPMNT_BNK_INDCTR",max_length=255, choices=MLTLTRL_DVLPMNT_BNK_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="MLTLTRL_DVLPMNT_BNK_INDCTR_INPT_domain")

	MRKT_CP_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Large_Market_Capitalisation",
		"2":"Small_Market_Capitalisation",
}

	MRKT_CPTLSTN_INDCTR = models.CharField("MRKT_CPTLSTN_INDCTR",max_length=255, choices=MRKT_CP_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="MRKT_CP_INDCTR_INPT_domain")

	NM_ENTTY = models.CharField("NM_ENTTY",max_length=255,default=None, blank=True, null=True)

	NMBR_EMPLYS = models.FloatField("NMBR_EMPLYS",default=None, blank=True, null=True)

	ORGNSTN_BY_PRCDNG_STTS_INPT_domain = {		"0":"Not_applicable",
		"14":"Organisation_without_legal_proceeding",
		"15":"Organisation_with_legal_proceeding",
}

	ORGNSTN_TYP_BY_PRCDNG_STTS = models.CharField("ORGNSTN_TYP_BY_PRCDNG_STTS",max_length=255, choices=ORGNSTN_BY_PRCDNG_STTS_INPT_domain,default=None, blank=True, null=True, db_comment="ORGNSTN_BY_PRCDNG_STTS_INPT_domain")

	PD = models.FloatField("PD",default=None, blank=True, null=True)

	PLLNG_EFFCT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Pulling_effect",
		"2":"Not_pulling_effect",
}

	PLLNG_EFFCT_INDCTR = models.CharField("PLLNG_EFFCT_INDCTR",max_length=255, choices=PLLNG_EFFCT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="PLLNG_EFFCT_INDCTR_INPT_domain")

	PRFRMNG_STTS_domain = {		"1":"Non_performing",
		"11":"Performing",
}

	PRFRMNG_STTS = models.CharField("PRFRMNG_STTS",max_length=255, choices=PRFRMNG_STTS_domain,default=None, blank=True, null=True, db_comment="PRFRMNG_STTS_domain")

	PRFRMNG_STTS_RSN_domain = {		"1":"Failed_reclassification_to_performing_at_end_of_probation_period",
		"2":"Exited_from_Non_performing_exposure_NPE_in_the_last_12_months",
}

	PRFRMNG_STTS_RSN = models.CharField("PRFRMNG_STTS_RSN",max_length=255, choices=PRFRMNG_STTS_RSN_domain,default=None, blank=True, null=True, db_comment="PRFRMNG_STTS_RSN_domain")

	PRTY_TYP_ADDRSS_INPT_domain = {		"100":"European_Union_member_party",
		"101":"Non_European_Union_member_party",
		"6":"No_registered_Postal_Code_system_party",
}

	PRTY_TYP_ADDRS = models.CharField("PRTY_TYP_ADDRS",max_length=255, choices=PRTY_TYP_ADDRSS_INPT_domain,default=None, blank=True, null=True, db_comment="PRTY_TYP_ADDRSS_INPT_domain")

	PSTL_CD = models.CharField("PSTL_CD",max_length=255,default=None, blank=True, null=True)

	STRT = models.CharField("STRT",max_length=255,default=None, blank=True, null=True)

	NUTS3_INPT_domain = {		"0":"Not_applicable",
		"AT111":"Mittelburgenland",
		"AT112":"Nordburgenland",
		"AT113":"Sudburgenland",
		"AT121":"Mostviertel_Eisenwurzen",
		"AT122":"Niederosterreich_Sud",
		"AT123":"Sankt_Polten",
		"AT124":"Waldviertel",
		"AT125":"Weinviertel",
		"AT126":"Wiener_Umland_Nordteil",
		"AT127":"Wiener_Umland_Sudteil",
		"AT130":"Wien",
		"AT211":"Klagenfurt_Villach",
		"AT212":"Oberkarnten",
		"AT213":"Unterkarnten",
		"AT221":"Graz",
		"AT222":"Liezen",
		"AT223":"Ostliche_Obersteiermark",
		"AT224":"Oststeiermark",
		"AT225":"West_und_Sudsteiermark",
		"AT226":"Westliche_Obersteiermark",
		"AT311":"Innviertel",
		"AT312":"Linz_Wels",
		"AT313":"Muhlviertel",
		"AT314":"Steyr_Kirchdorf",
		"AT315":"Traunviertel",
		"AT321":"Lungau",
		"AT322":"Pinzgau_Pongau",
		"AT323":"Salzburg_und_Umgebung",
		"AT331":"Ausserfern",
		"AT332":"Innsbruck",
		"AT333":"Osttirol",
		"AT334":"Tiroler_Oberland",
		"AT335":"Tiroler_Unterland",
		"AT341":"Bludenz_Bregenzer_Wald",
		"AT342":"Rheintal_Bodenseegebiet",
		"ATZZZ":"Extra_Regio_NUTS_3",
		"BE100":"Arr_de_Bruxelles_Capitale_Arr_van_Brussel_Hoofdstad",
		"BE211":"Arr_Antwerpen",
		"BE212":"Arr_Mechelen",
		"BE213":"Arr_Turnhout",
		"BE221":"Arr_Hasselt",
		"BE222":"Arr_Maaseik",
		"BE223":"Arr_Tongeren",
		"BE231":"Arr_Aalst",
		"BE232":"Arr_Dendermonde",
		"BE233":"Arr_Eeklo",
		"BE234":"Arr_Gent",
		"BE235":"Arr_Oudenaarde",
		"BE236":"Arr_Sint_Niklaas",
		"BE241":"Arr_Halle_Vilvoorde",
		"BE242":"Arr_Leuven",
		"BE251":"Arr_Brugge",
		"BE252":"Arr_Diksmuide",
		"BE253":"Arr_Ieper",
		"BE254":"Arr_Kortrijk",
		"BE255":"Arr_Oostende",
		"BE256":"Arr_Roeselare",
		"BE257":"Arr_Tielt",
		"BE258":"Arr_Veurne",
		"BE310":"Arr_Nivelles",
		"BE321":"Arr_Ath",
		"BE322":"Arr_Charleroi",
		"BE323":"Arr_Mons",
		"BE324":"Arr_Mouscron",
		"BE325":"Arr_Soignies",
		"BE326":"Arr_Thuin",
		"BE327":"Arr_Tournai",
		"BE331":"Arr_Huy",
		"BE332":"Arr_Liege",
		"BE334":"Arr_Waremme",
		"BE335":"Arr_Verviers_communes_francophones",
		"BE336":"Bezirk_Verviers_Deutschsprachige_Gemeinschaft",
		"BE341":"Arr_Arlon",
		"BE342":"Arr_Bastogne",
		"BE343":"Arr_Marche_en_Famenne",
		"BE344":"Arr_Neufchateau",
		"BE345":"Arr_Virton",
		"BE351":"Arr_Dinant",
		"BE352":"Arr_Namur",
		"BE353":"Arr_Philippeville",
		"BEZZZ":"Extra_Regio_NUTS_3_x2",
		"BG311":"Vidin",
		"BG312":"Montana",
		"BG313":"Vratsa",
		"BG314":"Pleven",
		"BG315":"Lovech",
		"BG321":"Veliko_Tarnovo",
		"BG322":"Gabrovo",
		"BG323":"Ruse",
		"BG324":"Razgrad",
		"BG325":"Silistra",
		"BG331":"Varna",
		"BG332":"Dobrich",
		"BG333":"Shumen",
		"BG334":"Targovishte",
		"BG341":"Burgas",
		"BG342":"Sliven",
		"BG343":"Yambol",
		"BG344":"Stara_Zagora",
		"BG411":"Sofia_stolitsa",
		"BG412":"Sofia",
		"BG413":"Blagoevgrad",
		"BG414":"Pernik",
		"BG415":"Kyustendil",
		"BG421":"Plovdiv",
		"BG422":"Haskovo",
		"BG423":"Pazardzhik",
		"BG424":"Smolyan",
		"BG425":"Kardzhali",
		"BGZZZ":"Extra_Regio_NUTS_3_x3",
		"CY000":"Kypros",
		"CYZZZ":"Extra_Regio_NUTS_3_x4",
		"CZ010":"Hlavni_Mesto_Praha",
		"CZ020":"Stredocesky_Kraj",
		"CZ031":"Jihocesky_Kraj",
		"CZ032":"Plzensky_Kraj",
		"CZ041":"Karlovarsky_kraj",
		"CZ042":"Ustecky_kraj",
		"CZ051":"Liberecky_kraj",
		"CZ052":"Kralovehradecky_kraj",
		"CZ053":"Pardubicky_kraj",
		"CZ063":"Kraj_Vysocina",
		"CZ064":"Jihomoravsky_kraj",
		"CZ071":"Olomoucky_kraj",
		"CZ072":"Zlinsky_kraj",
		"CZ080":"Moravskoslezsky_kraj",
		"CZZZZ":"Extra_Regio_NUTS_3_x5",
		"DE111":"Stuttgart_Stadtkreis",
		"DE112":"Boblingen",
		"DE113":"Esslingen",
		"DE114":"Goppingen",
		"DE115":"Ludwigsburg",
		"DE116":"Rems_Murr_Kreis",
		"DE117":"Heilbronn_Stadtkreis",
		"DE118":"Heilbronn_Landkreis",
		"DE119":"Hohenlohekreis",
		"DE11A":"Schwabisch_Hall",
		"DE11B":"Main_Tauber_Kreis",
		"DE11C":"Heidenheim",
		"DE11D":"Ostalbkreis",
		"DE121":"Baden_Baden_Stadtkreis",
		"DE122":"Karlsruhe_Stadtkreis",
		"DE123":"Karlsruhe_Landkreis",
		"DE124":"Rastatt",
		"DE125":"Heidelberg_Stadtkreis",
		"DE126":"Mannheim_Stadtkreis",
		"DE127":"Neckar_Odenwald_Kreis",
		"DE128":"Rhein_Neckar_Kreis",
		"DE129":"Pforzheim_Stadtkreis",
		"DE12A":"Calw",
		"DE12B":"Enzkreis",
		"DE12C":"Freudenstadt",
		"DE131":"Freiburg_im_Breisgau_Stadtkreis",
		"DE132":"Breisgau_Hochschwarzwald",
		"DE133":"Emmendingen",
		"DE134":"Ortenaukreis",
		"DE135":"Rottweil",
		"DE136":"Schwarzwald_Baar_Kreis",
		"DE137":"Tuttlingen",
		"DE138":"Konstanz",
		"DE139":"Lorrach",
		"DE13A":"Waldshut",
		"DE141":"Reutlingen",
		"DE142":"Tubingen_Landkreis",
		"DE143":"Zollernalbkreis",
		"DE144":"Ulm_Stadtkreis",
		"DE145":"Alb_Donau_Kreis",
		"DE146":"Biberach",
		"DE147":"Bodenseekreis",
		"DE148":"Ravensburg",
		"DE149":"Sigmaringen",
		"DE211":"Ingolstadt_Kreisfreie_Stadt",
		"DE212":"Munchen_Kreisfreie_Stadt",
		"DE213":"Rosenheim_Kreisfreie_Stadt",
		"DE214":"Altotting",
		"DE215":"Berchtesgadener_Land",
		"DE216":"Bad_Tolz_Wolfratshausen",
		"DE217":"Dachau",
		"DE218":"Ebersberg",
		"DE219":"Eichstatt",
		"DE21A":"Erding",
		"DE21B":"Freising",
		"DE21C":"Furstenfeldbruck",
		"DE21D":"Garmisch_Partenkirchen",
		"DE21E":"Landsberg_am_Lech",
		"DE21F":"Miesbach",
		"DE21G":"Muhldorf_a_Inn",
		"DE21H":"Munchen_Landkreis",
		"DE21I":"Neuburg_Schrobenhausen",
		"DE21J":"Pfaffenhofen_a_d_Ilm",
		"DE21K":"Rosenheim_Landkreis",
		"DE21L":"Starnberg",
		"DE21M":"Traunstein",
		"DE21N":"Weilheim_Schongau",
		"DE221":"Landshut_Kreisfreie_Stadt",
		"DE222":"Passau_Kreisfreie_Stadt",
		"DE223":"Straubing_Kreisfreie_Stadt",
		"DE224":"Deggendorf",
		"DE225":"Freyung_Grafenau",
		"DE226":"Kelheim",
		"DE227":"Landshut_Landkreis",
		"DE228":"Passau_Landkreis",
		"DE229":"Regen",
		"DE22A":"Rottal_Inn",
		"DE22B":"Straubing_Bogen",
		"DE22C":"Dingolfing_Landau",
		"DE231":"Amberg_Kreisfreie_Stadt",
		"DE232":"Regensburg_Kreisfreie_Stadt",
		"DE233":"Weiden_i_d_Opf_Kreisfreie_Stadt",
		"DE234":"Amberg_Sulzbach",
		"DE235":"Cham",
		"DE236":"Neumarkt_i_d_OPf",
		"DE237":"Neustadt_a_d_Waldnaab",
		"DE238":"Regensburg_Landkreis",
		"DE239":"Schwandorf",
		"DE23A":"Tirschenreuth",
		"DE241":"Bamberg_Kreisfreie_Stadt",
		"DE242":"Bayreuth_Kreisfreie_Stadt",
		"DE243":"Coburg_Kreisfreie_Stadt",
		"DE244":"Hof_Kreisfreie_Stadt",
		"DE245":"Bamberg_Landkreis",
		"DE246":"Bayreuth_Landkreis",
		"DE247":"Coburg_Landkreis",
		"DE248":"Forchheim",
		"DE249":"Hof_Landkreis",
		"DE24A":"Kronach",
		"DE24B":"Kulmbach",
		"DE24C":"Lichtenfels",
		"DE24D":"Wunsiedel_i_Fichtelgebirge",
		"DE251":"Ansbach_Kreisfreie_Stadt",
		"DE252":"Erlangen_Kreisfreie_Stadt",
		"DE253":"Furth_Kreisfreie_Stadt",
		"DE254":"Nurnberg_Kreisfreie_Stadt",
		"DE255":"Schwabach_Kreisfreie_Stadt",
		"DE256":"Ansbach_Landkreis",
		"DE257":"Erlangen_Hochstadt",
		"DE258":"Furth_Landkreis",
		"DE259":"Nurnberger_Land",
		"DE25A":"Neustadt_a_d_Aisch_Bad_Windsheim",
		"DE25B":"Roth",
		"DE25C":"Weissenburg_Gunzenhausen",
		"DE261":"Aschaffenburg_Kreisfreie_Stadt",
		"DE262":"Schweinfurt_Kreisfreie_Stadt",
		"DE263":"Wurzburg_Kreisfreie_Stadt",
		"DE264":"Aschaffenburg_Landkreis",
		"DE265":"Bad_Kissingen",
		"DE266":"Rhon_Grabfeld",
		"DE267":"Hassberge",
		"DE268":"Kitzingen",
		"DE269":"Miltenberg",
		"DE26A":"Main_Spessart",
		"DE26B":"Schweinfurt_Landkreis",
		"DE26C":"Wurzburg_Landkreis",
		"DE271":"Augsburg_Kreisfreie_Stadt",
		"DE272":"Kaufbeuren_Kreisfreie_Stadt",
		"DE273":"Kempten_Allgau_Kreisfreie_Stadt",
		"DE274":"Memmingen_Kreisfreie_Stadt",
		"DE275":"Aichach_Friedberg",
		"DE276":"Augsburg_Landkreis",
		"DE277":"Dillingen_a_d_Donau",
		"DE278":"Gunzburg",
		"DE279":"Neu_Ulm",
		"DE27A":"Lindau_Bodensee",
		"DE27B":"Ostallgau",
		"DE27C":"Unterallgau",
		"DE27D":"Donau_Ries",
		"DE27E":"Oberallgau",
		"DE300":"Berlin",
		"DE401":"Brandenburg_an_der_Havel_Kreisfreie_Stadt",
		"DE402":"Cottbus_Kreisfreie_Stadt",
		"DE403":"Frankfurt_Oder_Kreisfreie_Stadt",
		"DE404":"Potsdam_Kreisfreie_Stadt",
		"DE405":"Barnim",
		"DE406":"Dahme_Spreewald",
		"DE407":"Elbe_Elster",
		"DE408":"Havelland",
		"DE409":"Markisch_Oderland",
		"DE40A":"Oberhavel",
		"DE40B":"Oberspreewald_Lausitz",
		"DE40C":"Oder_Spree",
		"DE40D":"Ostprignitz_Ruppin",
		"DE40E":"Potsdam_Mittelmark",
		"DE40F":"Prignitz",
		"DE40G":"Spree_Neisse",
		"DE40H":"Teltow_Flaming",
		"DE40I":"Uckermark",
		"DE501":"Bremen_Kreisfreie_Stadt",
		"DE502":"Bremerhaven_Kreisfreie_Stadt",
		"DE600":"Hamburg",
		"DE711":"Darmstadt_Kreisfreie_Stadt",
		"DE712":"Frankfurt_am_Main_Kreisfreie_Stadt",
		"DE713":"Offenbach_am_Main_Kreisfreie_Stadt",
		"DE714":"Wiesbaden_Kreisfreie_Stadt",
		"DE715":"Bergstrasse",
		"DE716":"Darmstadt_Dieburg",
		"DE717":"Gross_Gerau",
		"DE718":"Hochtaunuskreis",
		"DE719":"Main_Kinzig_Kreis",
		"DE71A":"Main_Taunus_Kreis",
		"DE71B":"Odenwaldkreis",
		"DE71C":"Offenbach_Landkreis",
		"DE71D":"Rheingau_Taunus_Kreis",
		"DE71E":"Wetteraukreis",
		"DE721":"Giessen_Landkreis",
		"DE722":"Lahn_Dill_Kreis",
		"DE723":"Limburg_Weilburg",
		"DE724":"Marburg_Biedenkopf",
		"DE725":"Vogelsbergkreis",
		"DE731":"Kassel_Kreisfreie_Stadt",
		"DE732":"Fulda",
		"DE733":"Hersfeld_Rotenburg",
		"DE734":"Kassel_Landkreis",
		"DE735":"Schwalm_Eder_Kreis",
		"DE736":"Waldeck_Frankenberg",
		"DE737":"Werra_Meissner_Kreis",
		"DE803":"Rostock_Kreisfreie_Stadt",
		"DE804":"Schwerin_Kreisfreie_Stadt",
		"DE80J":"Mecklenburgische_Seenplatte",
		"DE80K":"Landkreis_Rostock",
		"DE80L":"Vorpommern_Rugen",
		"DE80M":"Nordwestmecklenburg",
		"DE80N":"Vorpommern_Greifswald",
		"DE80O":"Ludwigslust_Parchim",
		"DE911":"Braunschweig_Kreisfreie_Stadt",
		"DE912":"Salzgitter_Kreisfreie_Stadt",
		"DE913":"Wolfsburg_Kreisfreie_Stadt",
		"DE914":"Gifhorn",
		"DE916":"Goslar",
		"DE917":"Helmstedt",
		"DE918":"Northeim",
		"DE91A":"Peine",
		"DE91B":"Wolfenbuttel",
		"DE91C":"Gottingen",
		"DE922":"Diepholz",
		"DE923":"Hameln_Pyrmont",
		"DE925":"Hildesheim",
		"DE926":"Holzminden",
		"DE927":"Nienburg_Weser",
		"DE928":"Schaumburg",
		"DE929":"Region_Hannover",
		"DE931":"Celle",
		"DE932":"Cuxhaven",
		"DE933":"Harburg",
		"DE934":"Luchow_Dannenberg",
		"DE935":"Luneburg_Landkreis",
		"DE936":"Osterholz",
		"DE937":"Rotenburg_Wumme",
		"DE938":"Soltau_Fallingbostel",
		"DE939":"Stade",
		"DE93A":"Uelzen",
		"DE93B":"Verden",
		"DE941":"Delmenhorst_Kreisfreie_Stadt",
		"DE942":"Emden_Kreisfreie_Stadt",
		"DE943":"Oldenburg_Oldenburg_Kreisfreie_Stadt",
		"DE944":"Osnabruck_Kreisfreie_Stadt",
		"DE945":"Wilhelmshaven_Kreisfreie_Stadt",
		"DE946":"Ammerland",
		"DE947":"Aurich",
		"DE948":"Cloppenburg",
		"DE949":"Emsland",
		"DE94A":"Friesland_DE",
		"DE94B":"Grafschaft_Bentheim",
		"DE94C":"Leer",
		"DE94D":"Oldenburg_Landkreis",
		"DE94E":"Osnabruck_Landkreis",
		"DE94F":"Vechta",
		"DE94G":"Wesermarsch",
		"DE94H":"Wittmund",
		"DEA11":"Dusseldorf_Kreisfreie_Stadt",
		"DEA12":"Duisburg_Kreisfreie_Stadt",
		"DEA13":"Essen_Kreisfreie_Stadt",
		"DEA14":"Krefeld_Kreisfreie_Stadt",
		"DEA15":"Monchengladbach_Kreisfreie_Stadt",
		"DEA16":"Mulheim_an_der_Ruhr_Kreisfreie_Stadt",
		"DEA17":"Oberhausen_Kreisfreie_Stadt",
		"DEA18":"Remscheid_Kreisfreie_Stadt",
		"DEA19":"Solingen_Kreisfreie_Stadt",
		"DEA1A":"Wuppertal_Kreisfreie_Stadt",
		"DEA1B":"Kleve",
		"DEA1C":"Mettmann",
		"DEA1D":"Rhein_Kreis_Neuss",
		"DEA1E":"Viersen",
		"DEA1F":"Wesel",
		"DEA22":"Bonn_Kreisfreie_Stadt",
		"DEA23":"Koln_Kreisfreie_Stadt",
		"DEA24":"Leverkusen_Kreisfreie_Stadt",
		"DEA26":"Duren",
		"DEA27":"Rhein_Erft_Kreis",
		"DEA28":"Euskirchen",
		"DEA29":"Heinsberg",
		"DEA2A":"Oberbergischer_Kreis",
		"DEA2B":"Rheinisch_Bergischer_Kreis",
		"DEA2C":"Rhein_Sieg_Kreis",
		"DEA2D":"Stadteregion_Aachen",
		"DEA31":"Bottrop_Kreisfreie_Stadt",
		"DEA32":"Gelsenkirchen_Kreisfreie_Stadt",
		"DEA33":"Munster_Kreisfreie_Stadt",
		"DEA34":"Borken",
		"DEA35":"Coesfeld",
		"DEA36":"Recklinghausen",
		"DEA37":"Steinfurt",
		"DEA38":"Warendorf",
		"DEA41":"Bielefeld_Kreisfreie_Stadt",
		"DEA42":"Gutersloh",
		"DEA43":"Herford",
		"DEA44":"Hoxter",
		"DEA45":"Lippe",
		"DEA46":"Minden_Lubbecke",
		"DEA47":"Paderborn",
		"DEA51":"Bochum_Kreisfreie_Stadt",
		"DEA52":"Dortmund_Kreisfreie_Stadt",
		"DEA53":"Hagen_Kreisfreie_Stadt",
		"DEA54":"Hamm_Kreisfreie_Stadt",
		"DEA55":"Herne_Kreisfreie_Stadt",
		"DEA56":"Ennepe_Ruhr_Kreis",
		"DEA57":"Hochsauerlandkreis",
		"DEA58":"Markischer_Kreis",
		"DEA59":"Olpe",
		"DEA5A":"Siegen_Wittgenstein",
		"DEA5B":"Soest",
		"DEA5C":"Unna",
		"DEB11":"Koblenz_Kreisfreie_Stadt",
		"DEB12":"Ahrweiler",
		"DEB13":"Altenkirchen_Westerwald",
		"DEB14":"Bad_Kreuznach",
		"DEB15":"Birkenfeld",
		"DEB17":"Mayen_Koblenz",
		"DEB18":"Neuwied",
		"DEB1A":"Rhein_Lahn_Kreis",
		"DEB1B":"Westerwaldkreis",
		"DEB1C":"Cochem_Zell",
		"DEB1D":"Rhein_Hunsruck_Kreis",
		"DEB21":"Trier_Kreisfreie_Stadt",
		"DEB22":"Bernkastel_Wittlich",
		"DEB23":"Eifelkreis_Bitburg_Prum",
		"DEB24":"Vulkaneifel",
		"DEB25":"Trier_Saarburg",
		"DEB31":"Frankenthal_Pfalz_Kreisfreie_Stadt",
		"DEB32":"Kaiserslautern_Kreisfreie_Stadt",
		"DEB33":"Landau_in_der_Pfalz_Kreisfreie_Stadt",
		"DEB34":"Ludwigshafen_am_Rhein_Kreisfreie_Stadt",
		"DEB35":"Mainz_Kreisfreie_Stadt",
		"DEB36":"Neustadt_an_der_Weinstrasse_Kreisfreie_Stadt",
		"DEB37":"Pirmasens_Kreisfreie_Stadt",
		"DEB38":"Speyer_Kreisfreie_Stadt",
		"DEB39":"Worms_Kreisfreie_Stadt",
		"DEB3A":"Zweibrucken_Kreisfreie_Stadt",
		"DEB3B":"Alzey_Worms",
		"DEB3C":"Bad_Durkheim",
		"DEB3D":"Donnersbergkreis",
		"DEB3E":"Germersheim",
		"DEB3F":"Kaiserslautern_Landkreis",
		"DEB3G":"Kusel",
		"DEB3H":"Sudliche_Weinstrasse",
		"DEB3I":"Rhein_Pfalz_Kreis",
		"DEB3J":"Mainz_Bingen",
		"DEB3K":"Sudwestpfalz",
		"DEC01":"Regionalverband_Saarbrucken",
		"DEC02":"Merzig_Wadern",
		"DEC03":"Neunkirchen",
		"DEC04":"Saarlouis",
		"DEC05":"Saarpfalz_Kreis",
		"DEC06":"St_Wendel",
		"DED21":"Dresden_Kreisfreie_Stadt",
		"DED2C":"Bautzen",
		"DED2D":"Gorlitz",
		"DED2E":"Meissen",
		"DED2F":"Sachsische_Schweiz_Osterzgebirge",
		"DED41":"Chemnitz_Kreisfreie_Stadt",
		"DED42":"Erzgebirgskreis",
		"DED43":"Mittelsachsen",
		"DED44":"Vogtlandkreis",
		"DED45":"Zwichau",
		"DED51":"Leipzig_Kreisfreie_Stadt",
		"DED52":"Leipzig",
		"DED53":"Nordsachsen",
		"DEE01":"Dessau_Rosslau_Kreisfreie_Stadt",
		"DEE02":"Halle_Saale_Kreisfreie_Stadt",
		"DEE03":"Magdeburg_Kreisfreie_Stadt",
		"DEE04":"Altmarkkreis_Salzwedel",
		"DEE05":"Anhalt_Bitterfeld",
		"DEE06":"Jerichower_Land",
		"DEE07":"Borde",
		"DEE08":"Burgenland_DE",
		"DEE09":"Harz",
		"DEE0A":"Mansfeld_Sudharz",
		"DEE0B":"Saalekreis",
		"DEE0C":"Salzlandkreis",
		"DEE0D":"Stendal",
		"DEE0E":"Wittenberg",
		"DEF01":"Flensburg_Kreisfreie_Stadt",
		"DEF02":"Kiel_Kreisfreie_Stadt",
		"DEF03":"Lubeck_Kreisfreie_Stadt",
		"DEF04":"Neumunster_Kreisfreie_Stadt",
		"DEF05":"Dithmarschen",
		"DEF06":"Herzogtum_Lauenburg",
		"DEF07":"Nordfriesland",
		"DEF08":"Ostholstein",
		"DEF09":"Pinneberg",
		"DEF0A":"Plon",
		"DEF0B":"Rendsburg_Eckernforde",
		"DEF0C":"Schleswig_Flensburg",
		"DEF0D":"Segeberg",
		"DEF0E":"Steinburg",
		"DEF0F":"Stormarn",
		"DEG01":"Erfurt_Kreisfreie_Stadt",
		"DEG02":"Gera_Kreisfreie_Stadt",
		"DEG03":"Jena_Kreisfreie_Stadt",
		"DEG04":"Suhl_Kreisfreie_Stadt",
		"DEG05":"Weimar_Kreisfreie_Stadt",
		"DEG06":"Eichsfeld",
		"DEG07":"Nordhausen",
		"DEG09":"Unstrut_Hainich_Kreis",
		"DEG0A":"Kyffhauserkreis",
		"DEG0B":"Schmalkalden_Meiningen",
		"DEG0C":"Gotha",
		"DEG0D":"Sommerda",
		"DEG0E":"Hildburghausen",
		"DEG0F":"Ilm_Kreis",
		"DEG0G":"Weimarer_Land",
		"DEG0H":"Sonneberg",
		"DEG0I":"Saalfeld_Rudolstadt",
		"DEG0J":"Saale_Holzland_Kreis",
		"DEG0K":"Saale_Orla_Kreis",
		"DEG0L":"Greiz",
		"DEG0M":"Altenburger_Land",
		"DEG0N":"Eisenach_Kreisfreie_Stadt",
		"DEG0P":"Wartburgkreis",
		"DEZZZ":"Extra_Regio_NUTS_3_x6",
		"DK011":"Byen_Kobenhavn",
		"DK012":"Kobenhavns_omegn",
		"DK013":"Nordsjaelland",
		"DK014":"Bornholm",
		"DK021":"Ostsjaelland",
		"DK022":"Vest_og_Sydsjaelland",
		"DK031":"Fyn",
		"DK032":"Sydjylland",
		"DK041":"Vestjylland",
		"DK042":"Ostjylland",
		"DK050":"Nordjylland",
		"DKZZZ":"Extra_Regio_NUTS_3_x7",
		"EE001":"Pohja_Eesti",
		"EE004":"Laane_Eesti",
		"EE006":"Kesk_Eesti",
		"EE007":"Kirde_Eesti",
		"EE008":"Louna_Eesti",
		"EEZZZ":"Extra_Regio_NUTS_3_x8",
		"EL301":"Voreios_Tomeas_Athinon",
		"EL302":"Dytikos_Tomeas_Athinon",
		"EL303":"Kentrikos_Tomeas_Athinon",
		"EL304":"Notios_Tomeas_Athinon",
		"EL305":"Anatoliki_Attiki",
		"EL306":"Dytiki_Attiki",
		"EL307":"Peiraias_Nisoi",
		"EL411":"Lesvos",
		"EL412":"Samos",
		"EL413":"Chios",
		"EL421":"Dodekanisos",
		"EL422":"Kyklades",
		"EL431":"Irakleio",
		"EL432":"Lasithi",
		"EL433":"Rethymni",
		"EL434":"Chania",
		"EL511":"Evros",
		"EL512":"Xanthi",
		"EL513":"Rodopi",
		"EL514":"Drama",
		"EL515":"Thasos_Kavala",
		"EL521":"Imathia",
		"EL522":"Thessaloniki",
		"EL523":"Kilkis",
		"EL524":"Pella",
		"EL525":"Pieria",
		"EL526":"Serres",
		"EL527":"Chalkidiki",
		"EL531":"Grevena_Kozani",
		"EL532":"Kastoria",
		"EL533":"Florina",
		"EL541":"Arta_Preveza",
		"EL542":"Thesprotia",
		"EL543":"Ioannina",
		"EL611":"Karditsa_Trikala",
		"EL612":"Larisa",
		"EL613":"Magnisia_Sporades",
		"EL621":"Zakynthos",
		"EL622":"Kerkyra",
		"EL623":"Ithaki_Kefallinia",
		"EL624":"Lefkada",
		"EL631":"Aitoloakarnania",
		"EL632":"Achaia",
		"EL633":"Ileia",
		"EL641":"Voiotia",
		"EL642":"Evvoia",
		"EL643":"Evrytania",
		"EL644":"Fthiotida",
		"EL645":"Fokida",
		"EL651":"Argolida_Arkadia",
		"EL652":"Korinthia",
		"EL653":"lakonia_Messinia",
		"ELZZZ":"Extra_Regio_NUTS_3_x9",
		"ES111":"A_Coruna",
		"ES112":"Lugo",
		"ES113":"Ourense",
		"ES114":"Pontevedra",
		"ES120":"Asturias",
		"ES130":"Cantabria",
		"ES211":"Alava",
		"ES212":"Guipuzcoa",
		"ES213":"Vizcaya",
		"ES220":"Navarra",
		"ES230":"La_Rioja",
		"ES241":"Huesca",
		"ES242":"Teruel",
		"ES243":"Zaragoza",
		"ES300":"Madrid",
		"ES411":"Avila",
		"ES412":"Burgos",
		"ES413":"Leon",
		"ES414":"Palencia",
		"ES415":"Salamanca",
		"ES416":"Segovia",
		"ES417":"Soria",
		"ES418":"Valladolid",
		"ES419":"Zamora",
		"ES421":"Albacete",
		"ES422":"Ciudad_Real",
		"ES423":"Cuenca",
		"ES424":"Guadalajara",
		"ES425":"Toledo",
		"ES431":"Badajoz",
		"ES432":"Caceres",
		"ES511":"Barcelona",
		"ES512":"Girona",
		"ES513":"Lleida",
		"ES514":"Tarragona",
		"ES521":"Alicante_Alacant",
		"ES522":"Castellon_Castello",
		"ES523":"Valencia_Valencia",
		"ES531":"Eivissa_y_Formentera",
		"ES532":"Mallorca",
		"ES533":"Menorca",
		"ES611":"Almeria",
		"ES612":"Cadiz",
		"ES613":"Cordoba",
		"ES614":"Granada",
		"ES615":"Huelva",
		"ES616":"Jaen",
		"ES617":"Malaga",
		"ES618":"Sevilla",
		"ES620":"Murcia",
		"ES630":"Ceuta",
		"ES640":"Melilla",
		"ES703":"El_Hierro",
		"ES704":"Fuerteventura",
		"ES705":"Gran_Canaria",
		"ES706":"La_Gomera",
		"ES707":"La_Palma",
		"ES708":"Lanzarote",
		"ES709":"Tenerife",
		"ESZZZ":"Extra_Regio_NUTS_3_x10",
		"FI193":"Keski_Suomi",
		"FI194":"Etela_Pohjanmaa",
		"FI195":"Pohjanmaa",
		"FI196":"Satakunta",
		"FI197":"Pirkanmaa",
		"FI1B1":"Helsinki_Uusimaa",
		"FI1C1":"Varsinais_Suomi",
		"FI1C2":"Kanta_Hame",
		"FI1C3":"Paijat_Hame",
		"FI1C4":"Kymenlaakso",
		"FI1C5":"Etela_Karjala",
		"FI1D1":"Etela_Savo",
		"FI1D2":"Pohjois_Savo",
		"FI1D3":"Pohjois_Karjala",
		"FI1D5":"Keski_Pohjanmaa",
		"FI1D7":"Lappi",
		"FI1D8":"Kainuu",
		"FI1D9":"Pohjois_Pohjanmaa",
		"FI200":"Aland",
		"FIZZZ":"Extra_Regio_NUTS_3_x11",
		"FR101":"Paris",
		"FR102":"Seine_et_Marne",
		"FR103":"Yvelines",
		"FR104":"Essonne",
		"FR105":"Hauts_de_Seine",
		"FR106":"Seine_Saint_Denis",
		"FR107":"Val_de_Marne",
		"FR108":"Val_d_Oise",
		"FRB01":"Cher",
		"FRB02":"Eure_et_Loir",
		"FRB03":"Indre",
		"FRB04":"Indre_et_Loire",
		"FRB05":"Loir_et_Cher",
		"FRB06":"Loiret",
		"FRC11":"Cote_d_Or",
		"FRC12":"Nievre",
		"FRC13":"Saone_et_Loire",
		"FRC14":"Yonne",
		"FRC21":"Doubs",
		"FRC22":"Jura",
		"FRC23":"Haute_Saone",
		"FRC24":"Territoire_de_Belfort",
		"FRD11":"Calvados",
		"FRD12":"Manche",
		"FRD13":"Orne",
		"FRD21":"Eure",
		"FRD22":"Seine_Maritime",
		"FRE11":"Nord",
		"FRE12":"Pas_de_Calais",
		"FRE21":"Aisne",
		"FRE22":"Oise",
		"FRE23":"Somme",
		"FRF11":"Bas_Rhin",
		"FRF12":"Haut_Rhin",
		"FRF21":"Ardennes",
		"FRF22":"Aube",
		"FRF23":"Marne",
		"FRF24":"Haute_Marne",
		"FRF31":"Meurthe_et_Moselle",
		"FRF32":"Meuse",
		"FRF33":"Moselle",
		"FRF34":"Vosges",
		"FRG01":"Loire_Atlantique",
		"FRG02":"Maine_et_Loire",
		"FRG03":"Mayenne",
		"FRG04":"Sarthe",
		"FRG05":"Vendee",
		"FRH01":"Cotes_d_Armor",
		"FRH02":"Finistere",
		"FRH03":"Ille_et_Vilaine",
		"FRH04":"Morbihan",
		"FRI11":"Dordogne",
		"FRI12":"Gironde",
		"FRI13":"Landes",
		"FRI14":"Lot_et_Garonne",
		"FRI15":"Pyrenees_Atlantiques",
		"FRI21":"Correze",
		"FRI22":"Creuse",
		"FRI23":"Haute_Vienne",
		"FRI31":"Charente",
		"FRI32":"Charente_Maritime",
		"FRI33":"Deux_Sevres",
		"FRI34":"Vienne",
		"FRJ11":"Aude",
		"FRJ12":"Gard",
		"FRJ13":"Herault",
		"FRJ14":"Lozere",
		"FRJ15":"Pyrenees_Orientales",
		"FRJ21":"Ariege",
		"FRJ22":"Aveyron",
		"FRJ23":"Haute_Garonne",
		"FRJ24":"Gers",
		"FRJ25":"Lot",
		"FRJ26":"Hautes_Pyrenees",
		"FRJ27":"Tarn",
		"FRJ28":"Tarn_et_Garonne",
		"FRK11":"Allier",
		"FRK12":"Cantal",
		"FRK13":"Haute_Loire",
		"FRK14":"Puy_de_Dome",
		"FRK21":"Ain",
		"FRK22":"Ardeche",
		"FRK23":"Drome",
		"FRK24":"Isere",
		"FRK25":"Loire",
		"FRK26":"Rhone",
		"FRK27":"Savoie",
		"FRK28":"Haute_Savoie",
		"FRL01":"Alpes_de_Haute_Provence",
		"FRL02":"Hautes_Alpes",
		"FRL03":"Alpes_Maritimes",
		"FRL04":"Bouches_du_Rhone",
		"FRL05":"Var",
		"FRL06":"Vaucluse",
		"FRM01":"Corse_du_Sud",
		"FRM02":"Haute_Corse",
		"FRY10":"Guadeloupe",
		"FRY20":"Martinique",
		"FRY30":"Guyane",
		"FRY40":"La_Reunion",
		"FRY50":"Mayotte",
		"FRZZZ":"Extra_Regio_NUTS_3_x12",
		"HR031":"Primorsko_goranska_zupanija",
		"HR032":"Licko_senjska_Zupanija",
		"HR033":"Zadarska_zupanija",
		"HR034":"Sibensko_kninska_zupanija",
		"HR035":"Splitsko_dalmatinska_zupanija",
		"HR036":"Istarska_zupanija",
		"HR037":"Dubrovacko_neretvanska_Zupanija",
		"HR041":"Grad_Zagreb",
		"HR042":"Zagrebacka_Zupanija",
		"HR043":"Krapinsko_zagorska_zupanija",
		"HR044":"Varazdinska_zupanija",
		"HR045":"Koprivnicko_krizevacka_Zupanija",
		"HR046":"Medimurska_Zupanija",
		"HR047":"Bjelovarsko_bilogorska_zupanija",
		"HR048":"Viroviticko_podravska_Zupanija",
		"HR049":"Pozesko_slavonska_zupanija",
		"HR04A":"Brodsko_posavska_zupanija",
		"HR04B":"Osjecko_baranjska_Zupanija",
		"HR04C":"Vukovarsko_srijemska_zupanija",
		"HR04D":"Karlovacka_Zupanija",
		"HR04E":"Sisacko_moslavacka_Zupanija",
		"HRZZZ":"Extra_Regio_NUTS_3_x13",
		"HU110":"Budapest",
		"HU120":"Pest",
		"HU211":"Fejer",
		"HU212":"Komarom_Esztergom",
		"HU213":"Veszprem",
		"HU221":"Gyor_moson_sopron",
		"HU222":"Vas",
		"HU223":"Zala",
		"HU231":"Baranya",
		"HU232":"Somogy",
		"HU233":"Tolna",
		"HU311":"Borsod_Abauj_Zemplen",
		"HU312":"Heves",
		"HU313":"Nograd",
		"HU321":"Hajdu_Bihar",
		"HU322":"Jasz_Nagykun_Szolnok",
		"HU323":"Szabolcs_Szatmar_Bereg",
		"HU331":"Bacs_Kiskun",
		"HU332":"Bekes",
		"HU333":"Csongrad",
		"HUZZZ":"Extra_Regio_NUTS_3_x14",
		"IE041":"Border",
		"IE042":"West",
		"IE051":"Mid_West",
		"IE052":"South_East",
		"IE053":"South_West",
		"IE061":"Dublin",
		"IE062":"Mid_East",
		"IE063":"Midland",
		"IEZZZ":"Extra_Regio_NUTS_3_x15",
		"ITC11":"Torino",
		"ITC12":"Vercelli",
		"ITC13":"Biella",
		"ITC14":"Verbano_Cusio_Ossola",
		"ITC15":"Novara",
		"ITC16":"Cuneo",
		"ITC17":"Asti",
		"ITC18":"Alessandria",
		"ITC20":"Valle_d_Aosta_Vallee_d_Aoste",
		"ITC31":"Imperia",
		"ITC32":"Savona",
		"ITC33":"Genova",
		"ITC34":"La_Spezia",
		"ITC41":"Varese",
		"ITC42":"Como",
		"ITC43":"Lecco",
		"ITC44":"Sondrio",
		"ITC46":"Bergamo",
		"ITC47":"Brescia",
		"ITC48":"Pavia",
		"ITC49":"Lodi",
		"ITC4A":"Cremona",
		"ITC4B":"Mantova",
		"ITC4C":"Milano",
		"ITC4D":"Monza_e_della_Brianza",
		"ITF11":"L_Aquila",
		"ITF12":"Teramo",
		"ITF13":"Pescara",
		"ITF14":"Chieti",
		"ITF21":"Isernia",
		"ITF22":"Campobasso",
		"ITF31":"Caserta",
		"ITF32":"Benevento",
		"ITF33":"Napoli",
		"ITF34":"Avellino",
		"ITF35":"Salerno",
		"ITF43":"Taranto",
		"ITF44":"Brindisi",
		"ITF45":"Lecce",
		"ITF46":"Foggia",
		"ITF47":"Bari",
		"ITF48":"Barletta_Andria_Trani",
		"ITF51":"Potenza",
		"ITF52":"Matera",
		"ITF61":"Cosenza",
		"ITF62":"Crotone",
		"ITF63":"Catanzaro",
		"ITF64":"Vibo_Valentia",
		"ITF65":"Reggio_di_Calabria",
		"ITG11":"Trapani",
		"ITG12":"Palermo",
		"ITG13":"Messina",
		"ITG14":"Agrigento",
		"ITG15":"Caltanissetta",
		"ITG16":"Enna",
		"ITG17":"Catania",
		"ITG18":"Ragusa",
		"ITG19":"Siracusa",
		"ITG25":"Sassari",
		"ITG26":"Nuoro",
		"ITG27":"Cagliari",
		"ITG28":"Oristano",
		"ITG29":"Olbia_Tempio",
		"ITG2A":"Ogliastra",
		"ITG2B":"Medio_Campidano",
		"ITG2C":"Carbonia_Iglesias",
		"ITH10":"Bolzano_Bozen",
		"ITH20":"Trento",
		"ITH31":"Verona",
		"ITH32":"Vicenza",
		"ITH33":"Belluno",
		"ITH34":"Treviso",
		"ITH35":"Venezia",
		"ITH36":"Padova",
		"ITH37":"Rovigo",
		"ITH41":"Pordenone",
		"ITH42":"Udine",
		"ITH43":"Gorizia",
		"ITH44":"Trieste",
		"ITH51":"Piacenza",
		"ITH52":"Parma",
		"ITH53":"Reggio_nell_Emilia",
		"ITH54":"Modena",
		"ITH55":"Bologna",
		"ITH56":"Ferrara",
		"ITH57":"Ravenna",
		"ITH58":"Forli_Cesena",
		"ITH59":"Rimini",
		"ITI11":"Massa_Carrara",
		"ITI12":"Lucca",
		"ITI13":"Pistoia",
		"ITI14":"Firenze",
		"ITI15":"Prato",
		"ITI16":"Livorno",
		"ITI17":"Pisa",
		"ITI18":"Arezzo",
		"ITI19":"Siena",
		"ITI1A":"Grosseto",
		"ITI21":"Perugia",
		"ITI22":"Terni",
		"ITI31":"Pesaro_e_Urbino",
		"ITI32":"Ancona",
		"ITI33":"Macerata",
		"ITI34":"Ascoli_Piceno",
		"ITI35":"Fermo",
		"ITI41":"Viterbo",
		"ITI42":"Rieti",
		"ITI43":"Roma",
		"ITI44":"Latina",
		"ITI45":"Frosinone",
		"ITZZZ":"Extra_Regio_NUTS_3_x16",
		"LT011":"Vilniaus_apskritis",
		"LT021":"Alytaus_apskritis",
		"LT022":"Kauno_apskritis",
		"LT023":"Klaip_dos_apskritis",
		"LT024":"Marijampol_s_apskritis",
		"LT025":"Panev_zio_apskritis",
		"LT026":"Siauli_apskritis",
		"LT027":"Taurag_s_apskritis",
		"LT028":"Telsi_apskritis",
		"LT029":"Utenos_apskritis",
		"LTZZZ":"Extra_Regio_NUTS_3_x17",
		"LU000":"Luxembourg",
		"LUZZZ":"Extra_Regio_NUTS_3_x18",
		"LV003":"Kurzeme",
		"LV005":"Latgale",
		"LV006":"Riga",
		"LV007":"Pieriga",
		"LV008":"Vidzeme",
		"LV009":"Zemgale",
		"LVZZZ":"Extra_Regio_NUTS_3_x19",
		"MT001":"Malta",
		"MT002":"Gozo_And_CominoGhawdex_U_Kemmuna",
		"MTZZZ":"Extra_Regio_NUTS_3_x20",
		"NL111":"Oost_Groningen",
		"NL112":"Delfzijl_en_omgeving",
		"NL113":"Overig_Groningen",
		"NL124":"Noord_Friesland",
		"NL125":"Zuidwest_Friesland",
		"NL126":"Zuidoost_Friesland",
		"NL131":"Noord_Drenthe",
		"NL132":"Zuidoost_Drenthe",
		"NL133":"Zuidwest_Drenthe",
		"NL211":"Noord_Overijssel",
		"NL212":"Zuidwest_Overijssel",
		"NL213":"Twente",
		"NL221":"Veluwe",
		"NL224":"Zuidwest_Gelderland",
		"NL225":"Achterhoek",
		"NL226":"Arnhem_Nijmegen",
		"NL230":"Flevoland",
		"NL310":"Utrecht",
		"NL321":"Kop_van_Noord_Holland",
		"NL323":"IJmond",
		"NL324":"Agglomeratie_Haarlem",
		"NL325":"Zaanstreek",
		"NL327":"Het_Gooi_en_Vechtstreek",
		"NL328":"Alkmaar_en_omgeving",
		"NL329":"Groot_Amsterdam",
		"NL332":"Agglomeratie_s_Gravenhage",
		"NL333":"Delft_en_Westland",
		"NL337":"Agglomeratie_Leiden_en_Bollenstreek",
		"NL33A":"Zuidoost_Zuid_Holland",
		"NL33B":"Oost_Zuid_Holland",
		"NL33C":"Groot_Rijnmond",
		"NL341":"Zeeuwsch_Vlaanderen",
		"NL342":"Overig_Zeeland",
		"NL411":"West_Noord_Brabant",
		"NL412":"Midden_Noord_Brabant",
		"NL413":"Noordoost_Noord_Brabant",
		"NL414":"Zuidoost_Noord_Brabant",
		"NL421":"Noord_Limburg",
		"NL422":"Midden_Limburg",
		"NL423":"Zuid_Limburg",
		"NLZZZ":"Extra_Regio_NUTS_3_x21",
		"PL213":"Miasto_Krakow",
		"PL214":"Krakowski",
		"PL217":"Tarnowski",
		"PL218":"Nowosadecki",
		"PL219":"Nowotarski",
		"PL21A":"Oswiecimski",
		"PL224":"Czestochowski",
		"PL225":"Bielski",
		"PL227":"Rybnicki",
		"PL228":"Bytomski",
		"PL229":"Gliwicki",
		"PL22A":"Katowicki",
		"PL22B":"Sosnowiecki",
		"PL22C":"Tyski",
		"PL411":"Pilski",
		"PL414":"Koninski",
		"PL415":"Miasto_Poznan",
		"PL416":"Kaliski",
		"PL417":"Leszczynski",
		"PL418":"Poznanski",
		"PL424":"Miasto_Szczecin",
		"PL426":"Koszalinski",
		"PL427":"Szczecinecko_pyrzycki",
		"PL428":"Szczecinski",
		"PL431":"Gorzowski",
		"PL432":"Zielonogorski",
		"PL514":"Miasto_Wroclaw",
		"PL515":"Jeleniogorski",
		"PL516":"Legnicko_glogowski",
		"PL517":"Walbrzyski",
		"PL518":"Wroclawski",
		"PL523":"Nyski",
		"PL524":"Opolski",
		"PL613":"Bydgosko_torunski",
		"PL616":"Grudziadzki",
		"PL617":"Inowroclawski",
		"PL618":"Swiecki",
		"PL619":"Wloclawski",
		"PL621":"Elblaski",
		"PL622":"Olsztynski",
		"PL623":"Elcki",
		"PL633":"Trojmiejski",
		"PL634":"Gdanski",
		"PL636":"Slupski",
		"PL637":"Chojnicki",
		"PL638":"Starogardzki",
		"PL711":"Miasto_od",
		"PL712":"_odzki",
		"PL713":"Piotrkowski",
		"PL714":"Sieradzki",
		"PL715":"Skierniewicki",
		"PL721":"Kielecki",
		"PL722":"Sandomiersko_j_drzejowski",
		"PL811":"Bialski",
		"PL812":"Che_msko_zamojski",
		"PL814":"Lubelski",
		"PL815":"Pu_awski",
		"PL821":"Kro_nie_ski",
		"PL822":"Przemyski",
		"PL823":"Rzeszowski",
		"PL824":"Tarnobrzeski",
		"PL841":"Bia_ostocki",
		"PL842":"_om_y_ski",
		"PL843":"Suwalski",
		"PL911":"Miasto_Warszawa",
		"PL912":"Warszawski_wschodni",
		"PL913":"Warszawski_zachodni",
		"PL921":"Radomski",
		"PL922":"Ciechanowski",
		"PL923":"P_ocki",
		"PL924":"Ostro_cki",
		"PL925":"Siedlecki",
		"PL926":"_yrardowski",
		"PLZZZ":"Extra_Regio_NUTS_3_x22",
		"PT111":"Minho_Lima",
		"PT112":"Cavado",
		"PT119":"Ave",
		"PT11A":"Area_Metropolitana_do_Porto",
		"PT11B":"Alto_Tamega",
		"PT11C":"Tamega_e_Sousa",
		"PT11D":"Douro",
		"PT11E":"Terras_de_Tras_os_Montes",
		"PT150":"Algarve",
		"PT16B":"Oeste",
		"PT16D":"Regiao_de_Aveiro",
		"PT16E":"Regiao_de_Coimbra",
		"PT16F":"Regiao_de_Leiria",
		"PT16G":"Viseu_Dao_Lafoes",
		"PT16H":"Beira_Baixa",
		"PT16I":"Medio_Tejo",
		"PT16J":"Beiras_e_Serra_da_Estrela",
		"PT170":"Area_Metropolitana_de_Lisboa",
		"PT181":"Alentejo_Litoral",
		"PT184":"Baixo_Alentejo",
		"PT185":"Leziria_do_Tejo",
		"PT186":"Alto_Alentejo",
		"PT187":"Alentejo_Central",
		"PT200":"Regiao_Autonoma_dos_Acores",
		"PT300":"Regiao_Autonoma_da_Madeira",
		"PTZZZ":"Extra_Regio_NUTS_3_x23",
		"RO111":"Bihor",
		"RO112":"Bistrita_nasaud",
		"RO113":"Cluj",
		"RO114":"Maramures",
		"RO115":"Satu_Mare",
		"RO116":"Salaj",
		"RO121":"Alba",
		"RO122":"Brasov",
		"RO123":"Covasna",
		"RO124":"Harghita",
		"RO125":"Mures",
		"RO126":"Sibiu",
		"RO211":"Bacau",
		"RO212":"Botosani",
		"RO213":"Iasi",
		"RO214":"Neamt",
		"RO215":"Suceava",
		"RO216":"Vaslui",
		"RO221":"Braila",
		"RO222":"Buzau",
		"RO223":"Constanta",
		"RO224":"Galati",
		"RO225":"Tulcea",
		"RO226":"Vrancea",
		"RO311":"Arges",
		"RO312":"Calarasi",
		"RO313":"Dambovita",
		"RO314":"Giurgiu",
		"RO315":"Ialomita",
		"RO316":"Prahova",
		"RO317":"Teleorman",
		"RO321":"Bucuresti",
		"RO322":"Ilfov",
		"RO411":"Dolj",
		"RO412":"Gorj",
		"RO413":"Mehedinti",
		"RO414":"Olt",
		"RO415":"Valcea",
		"RO421":"Arad",
		"RO422":"Caras_severin",
		"RO423":"Hunedoara",
		"RO424":"Timis",
		"ROZZZ":"Extra_Regio_NUTS_3_x24",
		"SE110":"Stockholms_lan",
		"SE121":"Uppsala_lan",
		"SE122":"Sodermanlands_lan",
		"SE123":"Ostergotlands_lan",
		"SE124":"Orebro_lan",
		"SE125":"Vastmanlands_lan",
		"SE211":"Jonkopings_lan",
		"SE212":"Kronobergs_lan",
		"SE213":"Kalmar_lan",
		"SE214":"Gotlands_lan",
		"SE221":"Blekinge_lan",
		"SE224":"Skane_lan",
		"SE231":"Hallands_lan",
		"SE232":"Vastra_Gotalands_lan",
		"SE311":"Varmlands_lan",
		"SE312":"Dalarnas_lan",
		"SE313":"Gavleborgs_lan",
		"SE321":"Vasternorrlands_lan",
		"SE322":"Jamtlands_lan",
		"SE331":"Vasterbottens_lan",
		"SE332":"Norrbottens_lan",
		"SEZZZ":"Extra_Regio_NUTS_3_x25",
		"SI031":"Pomurska",
		"SI032":"Podravska",
		"SI033":"Koroska",
		"SI034":"Savinjska",
		"SI035":"Zasavska",
		"SI036":"Posavska",
		"SI037":"Jugovzhodna_Slovenija",
		"SI038":"Primorsko_notranjska",
		"SI041":"Osrednjeslovenska",
		"SI042":"Gorenjska",
		"SI043":"Goriska",
		"SI044":"Obalno_kraska",
		"SIZZZ":"Extra_Regio_NUTS_3_x26",
		"SK010":"Bratislavsky_kraj",
		"SK021":"Trnavsky_kraj",
		"SK022":"Trenciansky_Kraj",
		"SK023":"Nitriansky_kraj",
		"SK031":"Zilinsky_kraj",
		"SK032":"Banskobystricky_kraj",
		"SK041":"Presovsky_kraj",
		"SK042":"Kosicky_kraj",
		"SKZZZ":"Extra_Regio_NUTS_3_x27",
		"UKC11":"Hartlepool_and_Stockton_on_Tees",
		"UKC12":"South_Teesside",
		"UKC13":"Darlington",
		"UKC14":"Durham_CC",
		"UKC21":"Northumberland",
		"UKC22":"Tyneside",
		"UKC23":"Sunderland",
		"UKD11":"West_Cumbria",
		"UKD12":"East_Cumbria",
		"UKD33":"Manchester",
		"UKD34":"Greater_Manchester_South_West",
		"UKD35":"Greater_Manchester_South_East",
		"UKD36":"Greater_Manchester_North_West",
		"UKD37":"Greater_Manchester_North_East",
		"UKD41":"Blackburn_with_Darwen",
		"UKD42":"Blackpool",
		"UKD44":"Lancaster_and_Wyre",
		"UKD45":"Mid_Lancashire",
		"UKD46":"East_Lancashire",
		"UKD47":"Chorley_and_West_Lancashire",
		"UKD61":"Warrington",
		"UKD62":"Cheshire_East",
		"UKD63":"Cheshire_West_and_Chester",
		"UKD71":"East_Merseyside",
		"UKD72":"Liverpool",
		"UKD73":"Sefton",
		"UKD74":"Wirral",
		"UKE11":"Kingston_upon_Hull_City_of",
		"UKE12":"East_Riding_of_Yorkshire",
		"UKE13":"North_and_North_East_Lincolnshire",
		"UKE21":"York",
		"UKE22":"North_Yorkshire_CC",
		"UKE31":"Barnsley_Doncaster_and_Rotherham",
		"UKE32":"Sheffield",
		"UKE41":"Bradford",
		"UKE42":"Leeds",
		"UKE44":"Calderdale_and_Kirklees",
		"UKE45":"Wakefield",
		"UKF11":"Derby",
		"UKF12":"East_Derbyshire",
		"UKF13":"South_and_West_Derbyshire",
		"UKF14":"Nottingham",
		"UKF15":"North_Nottinghamshire",
		"UKF16":"South_Nottinghamshire",
		"UKF21":"Leicester",
		"UKF22":"Leicestershire_CC_and_Rutland",
		"UKF24":"West_Northamptonshire",
		"UKF25":"North_Northamptonshire",
		"UKF30":"Lincolnshire",
		"UKG11":"Herefordshire_County_of",
		"UKG12":"Worcestershire",
		"UKG13":"Warwickshire",
		"UKG21":"Telford_and_Wrekin",
		"UKG22":"Shropshire_CC",
		"UKG23":"Stoke_on_Trent",
		"UKG24":"Staffordshire_CC",
		"UKG31":"Birmingham",
		"UKG32":"Solihull",
		"UKG33":"Coventry",
		"UKG36":"Dudley",
		"UKG37":"Sandwell",
		"UKG38":"Walsall",
		"UKG39":"Wolverhampton",
		"UKH11":"Peterborough",
		"UKH12":"Cambridgeshire_CC",
		"UKH14":"Suffolk",
		"UKH15":"Norwich_and_East_Norfolk",
		"UKH16":"North_and_West_Norfolk",
		"UKH17":"Breckland_and_South_Norfolk",
		"UKH21":"Luton",
		"UKH23":"Hertfordshire",
		"UKH24":"Bedford",
		"UKH25":"Central_Bedfordshire",
		"UKH31":"Southend_on_Sea",
		"UKH32":"Thurrock",
		"UKH34":"Essex_Haven_Gateway",
		"UKH35":"West_Essex",
		"UKH36":"Heart_of_Essex",
		"UKH37":"Essex_Thames_Gateway",
		"UKI31":"Camden_and_City_of_London",
		"UKI32":"Westminster",
		"UKI33":"Kensington_Chelsea_and_Hammersmith_Fulham",
		"UKI34":"Wandsworth",
		"UKI41":"Hackney_and_Newham",
		"UKI42":"Tower_Hamlets",
		"UKI43":"Haringey_and_Islington",
		"UKI44":"Lewisham_and_Southwark",
		"UKI45":"Lambeth",
		"UKI51":"Bexley_and_Greenwich",
		"UKI52":"Barking_Dagenham_and_Havering",
		"UKI53":"Redbridge_and_Waltham_Forest",
		"UKI54":"Enfield",
		"UKI61":"Bromley",
		"UKI62":"Croydon",
		"UKI63":"Merton_Kingston_upon_Thames_and_Sutton",
		"UKI71":"Barnet",
		"UKI72":"Brent",
		"UKI73":"Ealing",
		"UKI74":"Harrow_and_Hillingdon",
		"UKI75":"Hounslow_and_Richmond_upon_Thames",
		"UKJ11":"Berkshire",
		"UKJ12":"Milton_Keynes",
		"UKJ13":"Buckinghamshire_CC",
		"UKJ14":"Oxfordshire",
		"UKJ21":"Brighton_and_Hove",
		"UKJ22":"East_Sussex_CC",
		"UKJ25":"West_Surrey",
		"UKJ26":"East_Surrey",
		"UKJ27":"West_Sussex_South_West",
		"UKJ28":"West_Sussex_North_East",
		"UKJ31":"Portsmouth",
		"UKJ32":"Southampton",
		"UKJ34":"Isle_of_Wight",
		"UKJ35":"South_Hampshire",
		"UKJ36":"Central_Hampshire",
		"UKJ37":"North_Hampshire",
		"UKJ41":"Medway",
		"UKJ43":"Kent_Thames_Gateway",
		"UKJ44":"East_Kent",
		"UKJ45":"Mid_Kent",
		"UKJ46":"West_Kent",
		"UKK11":"Bristol_City_of",
		"UKK12":"Bath_and_North_East_Somerset_North_Somerset_and_South_Gloucestershire",
		"UKK13":"Gloucestershire",
		"UKK14":"Swindon",
		"UKK15":"Wiltshire_CC",
		"UKK21":"Bournemouth_and_Poole",
		"UKK22":"Dorset_CC",
		"UKK23":"Somerset",
		"UKK30":"Cornwall_and_Isles_of_Scilly",
		"UKK41":"Plymouth",
		"UKK42":"Torbay",
		"UKK43":"Devon_CC",
		"UKL11":"Isle_of_Anglesey",
		"UKL12":"Gwynedd",
		"UKL13":"Conwy_and_Denbighshire",
		"UKL14":"South_West_Wales",
		"UKL15":"Central_Valleys",
		"UKL16":"Gwent_Valleys",
		"UKL17":"Bridgend_and_Neath_Port_Talbot",
		"UKL18":"Swansea",
		"UKL21":"Monmouthshire_and_Newport",
		"UKL22":"Cardiff_and_Vale_of_Glamorgan",
		"UKL23":"Flintshire_and_Wrexham",
		"UKL24":"Powys",
		"UKM50":"Aberdeen_City_and_Aberdeenshire",
		"UKM61":"Caithness_Sutherland_and_Ross_Cromarty",
		"UKM62":"Inverness_Nairn_and_Moray_Badenoch_Strathspey",
		"UKM63":"Lochaber_Skye_Lochalsh_Arran_Cumbrae_and_Argyll_Bute",
		"UKM64":"Eilean_Siar_Western_Isles",
		"UKM65":"Orkney_Islands",
		"UKM66":"Shetland_Islands",
		"UKM71":"Angus_and_Dundee_City",
		"UKM72":"Clackmannanshire_and_Fife",
		"UKM73":"East_Lothian_and_Midlothian",
		"UKM75":"Edinburgh_City_of",
		"UKM76":"Falkirk",
		"UKM77":"Perth_Kinross_and_Stirling",
		"UKM78":"West_Lothian",
		"UKM81":"East_Dunbartonshire_West_Dunbartonshire_and_Helensburgh_Lomond",
		"UKM82":"Glasgow_City",
		"UKM83":"Inverclyde_East_Renfrewshire_and_Renfrewshire",
		"UKM84":"North_Lanarkshire",
		"UKM91":"Scottish_Borders",
		"UKM92":"Dumfries_Galloway",
		"UKM93":"East_Ayrshire_and_North_Ayrshire_mainland",
		"UKM94":"South_Ayrshire",
		"UKM95":"South_Lanarkshire",
		"UKN05":"West_and_South_of_Northern_Ireland",
		"UKN06":"Belfast",
		"UKN07":"Armagh_City_Banbridge_and_Craigavon",
		"UKN08":"Newry_Mourne_and_Down",
		"UKN09":"Ards_and_North_Down",
		"UKN10":"Derry_City_and_Strabane",
		"UKN11":"Mid_Ulster",
		"UKN12":"Causeway_Coast_and_Glens",
		"UKN13":"Antrim_and_Newtownabbey",
		"UKN14":"Lisburn_and_Castlereagh",
		"UKN15":"Mid_and_East_Antrim",
		"UKN16":"Fermanagh_and_Omagh",
		"UKZZZ":"Extra_Regio_NUTS_3_x28",
}

	TRRTRL_UNT = models.CharField("TRRTRL_UNT",max_length=255, choices=NUTS3_INPT_domain,default=None, blank=True, null=True, db_comment="NUTS3_INPT_domain")

	TYP_ECNMY_INPT_domain = {		"0":"Not_Applicable",
		"1":"Emerging_market_economy",
		"2":"Advanced_economy",
}

	TYP_ECNMY = models.CharField("TYP_ECNMY",max_length=255, choices=TYP_ECNMY_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_ECNMY_INPT_domain")

	TYP_PRTY_INPT_domain = {		"18":"Non_self_employed_natural_person",
		"19":"Self_employed_natural_person",
		"25":"Domestic_branch",
		"26":"Foreign_branch",
		"33":"Investment_vehicle_fund",
		"34":"Other_organisational_unit",
		"36":"Private_sector_company_other_than_corporation",
		"37":"European_Central_Bank",
		"38":"Central_Bank_that_is_not_the_European_Central_Bank",
		"5":"Other_financial_corporation",
		"6":"Central_government",
		"7":"State_and_local_government_and_Social_security_funds",
		"9":"International_organisation",
		"S11":"Non_financial_corporation",
		"S122_A":"Credit_institution",
}

	TYP_PRTY = models.CharField("TYP_PRTY",max_length=255, choices=TYP_PRTY_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_INPT_domain")

	theGRP = models.ForeignKey("GRP", models.SET_NULL,blank=True,null=True,related_name="PRTY_to_theGRPs")

	thePRTY = models.ForeignKey("PRTY", models.SET_NULL,blank=True,null=True,related_name="PRTY_to_thePRTYs")

	thePRTY1 = models.ForeignKey("PRTY", models.SET_NULL,blank=True,null=True,related_name="PRTY_to_thePRTY1s")

	class Meta:

		verbose_name = 'PRTY'

		verbose_name_plural = 'PRTYs'

class PRTY_CD(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	PRTY_CD_uniqueID = models.CharField("PRTY_CD_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTY_CD_TYP_domain = {		"1":"Legal_entity_identifier_party_code",
		"2":"Register_of_Institutions_and_Affiliates_Database_RIAD_party_code",
		"3":"Other_party_code",
}

	PRTY_CD_TYP = models.CharField("PRTY_CD_TYP",max_length=255, choices=PRTY_CD_TYP_domain,default=None, blank=True, null=True, db_comment="PRTY_CD_TYP_domain")

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	PRTY_CD = models.CharField("PRTY_CD",max_length=255,default=None, blank=True, null=True)

	thePRTY = models.ForeignKey("PRTY", models.SET_NULL,blank=True,null=True,related_name="PRTY_CD_to_thePRTYs")

	class Meta:

		verbose_name = 'PRTY_CD'

		verbose_name_plural = 'PRTY_CDs'

class PRTY_PRVS_PRD_DT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	PRTY_PRVS_PRD_DT_uniqueID = models.CharField("PRTY_PRVS_PRD_DT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	YR = models.BigIntegerField("YR",default=None, blank=True, null=True)

	SZ_CLCLTD_PRVS_PRD_domain = {		"2":"Medium_enterprise_Enterprise_qualifying_as_an_SME_but_not_as_a_small_or_micro_enterprise_in_accordance_with_the_Annex_to_Recommendation_2003_361_EC",
		"3":"Small_enterprise_Enterprise_qualifying_as_a_small_enterprise_in_accordance_with_the_Annex_to_Recommendation_2003_361_EC",
		"4":"Micro_enterprise_Enterprise_qualifying_as_a_micro_enterprise_in_accordance_with_the_Annex_to_Recommendation_2003_361_EC",
		"6":"Large_enterprise_from_input_data_Enterprise_not_qualifying_as_a_micro_small_or_medium_sized_enterprise_SME_in_accordance_with_the_Annex_to_Recommendation_2003_361_EC_as_calculated_from_input_data",
		"7":"Large_enterprise_because_of_absence_of_input_data_Enterprise_not_qualifying_as_a_micro_small_or_medium_sized_enterprise_SME_in_accordance_with_the_Annex_to_Recommendation_2003_361_EC_as_classified_because_of_absence_of_input_data",
}

	ENTRPRS_SZ_CLCLTD = models.CharField("ENTRPRS_SZ_CLCLTD",max_length=255, choices=SZ_CLCLTD_PRVS_PRD_domain,default=None, blank=True, null=True, db_comment="SZ_CLCLTD_PRVS_PRD_domain")

	thePRTY = models.ForeignKey("PRTY", models.SET_NULL,blank=True,null=True,related_name="PRTY_PRVS_PRD_DT_to_thePRTYs")

	class Meta:

		verbose_name = 'PRTY_PRVS_PRD_DT'

		verbose_name_plural = 'PRTY_PRVS_PRD_DTs'

class RPRCHS_AGRMNT_CMPNNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	RPRCHS_AGRMNT_CMPNNT_uniqueID = models.CharField("RPRCHS_AGRMNT_CMPNNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain = {		"3":"Security_leg",
		"4":"Loans_and_advances_leg",
		"5":"Equity_instrument_leg",
		"6":"Reverse_repurchase_agreement_cash_leg",
		"7":"Repurchase_agreement_cash_leg",
		"8":"Gold_collateral_leg",
}

	RPRCHS_AGRMNT_CMPNNT_TYP = models.CharField("RPRCHS_AGRMNT_CMPNNT_TYP",max_length=255, choices=RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain")

	RPRCHS_AGRMNT_INSTRMNT_ID = models.CharField("RPRCHS_AGRMNT_INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT_INPT_domain = {		"0":"Not_applicable",
		"1":"Entirely_recognised_Instrument_entirely_recognised_in_accordance_with_Implementing_Regulation_EU_No_680_2014",
		"2":"Recognised_to_the_extent_of_the_institution_s_continuing_involvement_Instrument_recognised_to_the_extent_of_the_institution_s_continuing_involvement_in_accordance_with_Implementing_Regulation_EU_No_680_2014",
		"3":"Entirely_derecognised_Instrument_entirely_derecognised_in_accordance_with_Implementing_Regulation_EU_No_680_2014",
}

	TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT = models.CharField("TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT",max_length=255, choices=TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT_INPT_domain,default=None, blank=True, null=True, db_comment="TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT_INPT_domain")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="RPRCHS_AGRMNT_CMPNNT_to_theINSTRMNTs")

	theINSTRMNT1 = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="RPRCHS_AGRMNT_CMPNNT_to_theINSTRMNT1s")

	class Meta:

		verbose_name = 'RPRCHS_AGRMNT_CMPNNT'

		verbose_name_plural = 'RPRCHS_AGRMNT_CMPNNTs'

class RSK_FAC_SA(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	RSK_FAC_SA_uniqueID = models.CharField("RSK_FAC_SA_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	RSK_FCTR_ID = models.CharField("RSK_FCTR_ID",max_length=255,default=None, blank=True, null=True)

	ISO4217_INPT_domain = {		"0":"Not_applicable",
		"AED":"UAE_Dirham",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"ARS":"Argentine_Peso",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYN":"Belarussian_Ruble",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHE":"WIR_Euro",
		"CHF":"Swiss_franc",
		"CHW":"WIR_Franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CZK":"Czech_koruna",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GTQ":"Quetzal",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"ILS":"New_Israeli_Sheqel",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MRU":"Ouguiya_x2",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDG":"Sudanese_Pound",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SRD":"Surinam_Dollar",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"STN":"Dobra_x2",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJS":"Somoni",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"USN":"US_Dollar_Next_day",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UYW":"Unidad_Previsional",
		"UZS":"Uzbekistan_Sum",
		"VEF":"Bolivar",
		"VES":"Bolivar_Soberano",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XAG":"Silver_one_Troy_ounce",
		"XAU":"Gold_one_Troy_ounce",
		"XBA":"Bond_Markets_Unit_European_Composite_Unit_EURCO",
		"XBB":"Bond_Markets_Unit_European_Monetary_Unit_E_M_U_6",
		"XBC":"Bond_Markets_Unit_European_Unit_of_Account_9_E_U_A_9",
		"XBD":"Bond_Markets_Unit_European_Unit_of_Account_17_E_U_A_17",
		"XCD":"East_Caribbean_Dollar",
		"XDR":"Special_Drawing_Rights_SDR",
		"XOF":"CFA_Franc_BCEAO",
		"XPD":"Palladium_one_Troy_ounce",
		"XPF":"CFP_Franc",
		"XPT":"Platinum_one_Troy_ounce",
		"XSU":"Sucre",
		"XTS":"Codes_specifically_reserved_for_testing_purposes",
		"XUA":"ADB_Unit_of_Account",
		"XXX":"Code_assigned_for_transactions_where_no_currency_is_involved",
		"YER":"Yemeni_Rial",
		"ZAR":"South_African_Rand",
		"ZMW":"Zambian_Kwacha",
		"ZWL":"Zimbabwe_Dollar",
}

	BS_CRRNCY = models.CharField("BS_CRRNCY",max_length=255, choices=ISO4217_INPT_domain,default=None, blank=True, null=True, db_comment="ISO4217_INPT_domain")

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	CMMDTY_TYP = models.CharField("CMMDTY_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RTNG_GRD_CRDT_QLTY_domain = {		"0":"Not_applicable",
		"1":"Senior_investment_grade",
		"2":"Non_senior_investment_grade",
		"3":"High_yield",
		"4":"Non_rated",
		"5":"Investment_grade",
}

	CRDT_SPRD_RSK_CRDT_QLTY = models.CharField("CRDT_SPRD_RSK_CRDT_QLTY",max_length=255, choices=RTNG_GRD_CRDT_QLTY_domain,default=None, blank=True, null=True, db_comment="RTNG_GRD_CRDT_QLTY_domain")

	CSR_CRV_TYP_domain = {		"0":"Not_applicable",
		"1":"Bond",
		"2":"Credit_spread_risk_CSR",
}

	CRDT_SPRD_RSK_CRV_TYP = models.CharField("CRDT_SPRD_RSK_CRV_TYP",max_length=255, choices=CSR_CRV_TYP_domain,default=None, blank=True, null=True, db_comment="CSR_CRV_TYP_domain")

	DLVRY_LCTN = models.CharField("DLVRY_LCTN",max_length=255,default=None, blank=True, null=True)

	EQUTY_FCTR_TYP_domain = {		"0":"Not_applicable",
		"1":"Spot",
		"2":"Repo",
}

	EQUTY_FCTR_TYP = models.CharField("EQUTY_FCTR_TYP",max_length=255, choices=EQUTY_FCTR_TYP_domain,default=None, blank=True, null=True, db_comment="EQUTY_FCTR_TYP_domain")

	GIRR_RSK_FCTR_domain = {		"0":"Not_applicable",
		"1":"Inflation",
		"2":"Basis",
		"3":"Yield",
}

	GIRR_FCTR_TYP = models.CharField("GIRR_FCTR_TYP",max_length=255, choices=GIRR_RSK_FCTR_domain,default=None, blank=True, null=True, db_comment="GIRR_RSK_FCTR_domain")

	RSK_CLSS_domain = {		"1":"General_interest_rate_risk_GIRR",
		"2":"Credit_spread_risk_CSR_non_securitisations",
		"3":"CSR_securitisations_non_correlation_trading_portfolio_or_non_CTP",
		"4":"CSR_securitisations_correlation_trading_portfolio_or_CTP",
		"5":"Equity_risk",
		"6":"Commodity_risk",
		"7":"Foreign_exchange_FX_risk",
}

	RSK_CLSS = models.CharField("RSK_CLSS",max_length=255, choices=RSK_CLSS_domain,default=None, blank=True, null=True, db_comment="RSK_CLSS_domain")

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="RSK_FAC_SA_to_theENTTY_RLs")

	theSCRTY_EXCHNG_TRDBL_DRVTV = models.ForeignKey("SCRTY_EXCHNG_TRDBL_DRVTV", models.SET_NULL,blank=True,null=True,related_name="RSK_FAC_SA_to_theSCRTY_EXCHNG_TRDBL_DRVTVs")

	class Meta:

		verbose_name = 'RSK_FAC_SA'

		verbose_name_plural = 'RSK_FAC_SAs'

class RTNG_AGNCY(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	RTNG_AGNCY_uniqueID = models.CharField("RTNG_AGNCY_uniqueID",max_length=255, primary_key=True)

	RTNG_AGNCY_NM = models.CharField("RTNG_AGNCY_NM",max_length=255,default=None, blank=True, null=True)

	ECAI_ECA_domain = {		"1":"ECAI",
		"2":"ECA",
}

	ECAI_ECA = models.CharField("ECAI_ECA",max_length=255, choices=ECAI_ECA_domain,default=None, blank=True, null=True, db_comment="ECAI_ECA_domain")

	class Meta:

		verbose_name = 'RTNG_AGNCY'

		verbose_name_plural = 'RTNG_AGNCYs'

class RTNG_AGNCY_EXCSS_MTHDLGY_CVRD_BND_PRGRMM_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	RTNG_AGNCY_EXCSS_MTHDLGY_CVRD_BND_PRGRMM_ASSGNMNT_uniqueID = models.CharField("RTNG_AGNCY_EXCSS_MTHDLGY_CVRD_BND_PRGRMM_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CVRD_BND_PRGRM_ID = models.CharField("CVRD_BND_PRGRM_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	RTNG_AGNCY_NM = models.CharField("RTNG_AGNCY_NM",max_length=255,default=None, blank=True, null=True)

	EXCSS_CVRG_ASST_SPCFC_VL = models.BigIntegerField("EXCSS_CVRG_ASST_SPCFC_VL",default=None, blank=True, null=True)

	EXCSS_CVRG_NML_AMNT = models.BigIntegerField("EXCSS_CVRG_NML_AMNT",default=None, blank=True, null=True)

	EXCSS_CVRG_PRSNT_VL_MRKT_VL = models.BigIntegerField("EXCSS_CVRG_PRSNT_VL_MRKT_VL",default=None, blank=True, null=True)

	RTNG_AGNCY_RNK = models.BigIntegerField("RTNG_AGNCY_RNK",default=None, blank=True, null=True)

	theCVRD_BND_PRGRM = models.ForeignKey("CVRD_BND_PRGRM", models.SET_NULL,blank=True,null=True,related_name="RTNG_AGNCY_EXCSS_MTHDLGY_CVRD_BND_PRGRMM_ASSGNMNT_to_theCVRD_BND_PRGRMs")

	theRTNG_AGNCY = models.ForeignKey("RTNG_AGNCY", models.SET_NULL,blank=True,null=True,related_name="RTNG_AGNCY_EXCSS_MTHDLGY_CVRD_BND_PRGRMM_ASSGNMNT_to_theRTNG_AGNCYs")

	class Meta:

		verbose_name = 'RTNG_AGNCY_EXCSS_MTHDLGY_CVRD_BND_PRGRMM_ASSGNMNT'

		verbose_name_plural = 'RTNG_AGNCY_EXCSS_MTHDLGY_CVRD_BND_PRGRMM_ASSGNMNTs'

class RTNG_GRD(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	RTNG_GRD_uniqueID = models.CharField("RTNG_GRD_uniqueID",max_length=255, primary_key=True)

	RTNG_AGNCY_NM = models.CharField("RTNG_AGNCY_NM",max_length=255,default=None, blank=True, null=True)

	RTNG_GRD = models.CharField("RTNG_GRD",max_length=255,default=None, blank=True, null=True)

	RTNG_SYSTM_NM = models.CharField("RTNG_SYSTM_NM",max_length=255,default=None, blank=True, null=True)

	RTNG_GRD_CRDT_QLTY_domain = {		"0":"Not_applicable",
		"1":"Senior_investment_grade",
		"2":"Non_senior_investment_grade",
		"3":"High_yield",
		"4":"Non_rated",
		"5":"Investment_grade",
}

	RTNG_GRD_CRDT_QLTY = models.CharField("RTNG_GRD_CRDT_QLTY",max_length=255, choices=RTNG_GRD_CRDT_QLTY_domain,default=None, blank=True, null=True, db_comment="RTNG_GRD_CRDT_QLTY_domain")

	TYP_RTNG_GRD_INPT_domain = {		"1":"Rating_grade_for_issue_based_rating_system",
		"3":"Rating_grade_for_issuer_based_rating_systems_for_non_Central_government",
		"4":"Rating_grade_for_issuer_based_rating_systems_for_Central_government",
}

	TYP_RTNG_GRD = models.CharField("TYP_RTNG_GRD",max_length=255, choices=TYP_RTNG_GRD_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_RTNG_GRD_INPT_domain")

	theRTNG_SYSTM = models.ForeignKey("RTNG_SYSTM", models.SET_NULL,blank=True,null=True,related_name="RTNG_GRD_to_theRTNG_SYSTMs")

	class Meta:

		verbose_name = 'RTNG_GRD'

		verbose_name_plural = 'RTNG_GRDs'

class RTNG_GRD_CNTRL_BNK_PRVT_SCTR_CMPN_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	RTNG_GRD_CNTRL_BNK_PRVT_SCTR_CMPN_ASSGNMNT_uniqueID = models.CharField("RTNG_GRD_CNTRL_BNK_PRVT_SCTR_CMPN_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	RTNG_AGNCY_NM = models.CharField("RTNG_AGNCY_NM",max_length=255,default=None, blank=True, null=True)

	RTNG_GRD = models.CharField("RTNG_GRD",max_length=255,default=None, blank=True, null=True)

	RTNG_SYSTM_NM = models.CharField("RTNG_SYSTM_NM",max_length=255,default=None, blank=True, null=True)

	thePRTY = models.ForeignKey("PRTY", models.SET_NULL,blank=True,null=True,related_name="RTNG_GRD_CNTRL_BNK_PRVT_SCTR_CMPN_ASSGNMNT_to_thePRTYs")

	theRTNG_GRD = models.ForeignKey("RTNG_GRD", models.SET_NULL,blank=True,null=True,related_name="RTNG_GRD_CNTRL_BNK_PRVT_SCTR_CMPN_ASSGNMNT_to_theRTNG_GRDs")

	class Meta:

		verbose_name = 'RTNG_GRD_CNTRL_BNK_PRVT_SCTR_CMPN_ASSGNMNT'

		verbose_name_plural = 'RTNG_GRD_CNTRL_BNK_PRVT_SCTR_CMPN_ASSGNMNTs'

class RTNG_GRD_CNTRY_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	RTNG_GRD_CNTRY_ASSGNMNT_uniqueID = models.CharField("RTNG_GRD_CNTRY_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ISO3166_domain = {		"AD":"Andorra",
		"AE":"United_Arab_Emirates_the",
		"AF":"Afghanistan",
		"AG":"Antigua_and_Barbuda",
		"AI":"Anguilla",
		"AL":"Albania",
		"AM":"Armenia",
		"AO":"Angola",
		"AQ":"Antarctica",
		"AR":"Argentina",
		"AS":"American_Samoa",
		"AT":"Austria",
		"AU":"Australia",
		"AW":"Aruba",
		"AX":"Aland_Islands",
		"AZ":"Azerbaijan",
		"BA":"Bosnia_and_Herzegovina",
		"BB":"Barbados",
		"BD":"Bangladesh",
		"BE":"Belgium",
		"BF":"Burkina_Faso",
		"BG":"Bulgaria",
		"BH":"Bahrain",
		"BI":"Burundi",
		"BJ":"Benin",
		"BL":"Saint_Barthelemy",
		"BM":"Bermuda",
		"BN":"Brunei_Darussalam",
		"BO":"Bolivia_Plurinational_State_of",
		"BQ":"Bonaire_Saint_Eustatius_and_Saba",
		"BR":"Brazil",
		"BS":"Bahamas_the",
		"BT":"Bhutan",
		"BV":"Bouvet_Island",
		"BW":"Botswana",
		"BY":"Belarus",
		"BZ":"Belize",
		"CA":"Canada",
		"CC":"Cocos_Keeling_Islands_the",
		"CD":"Congo_the_Democratic_Republic_of_the",
		"CF":"Central_African_Republic_the",
		"CG":"Congo_the",
		"CH":"Switzerland",
		"CI":"Cote_d_Ivoire",
		"CK":"Cook_Islands_the",
		"CL":"Chile",
		"CM":"Cameroon",
		"CN":"China_China_excluding_Taiwan_TW_Hong_Kong_HK_Macao_MO",
		"CO":"Colombia",
		"CR":"Costa_Rica",
		"CU":"Cuba",
		"CV":"Cabo_Verde",
		"CW":"Curacao",
		"CX":"Christmas_Island",
		"CY":"Cyprus",
		"CZ":"Czechia",
		"DE":"Germany",
		"DJ":"Djibouti",
		"DK":"Denmark",
		"DM":"Dominica",
		"DO":"Dominican_Republic_the",
		"DZ":"Algeria",
		"EC":"Ecuador",
		"EE":"Estonia",
		"EG":"Egypt",
		"EH":"Western_Sahara",
		"ER":"Eritrea",
		"ES":"Spain",
		"ET":"Ethiopia",
		"FI":"Finland_Finland_excluding_Aland_AX",
		"FJ":"Fiji",
		"FK":"Falkland_Islands_the_Malvinas",
		"FM":"Micronesia_Federated_States_of",
		"FO":"Faroe_Islands_the",
		"FR":"France_France_excluding_Guadeloupe_GP_Guyane_GF_La_Reunion_RE_Martinique_MQ_Mayotte_YT_Nouvelle_Caledonie_NC_Polynesie_francaise_PF_Saint_Barthelemy_BL_Saint_Martin_MF_Saint_Pierre_et_Miquelon_PM_Terres_australes_francaises_TF_Wallis_et_Futuna_WF",
		"GA":"Gabon",
		"GB":"United_Kingdom_of_Great_Britain_and_Northern_Ireland_the",
		"GD":"Grenada",
		"GE":"Georgia",
		"GF":"French_Guiana",
		"GG":"Guernsey",
		"GH":"Ghana",
		"GI":"Gibraltar",
		"GL":"Greenland",
		"GM":"Gambia_the",
		"GN":"Guinea",
		"GP":"Guadeloupe",
		"GQ":"Equatorial_Guinea",
		"GR":"Greece",
		"GS":"South_Georgia_and_the_South_Sandwich_Islands",
		"GT":"Guatemala",
		"GU":"Guam",
		"GW":"Guinea_Bissau",
		"GY":"Guyana",
		"HK":"Hong_Kong",
		"HM":"Heard_Island_and_McDonald_Islands",
		"HN":"Honduras",
		"HR":"Croatia",
		"HT":"Haiti",
		"HU":"Hungary",
		"ID":"Indonesia",
		"IE":"Ireland",
		"IL":"Israel",
		"IM":"Isle_of_Man",
		"IN":"India",
		"IO":"British_Indian_Ocean_Territory_the",
		"IQ":"Iraq",
		"IR":"Iran_Islamic_Republic_of",
		"IS":"Iceland",
		"IT":"Italy",
		"JE":"Jersey",
		"JM":"Jamaica",
		"JO":"Jordan",
		"JP":"Japan",
		"KE":"Kenya",
		"KG":"Kyrgyzstan",
		"KH":"Cambodia",
		"KI":"Kiribati",
		"KM":"Comoros_the",
		"KN":"Saint_Kitts_and_Nevis",
		"KP":"Korea_the_Democratic_People_s_Republic_of",
		"KR":"Korea_the_Republic_of",
		"KW":"Kuwait",
		"KY":"Cayman_Islands_the",
		"KZ":"Kazakhstan",
		"LA":"Lao_People_s_Democratic_Republic_the",
		"LB":"Lebanon",
		"LC":"Saint_Lucia",
		"LI":"Liechtenstein",
		"LK":"Sri_Lanka",
		"LR":"Liberia",
		"LS":"Lesotho",
		"LT":"Lithuania",
		"LU":"Luxembourg",
		"LV":"Latvia",
		"LY":"Libya",
		"MA":"Morocco",
		"MC":"Monaco",
		"MD":"Moldova_the_Republic_of",
		"ME":"Montenegro",
		"MF":"Saint_Martin_French_part",
		"MG":"Madagascar",
		"MH":"Marshall_Islands_the",
		"MK":"Macedonia_the_former_Yugoslav_Republic_of",
		"ML":"Mali",
		"MM":"Myanmar",
		"MN":"Mongolia",
		"MO":"Macao",
		"MP":"Northern_Mariana_Islands_the",
		"MQ":"Martinique",
		"MR":"Mauritania",
		"MS":"Montserrat",
		"MT":"Malta",
		"MU":"Mauritius",
		"MV":"Maldives",
		"MW":"Malawi",
		"MX":"Mexico",
		"MY":"Malaysia",
		"MZ":"Mozambique",
		"NA":"Namibia",
		"NC":"New_Caledonia",
		"NE":"Niger_the",
		"NF":"Norfolk_Island",
		"NG":"Nigeria",
		"NI":"Nicaragua",
		"NL":"Netherlands_the_Netherlands_excluding_Aruba_AW_Bonaire_Saint_Eustatius_and_Saba_BQ_Curacao_CW_Sint_Maarten_SX",
		"NO":"Norway_Norway_excluding_Svalbard_and_Jan_Mayen_SJ",
		"NP":"Nepal",
		"NR":"Nauru",
		"NU":"Niue",
		"NZ":"New_Zealand",
		"OM":"Oman",
		"PA":"Panama",
		"PE":"Peru",
		"PF":"French_Polynesia",
		"PG":"Papua_New_Guinea",
		"PH":"Philippines_the",
		"PK":"Pakistan",
		"PL":"Poland",
		"PM":"Saint_Pierre_and_Miquelon",
		"PN":"Pitcairn",
		"PR":"Puerto_Rico",
		"PS":"Palestine_State_of",
		"PT":"Portugal",
		"PW":"Palau",
		"PY":"Paraguay",
		"QA":"Qatar",
		"RE":"Reunion",
		"RO":"Romania",
		"RS":"Serbia",
		"RU":"Russian_Federation_the",
		"RW":"Rwanda",
		"SA":"Saudi_Arabia",
		"SB":"Solomon_Islands",
		"SC":"Seychelles",
		"SD":"Sudan_the",
		"SE":"Sweden",
		"SG":"Singapore",
		"SH":"Saint_Helena_Ascension_and_Tristan_da_Cunha",
		"SI":"Slovenia",
		"SJ":"Svalbard_and_Jan_Mayen",
		"SK":"Slovakia",
		"SL":"Sierra_Leone",
		"SM":"San_Marino",
		"SN":"Senegal",
		"SO":"Somalia",
		"SR":"Suriname",
		"SS":"South_Sudan",
		"ST":"Sao_Tome_and_Principe",
		"SV":"El_Salvador",
		"SX":"Sint_Maarten_Dutch_part",
		"SY":"Syrian_Arab_Republic",
		"SZ":"Swaziland",
		"TC":"Turks_and_Caicos_Islands_the",
		"TD":"Chad",
		"TF":"French_Southern_Territories_the",
		"TG":"Togo",
		"TH":"Thailand",
		"TJ":"Tajikistan",
		"TK":"Tokelau",
		"TL":"Timor_Leste",
		"TM":"Turkmenistan",
		"TN":"Tunisia",
		"TO":"Tonga",
		"TR":"Turkey",
		"TT":"Trinidad_and_Tobago",
		"TV":"Tuvalu",
		"TW":"Taiwan_Province_of_China",
		"TZ":"Tanzania_United_Republic_of",
		"UA":"Ukraine",
		"UG":"Uganda",
		"UM":"United_States_Minor_Outlying_Islands_the",
		"US":"United_States_of_America_the_United_States_excluding_American_Samoa_AS_Guam_GU_Northern_Mariana_Islands_MP_Puerto_Rico_PR_United_States_Minor_Outlying_Islands_UM_Virgin_Islands_U_S_VI",
		"UY":"Uruguay",
		"UZ":"Uzbekistan",
		"VA":"Holy_See_the",
		"VC":"Saint_Vincent_and_the_Grenadines",
		"VE":"Venezuela_Bolivarian_Republic_of",
		"VG":"Virgin_Islands_British",
		"VI":"Virgin_Islands_U_S",
		"VN":"Viet_Nam",
		"VU":"Vanuatu",
		"WF":"Wallis_and_Futuna",
		"WS":"Samoa",
		"YE":"Yemen",
		"YT":"Mayotte",
		"ZA":"South_Africa",
		"ZM":"Zambia",
		"ZW":"Zimbabwe",
}

	CNTRY_CD = models.CharField("CNTRY_CD",max_length=255, choices=ISO3166_domain,default=None, blank=True, null=True, db_comment="ISO3166_domain")

	RTNG_AGNCY_NM = models.CharField("RTNG_AGNCY_NM",max_length=255,default=None, blank=True, null=True)

	RTNG_GRD = models.CharField("RTNG_GRD",max_length=255,default=None, blank=True, null=True)

	RTNG_SYSTM_NM = models.CharField("RTNG_SYSTM_NM",max_length=255,default=None, blank=True, null=True)

	theRTNG_GRD = models.ForeignKey("RTNG_GRD", models.SET_NULL,blank=True,null=True,related_name="RTNG_GRD_CNTRY_ASSGNMNT_to_theRTNG_GRDs")

	class Meta:

		verbose_name = 'RTNG_GRD_CNTRY_ASSGNMNT'

		verbose_name_plural = 'RTNG_GRD_CNTRY_ASSGNMNTs'

class RTNG_GRD_ISS_BSD_RTNG_SSTM_DBT_SCRTY_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	RTNG_GRD_ISS_BSD_RTNG_SSTM_DBT_SCRTY_ASSGNMNT_uniqueID = models.CharField("RTNG_GRD_ISS_BSD_RTNG_SSTM_DBT_SCRTY_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	RTNG_AGNCY_NM = models.CharField("RTNG_AGNCY_NM",max_length=255,default=None, blank=True, null=True)

	RTNG_GRD = models.CharField("RTNG_GRD",max_length=255,default=None, blank=True, null=True)

	RTNG_SYSTM_NM = models.CharField("RTNG_SYSTM_NM",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	theRTNG_GRD = models.ForeignKey("RTNG_GRD", models.SET_NULL,blank=True,null=True,related_name="RTNG_GRD_ISS_BSD_RTNG_SSTM_DBT_SCRTY_ASSGNMNT_to_theRTNG_GRDs")

	theSCRTY_EXCHNG_TRDBL_DRVTV = models.ForeignKey("SCRTY_EXCHNG_TRDBL_DRVTV", models.SET_NULL,blank=True,null=True,related_name="RTNG_GRD_ISS_BSD_RTNG_SSTM_DBT_SCRTY_ASSGNMNT_to_theSCRTY_EXCHNG_TRDBL_DRVTVs")

	class Meta:

		verbose_name = 'RTNG_GRD_ISS_BSD_RTNG_SSTM_DBT_SCRTY_ASSGNMNT'

		verbose_name_plural = 'RTNG_GRD_ISS_BSD_RTNG_SSTM_DBT_SCRTY_ASSGNMNTs'

class RTNG_SYSTM(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	RTNG_SYSTM_uniqueID = models.CharField("RTNG_SYSTM_uniqueID",max_length=255, primary_key=True)

	RTNG_AGNCY_NM = models.CharField("RTNG_AGNCY_NM",max_length=255,default=None, blank=True, null=True)

	RTNG_SYSTM_NM = models.CharField("RTNG_SYSTM_NM",max_length=255,default=None, blank=True, null=True)

	RTN_SYSTM_TYP_NTR_domain = {		"5":"Graded_Rating_System",
		"6":"Numeric_rating_system",
}

	RTNG_SYSTM_TYP_BY_NTR = models.CharField("RTNG_SYSTM_TYP_BY_NTR",max_length=255, choices=RTN_SYSTM_TYP_NTR_domain,default=None, blank=True, null=True, db_comment="RTN_SYSTM_TYP_NTR_domain")

	SHRT_TRM_CRDT_ASSMNT_INDCTR_domain = {		"1":"Short_term_credit_assessment",
		"2":"Not_short_term_credit_assessment",
}

	SHRT_TRM_CRDT_ASSSSMNT_INDCTR = models.CharField("SHRT_TRM_CRDT_ASSSSMNT_INDCTR",max_length=255, choices=SHRT_TRM_CRDT_ASSMNT_INDCTR_domain,default=None, blank=True, null=True, db_comment="SHRT_TRM_CRDT_ASSMNT_INDCTR_domain")

	RTNG_SYSTM_TYP_TRGT_INPT_domain = {		"1":"Issue_based_rating_system",
		"3":"Central_government_rating_system",
		"4":"Non_Central_government_rating_system",
}

	TYP_RTNG_SYSTM = models.CharField("TYP_RTNG_SYSTM",max_length=255, choices=RTNG_SYSTM_TYP_TRGT_INPT_domain,default=None, blank=True, null=True, db_comment="RTNG_SYSTM_TYP_TRGT_INPT_domain")

	theRTNG_AGNCY = models.ForeignKey("RTNG_AGNCY", models.SET_NULL,blank=True,null=True,related_name="RTNG_SYSTM_to_theRTNG_AGNCYs")

	class Meta:

		verbose_name = 'RTNG_SYSTM'

		verbose_name_plural = 'RTNG_SYSTMs'

class RTNG_SYSTM_APPLD_LGL_PRSN(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	RTNG_SYSTM_APPLD_LGL_PRSN_uniqueID = models.CharField("RTNG_SYSTM_APPLD_LGL_PRSN_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	RTNG_AGNCY_NM = models.CharField("RTNG_AGNCY_NM",max_length=255,default=None, blank=True, null=True)

	RTNG_SYSTM_NM = models.CharField("RTNG_SYSTM_NM",max_length=255,default=None, blank=True, null=True)

	PD = models.FloatField("PD",default=None, blank=True, null=True)

	thePRTY = models.ForeignKey("PRTY", models.SET_NULL,blank=True,null=True,related_name="RTNG_SYSTM_APPLD_LGL_PRSN_to_thePRTYs")

	theRTNG_SYSTM = models.ForeignKey("RTNG_SYSTM", models.SET_NULL,blank=True,null=True,related_name="RTNG_SYSTM_APPLD_LGL_PRSN_to_theRTNG_SYSTMs")

	class Meta:

		verbose_name = 'RTNG_SYSTM_APPLD_LGL_PRSN'

		verbose_name_plural = 'RTNG_SYSTM_APPLD_LGL_PRSNs'

class SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT_uniqueID = models.CharField("SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	GRP_ID = models.CharField("GRP_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	OTHR_ORGNSTN_RL_TYP = models.CharField("OTHR_ORGNSTN_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ACCMLTD_EQT_INTRST = models.FloatField("ACCMLTD_EQT_INTRST",default=None, blank=True, null=True)

	CNSLDTN_MTHD_FLL_domain = {		"1":"Full_consolidation",
		"2":"Proportional_consolidation",
		"3":"Equity_method",
		"4":"Other_than_Full_consolidation_Proportional_consolidation_Equity_method",
}

	ACCNTNG_TRTMNT_CRR = models.CharField("ACCNTNG_TRTMNT_CRR",max_length=255, choices=CNSLDTN_MTHD_FLL_domain,default=None, blank=True, null=True, db_comment="CNSLDTN_MTHD_FLL_domain")

	CNSLDTN_MTHD_FLL_domain = {		"1":"Full_consolidation",
		"2":"Proportional_consolidation",
		"3":"Equity_method",
		"4":"Other_than_Full_consolidation_Proportional_consolidation_Equity_method",
}

	ACCNTNG_TRTMNT_IFRS = models.CharField("ACCNTNG_TRTMNT_IFRS",max_length=255, choices=CNSLDTN_MTHD_FLL_domain,default=None, blank=True, null=True, db_comment="CNSLDTN_MTHD_FLL_domain")

	ACQSTN_CST = models.BigIntegerField("ACQSTN_CST",default=None, blank=True, null=True)

	CRRYNG_AMNT = models.BigIntegerField("CRRYNG_AMNT",default=None, blank=True, null=True)

	DT_ENTRY = models.DateTimeField("DT_ENTRY",default=None, blank=True, null=True)

	FV_INVSTMNTS_PBLSHD_PRC_QTTNS = models.BigIntegerField("FV_INVSTMNTS_PBLSHD_PRC_QTTNS",default=None, blank=True, null=True)

	GDWLL_INVST = models.BigIntegerField("GDWLL_INVST",default=None, blank=True, null=True)

	SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT_TYP_domain = {		"1":"Subsidiary_joint_venture_and_associate_Subsidiary_assignment",
		"2":"Subsidiary_joint_venture_and_associate_Joint_venture_assignment",
		"3":"Subsidiary_joint_venture_and_associate_Associate_assignment",
}

	SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT_TYP = models.CharField("SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT_TYP",max_length=255, choices=SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT_TYP_domain")

	VTNG_RGHT = models.FloatField("VTNG_RGHT",default=None, blank=True, null=True)

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT_to_theENTTY_RLs")

	theGRP = models.ForeignKey("GRP", models.SET_NULL,blank=True,null=True,related_name="SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT_to_theGRPs")

	class Meta:

		verbose_name = 'SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT'

		verbose_name_plural = 'SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNTs'

class SCRTY_BRRWNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SCRTY_BRRWNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT_uniqueID = models.CharField("SCRTY_BRRWNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	theCLLTRL = models.ForeignKey("CLLTRL", models.SET_NULL,blank=True,null=True,related_name="SCRTY_BRRWNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT_to_theCLLTRLs")

	theSCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL = models.ForeignKey("SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL", models.SET_NULL,blank=True,null=True,related_name="SCRTY_BRRWNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT_to_theSCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRLs")

	class Meta:

		verbose_name = 'SCRTY_BRRWNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT'

		verbose_name_plural = 'SCRTY_BRRWNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNTs'

class SCRTY_CLLTRL_LNDNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SCRTY_CLLTRL_LNDNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT_uniqueID = models.CharField("SCRTY_CLLTRL_LNDNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	theCLLTRL = models.ForeignKey("CLLTRL", models.SET_NULL,blank=True,null=True,related_name="SCRTY_CLLTRL_LNDNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT_to_theCLLTRLs")

	theSCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL = models.ForeignKey("SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL", models.SET_NULL,blank=True,null=True,related_name="SCRTY_CLLTRL_LNDNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT_to_theSCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRLs")

	class Meta:

		verbose_name = 'SCRTY_CLLTRL_LNDNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNT'

		verbose_name_plural = 'SCRTY_CLLTRL_LNDNG_CMPNNT_SCRTY_CLLTRL_ASSGNMNTs'

class SCRTY_ENTTY_RL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SCRTY_ENTTY_RL_ASSGNMNT_uniqueID = models.CharField("SCRTY_ENTTY_RL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	PRTY_ID = models.CharField("PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	PRTY_RL_TYP = models.CharField("PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ENTTY_RL_ASSGNMNT_TYP_domain = {		"1":"Debt_security_Debtor_assignment",
		"2":"Security_Issuer_assignment",
}

	SCRTY_ENTTY_RL_ASSGNMNT_TYP = models.CharField("SCRTY_ENTTY_RL_ASSGNMNT_TYP",max_length=255, choices=SCRTY_ENTTY_RL_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="SCRTY_ENTTY_RL_ASSGNMNT_TYP_domain")

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="SCRTY_ENTTY_RL_ASSGNMNT_to_theENTTY_RLs")

	theSCRTY_EXCHNG_TRDBL_DRVTV = models.ForeignKey("SCRTY_EXCHNG_TRDBL_DRVTV", models.SET_NULL,blank=True,null=True,related_name="SCRTY_ENTTY_RL_ASSGNMNT_to_theSCRTY_EXCHNG_TRDBL_DRVTVs")

	class Meta:

		verbose_name = 'SCRTY_ENTTY_RL_ASSGNMNT'

		verbose_name_plural = 'SCRTY_ENTTY_RL_ASSGNMNTs'

class SCRTY_EXCHNG_TRDBL_DRVTV(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SCRTY_EXCHNG_TRDBL_DRVTV_uniqueID = models.CharField("SCRTY_EXCHNG_TRDBL_DRVTV_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	ACCRD_INTRST_MRKT_VL_INDCTR_SHSG4_ISIN_ACCRD_INTRST_MRKT_VL_INDCTR_REF_domain = {		"1":"Accrued_interests_for_market_values",
		"2":"Not_accrued_interests_for_market_values",
}

	ACCRD_INTRST_MRKT_VL_INDCTR = models.CharField("ACCRD_INTRST_MRKT_VL_INDCTR",max_length=255, choices=ACCRD_INTRST_MRKT_VL_INDCTR_SHSG4_ISIN_ACCRD_INTRST_MRKT_VL_INDCTR_REF_domain,default=None, blank=True, null=True, db_comment="ACCRD_INTRST_MRKT_VL_INDCTR_SHSG4_ISIN_ACCRD_INTRST_MRKT_VL_INDCTR_REF_domain")

	RSDL_MTRTY_BND_domain = {		"12":"_3m_6m",
		"16":"_6m_12m",
		"21":"_1y_2y",
		"28":"_2y_3y",
		"3":"_1d_1w",
		"31":"_3y_5y",
		"36":"_5y_10y",
		"40":"Over_10_years",
		"64":"_0d_1d",
		"81":"_gt_7_days_lt_eq_14_days",
		"82":"_gt_2_weeks_lt_eq_1_month",
		"9":"_1m_3m",
		"999":"Open_maturity",
}

	ASST_ENCMBRNC_RSDL_MTRTY_BND = models.CharField("ASST_ENCMBRNC_RSDL_MTRTY_BND",max_length=255, choices=RSDL_MTRTY_BND_domain,default=None, blank=True, null=True, db_comment="RSDL_MTRTY_BND_domain")

	ISO4217_domain = {		"AED":"UAE_Dirham",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"ARS":"Argentine_Peso",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYN":"Belarussian_Ruble",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHE":"WIR_Euro",
		"CHF":"Swiss_franc",
		"CHW":"WIR_Franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CZK":"Czech_koruna",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GTQ":"Quetzal",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"ILS":"New_Israeli_Sheqel",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MRU":"Ouguiya_x2",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDG":"Sudanese_Pound",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SRD":"Surinam_Dollar",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"STN":"Dobra_x2",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJS":"Somoni",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"USN":"US_Dollar_Next_day",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UYW":"Unidad_Previsional",
		"UZS":"Uzbekistan_Sum",
		"VEF":"Bolivar",
		"VES":"Bolivar_Soberano",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XAG":"Silver_one_Troy_ounce",
		"XAU":"Gold_one_Troy_ounce",
		"XBA":"Bond_Markets_Unit_European_Composite_Unit_EURCO",
		"XBB":"Bond_Markets_Unit_European_Monetary_Unit_E_M_U_6",
		"XBC":"Bond_Markets_Unit_European_Unit_of_Account_9_E_U_A_9",
		"XBD":"Bond_Markets_Unit_European_Unit_of_Account_17_E_U_A_17",
		"XCD":"East_Caribbean_Dollar",
		"XDR":"Special_Drawing_Rights_SDR",
		"XOF":"CFA_Franc_BCEAO",
		"XPD":"Palladium_one_Troy_ounce",
		"XPF":"CFP_Franc",
		"XPT":"Platinum_one_Troy_ounce",
		"XSU":"Sucre",
		"XTS":"Codes_specifically_reserved_for_testing_purposes",
		"XUA":"ADB_Unit_of_Account",
		"XXX":"Code_assigned_for_transactions_where_no_currency_is_involved",
		"YER":"Yemeni_Rial",
		"ZAR":"South_African_Rand",
		"ZMW":"Zambian_Kwacha",
		"ZWL":"Zimbabwe_Dollar",
}

	CRRNCY = models.CharField("CRRNCY",max_length=255, choices=ISO4217_domain,default=None, blank=True, null=True, db_comment="ISO4217_domain")

	CRRNCY_SHSG4_ISIN_1_CRRNCY_TRNSCTN_RPRTD_REF_domain = {		"ADF":"Andorran_Franc_1_1_peg_to_the_French_franc",
		"ADP":"Andorran_Peseta_1_1_peg_to_the_Spanish_peseta",
		"AED":"UAE_Dirham",
		"AFA":"Afghanistan_afghani_old",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"AON":"Angolan_kwanza_old",
		"AOR":"Angolan_kwanza_reajustado",
		"ARS":"Argentine_Peso",
		"ATS":"Austrian_schilling",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZM":"Azerbaijanian_manat_old",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BEF":"Belgian_franc",
		"BEL":"Belgian_franc_financial",
		"BGL":"Bulgarian_lev_A_99",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYB":"Belarussian_rouble_old",
		"BYR":"Belarus_Rubles",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHF":"Swiss_franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CSD":"Serbian_dinar_old",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CYP":"Cyprus_pound",
		"CZK":"Czech_koruna",
		"DEM":"German_mark",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"ECS":"Ecuador_sucre",
		"EEK":"Estonian_kroon",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ESP":"Spanish_peseta",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FIM":"Finnish_markka",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"FRF":"French_franc",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GGP":"Guernsey_Pounds",
		"GHC":"Ghanaian_cedi_old",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GRD":"Greek_drachma",
		"GTQ":"Quetzal",
		"GWP":"Guinea_Bissau_Peso",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HKQ":"Hong_Kong_dollar_old",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"IEP":"Irish_pound",
		"ILS":"New_Israeli_Sheqel",
		"IMP":"Isle_of_Man_Pounds",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"ITL":"Italian_lira",
		"JEP":"Jersey_Pounds",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LTL":"Lithuanian_litas",
		"LUF":"Luxembourg_franc",
		"LVL":"Latvian_lats",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MGF":"Malagasy_franc",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MTL":"Maltese_lira",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXP":"Mexican_peso_old",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZM":"Mozambique_metical_old",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NLG":"Netherlands_guilder",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PLZ":"Polish_zloty_old",
		"PTE":"Portugese_escudo",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"ROL":"Romanian_leu_old",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RUR":"Russian_ruble_old",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDD":"Sudanese_dinar",
		"SDG":"Sudanese_Pound",
		"SDP":"Sudanese_pound_old",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SIT":"Slovenian_tolar",
		"SKK":"Slovak_koruna",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SPL":"Seborga_Luigini",
		"SRD":"Surinam_Dollar",
		"SRG":"Suriname_guilder",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJR":"Tajikistan_rouble",
		"TJS":"Somoni",
		"TMM":"Turkmenistan_manat",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TPE":"East_Timor_escudo",
		"TRL":"Turkish_lira_old",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TVD":"Tuvalu_Tuvalu_Dollars",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UZS":"Uzbekistan_Sum",
		"VEB":"Venezuela_bolivar",
		"VEF":"Bolivar",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XCD":"East_Caribbean_Dollar",
		"XEU":"European_Currency_Unit_E_C_U",
		"XOF":"CFA_Franc_BCEAO",
		"XPF":"CFP_Franc",
		"XSU":"Sucre",
		"YER":"Yemeni_Rial",
		"YUM":"Yugoslav_dinar",
		"ZAR":"South_African_Rand",
		"ZMK":"Zambian_Kwacha",
		"ZMW":"Zambian_Kwacha_x2",
		"ZWD":"Zimbabwe_dollar",
		"ZWL":"Zimbabwe_Dollar_x2",
		"ZWN":"Zimbabwe_dollars_old",
		"ZWR":"Third_Zimbabwe_dollar",
}

	CRRNCY_TRNSCTN_RPRTD = models.CharField("CRRNCY_TRNSCTN_RPRTD",max_length=255, choices=CRRNCY_SHSG4_ISIN_1_CRRNCY_TRNSCTN_RPRTD_REF_domain,default=None, blank=True, null=True, db_comment="CRRNCY_SHSG4_ISIN_1_CRRNCY_TRNSCTN_RPRTD_REF_domain")

	DBT_SCRTY_ACCNTNG_STNDRD_TYP_INPT_domain = {		"0":"Not_applicable",
		"21":"Debt_security_for_international_financial_reporting_standard_IFRS",
		"22":"Debt_security_for_national_general_accepted_accounting_principles_nGAAP",
}

	DBT_SCRTY_ACCNTNG_STNDRD = models.CharField("DBT_SCRTY_ACCNTNG_STNDRD",max_length=255, choices=DBT_SCRTY_ACCNTNG_STNDRD_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="DBT_SCRTY_ACCNTNG_STNDRD_TYP_INPT_domain")

	DBT_SCRTY_PRFRMNG_STTS_TYP_INPT_domain = {		"0":"Not_applicable",
		"19":"Performing_debt_security",
		"20":"Non_performing_debt_security",
}

	DBT_SCRTY_PRFRMNG_STTS_TYP = models.CharField("DBT_SCRTY_PRFRMNG_STTS_TYP",max_length=255, choices=DBT_SCRTY_PRFRMNG_STTS_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="DBT_SCRTY_PRFRMNG_STTS_TYP_INPT_domain")

	DT_ISS = models.DateTimeField("DT_ISS",default=None, blank=True, null=True)

	DT_LGL_FNL_MTRTY = models.DateTimeField("DT_LGL_FNL_MTRTY",default=None, blank=True, null=True)

	DT_PRFRMNG_STTS = models.DateTimeField("DT_PRFRMNG_STTS",default=None, blank=True, null=True)

	DT_PST_D = models.DateTimeField("DT_PST_D",default=None, blank=True, null=True)

	DT_SCRTY_STTS = models.DateTimeField("DT_SCRTY_STTS",default=None, blank=True, null=True)

	ELGBL_CNTRL_BNK_FNDNG_INPT_domain = {		"0":"Not_applicable_To_be_used_if_central_bank_eligibility_does_not_apply",
		"1":"Eligible_for_central_bank_funding_Specifies_if_an_object_is_eligible_for_central_bank_funding_in_the_sense_that_it_might_be_exchanged_provided_as_collateral_for_funding",
		"2":"Not_elibible_for_central_bank_funding_Specifies_if_an_object_is_not_eligible_for_central_bank_funding",
}

	ELGBL_CNTRL_BNK_FNDNG = models.CharField("ELGBL_CNTRL_BNK_FNDNG",max_length=255, choices=ELGBL_CNTRL_BNK_FNDNG_INPT_domain,default=None, blank=True, null=True, db_comment="ELGBL_CNTRL_BNK_FNDNG_INPT_domain")

	ERLY_RDMPTN_INCLSN_INDCTR_SHSG4_ISIN_ERLY_RDMPTN_INCLSN_INDCTR_REF_domain = {		"1":"Early_redemptions_included",
		"2":"Not_early_redemptions_included",
}

	ERLY_RDMPTN_INCLSN_INDCTR = models.CharField("ERLY_RDMPTN_INCLSN_INDCTR",max_length=255, choices=ERLY_RDMPTN_INCLSN_INDCTR_SHSG4_ISIN_ERLY_RDMPTN_INCLSN_INDCTR_REF_domain,default=None, blank=True, null=True, db_comment="ERLY_RDMPTN_INCLSN_INDCTR_SHSG4_ISIN_ERLY_RDMPTN_INCLSN_INDCTR_REF_domain")

	EXPSR_CLSS_CLCLTN_INPT_domain = {		"0":"Not_applicable",
		"1":"SA_Equity_exposures",
		"10":"SA_Exposures_to_international_organisations",
		"11":"SA_Exposures_to_multilateral_development_banks",
		"12":"SA_Exposures_to_public_sector_entities",
		"13":"SA_Exposures_to_regional_governments_or_local_authorities",
		"14":"SA_Items_associated_with_a_particular_high_risk",
		"16":"SA_Other_items",
		"2":"SA_Exposures_in_default",
		"3":"SA_Exposures_in_the_form_of_covered_bonds",
		"4":"SA_Exposures_in_the_form_of_units_or_shares_in_CIUs",
		"6":"SA_Exposures_to_central_governments_or_central_banks",
		"7":"SA_Exposures_to_corporates_without_a_short_term_credit_assessment",
		"8":"SA_Exposures_to_institutions_and_corporates_with_a_short_term_credit_assessment",
		"9":"SA_Exposures_to_institutions_without_a_short_term_credit_assessment",
}

	EXPSR_CLSS = models.CharField("EXPSR_CLSS",max_length=255, choices=EXPSR_CLSS_CLCLTN_INPT_domain,default=None, blank=True, null=True, db_comment="EXPSR_CLSS_CLCLTN_INPT_domain")

	FRBRNC_MSR_CNT = models.BigIntegerField("FRBRNC_MSR_CNT",default=None, blank=True, null=True)

	HQLA_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"High_liquidity_and_credit_quality_HQLA",
		"2":"Not_high_liquidity_and_credit_quality_HQLA",
}

	HQLA_INDCTR = models.CharField("HQLA_INDCTR",max_length=255, choices=HQLA_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="HQLA_INDCTR_INPT_domain")

	IDNTFR_TYP_domain = {		"0":"Not_applicable",
		"CUSIP":"CUSIP",
		"INTERNAL_CODE":"Internal_Code",
		"SEDOL":"SEDOL",
}

	IDNTFR_TYP = models.CharField("IDNTFR_TYP",max_length=255, choices=IDNTFR_TYP_domain,default=None, blank=True, null=True, db_comment="IDNTFR_TYP_domain")

	LST_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"F":"Non_listed",
		"T":"Listed",
}

	IS_LSTD = models.CharField("IS_LSTD",max_length=255, choices=LST_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="LST_INDCTR_INPT_domain")

	ISIN = models.CharField("ISIN",max_length=255,default=None, blank=True, null=True)

	LW_CRDT_RSK_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Low_credit_risk_instrument",
		"2":"Non_low_credit_risk_instrument",
}

	LW_CRDT_RSK_INDCTR = models.CharField("LW_CRDT_RSK_INDCTR",max_length=255, choices=LW_CRDT_RSK_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="LW_CRDT_RSK_INDCTR_INPT_domain")

	MLTPL_FRBRNC_MSR_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Multiple_forbearance_measures_in_place",
		"2":"Not_multiple_forbearance_measures_in_place",
}

	MLTPL_FRBRNC_MSRS_INDCTR = models.CharField("MLTPL_FRBRNC_MSRS_INDCTR",max_length=255, choices=MLTPL_FRBRNC_MSR_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="MLTPL_FRBRNC_MSR_INDCTR_INPT_domain")

	NGTBL_SCRTY_domain = {		"0":"Not_applicable",
		"1":"Negotiable_security",
		"2":"Non_negotiable_security",
}

	NGTBL_SCRTY_INDCTR = models.CharField("NGTBL_SCRTY_INDCTR",max_length=255, choices=NGTBL_SCRTY_domain,default=None, blank=True, null=True, db_comment="NGTBL_SCRTY_domain")

	NN_PRFRMNG_EXT_CRTR_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Failed_to_meet_the_non_performing_exit_criteria",
		"2":"Still_able_to_meet_the_non_performing_exit_criteria",
}

	NN_PRFRMNG_EXT_CRTR_MT_INDCTR = models.CharField("NN_PRFRMNG_EXT_CRTR_MT_INDCTR",max_length=255, choices=NN_PRFRMNG_EXT_CRTR_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="NN_PRFRMNG_EXT_CRTR_INDCTR_INPT_domain")

	OFFCL_SCRTY_ID = models.CharField("OFFCL_SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	TM_INTRVL_SHSG4_NON_ISIN_1_ORGNL_MTRTY_INTRVL_REF_domain = {		"20":"Up_to_1_year",
		"25":"Over_1_year",
		"83":"Any_value_from_the_input_layer_The_member_is_used_for_mapping_purposes_to_represent_any_possible_value_from_the_input_layer",
}

	ORGNL_MTRTY_INTRVL = models.CharField("ORGNL_MTRTY_INTRVL",max_length=255, choices=TM_INTRVL_SHSG4_NON_ISIN_1_ORGNL_MTRTY_INTRVL_REF_domain,default=None, blank=True, null=True, db_comment="TM_INTRVL_SHSG4_NON_ISIN_1_ORGNL_MTRTY_INTRVL_REF_domain")

	ORGNL_NMNL_AMNT = models.BigIntegerField("ORGNL_NMNL_AMNT",default=None, blank=True, null=True)

	P_FRBRN_EXPSR_PRBTN_RCLD_NP_INPT_domain = {		"0":"Not_applicable",
		"1":"Performing_forborne_exposure_under_probation",
		"2":"Performing_forborne_exposure_not_under_probation",
}

	PRFRMNG_FRBRN_EXPSR_UNDR_PRBTN_RCLSSFD_NN_PRFRMNG_INDCTR = models.CharField("PRFRMNG_FRBRN_EXPSR_UNDR_PRBTN_RCLSSFD_NN_PRFRMNG_INDCTR",max_length=255, choices=P_FRBRN_EXPSR_PRBTN_RCLD_NP_INPT_domain,default=None, blank=True, null=True, db_comment="P_FRBRN_EXPSR_PRBTN_RCLD_NP_INPT_domain")

	PRFRMNG_STTS_RSN_INPT_domain = {		"0":"Not_applicable",
		"1":"Failed_reclassification_to_performing_at_end_of_probation_period",
		"2":"Exited_from_NPE_in_the_last_12_months",
}

	PRFRMNG_STTS_RSN = models.CharField("PRFRMNG_STTS_RSN",max_length=255, choices=PRFRMNG_STTS_RSN_INPT_domain,default=None, blank=True, null=True, db_comment="PRFRMNG_STTS_RSN_INPT_domain")

	PRMRY_ASST_CLSSFCTN_INPT_domain = {		"0":"Not_applicable",
		"D_11":"Straight_bond",
		"D_121":"Traditional_securitisation",
		"D_122":"Synthetic_securitisation",
		"D_129":"Other_securitisation",
		"D_131":"Jumbo_covered_bond",
		"D_139":"Other_covered_bond",
		"D_141":"Euro_medium_term_notes_EMTN",
		"D_149":"Other_MTN",
		"D_15":"Perpetual_bond",
		"D_161":"Inflation_linked_bond",
		"D_162":"Interest_rate_linked_bond",
		"D_163":"Asset_linked_bond",
		"D_164":"Currency_linked_bond",
		"D_165":"Credit_linked_bond",
		"D_166":"Exchange_traded_notes_ETN",
		"D_167":"Exchange_traded_commodities_ETC",
		"D_169":"Other_linked_bond",
		"D_171":"Principal_strip",
		"D_172":"Coupon_strip",
		"D_181":"Investment_product",
		"D_1811":"Capital_protection_product",
		"D_1812":"Yield_enhancement_product",
		"D_1813":"Participation_product",
		"D_1819":"Other_investment_product",
		"D_182":"Leverage_Product",
		"D_1821":"Leverage_product_with_knock_out",
		"D_1822":"Leverage_product_without_knock_out",
		"D_1823":"Constant_leverage_product",
		"D_1829":"Other_leverage_product",
		"D_19":"Other_bond",
		"D_21":"Bankers_acceptance",
		"D_22":"Certificate_of_deposit",
		"D_231":"Euro_commercial_paper_ECP",
		"D_232":"Pagares",
		"D_239":"Other_CP",
		"D_24":"Treasury_bill",
		"D_29":"Other_money_market_instrument",
		"D_31":"Convertible_bond",
		"D_311":"Contingent_convertible_bonds_CoCo_s",
		"D_32":"Bonds_with_warrants_attached",
		"D_33":"Stapled_debt_instrument",
		"D_34":"Non_participating_preferred_share",
		"D_39":"Other_hybrid_debt_Instrument",
		"D_9":"Other_debt",
		"E_1":"Ordinary_Common_share",
		"E_21":"Cumulative_preferred_share",
		"E_22":"Participating_preferred_share",
		"E_23":"Cumulative_participating_preferred_share",
		"E_24":"Redeemable_preferred_share",
		"E_29":"Other_preferred_share",
		"E_31":"American_depository_receipt_ADR",
		"E_32":"Global_depository_receipt_GDR",
		"E_39":"Other_depository_receipt",
		"E_41":"Participation_certificate_Genussschein",
		"E_42":"Convertible_preferred_share",
		"E_43":"Subscription_right",
		"E_49":"Other_hybrid_equity_instrument",
		"E_9":"Other_equity",
		"F_1":"Undertaking_for_collective_investment_in_transferable_securities_UCITS_Fund",
		"F_2":"Alternative_investment_fund_AIF",
		"F_9":"Other_fund",
}

	PRMRY_ASST_CLSSFCTN = models.CharField("PRMRY_ASST_CLSSFCTN",max_length=255, choices=PRMRY_ASST_CLSSFCTN_INPT_domain,default=None, blank=True, null=True, db_comment="PRMRY_ASST_CLSSFCTN_INPT_domain")

	PRPTL_DBT_SCRTY_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"17":"Perpetual_debt_security",
		"18":"Non_perpetual_debt_security",
}

	PRPTL_DBT_SCRTY_INDCTR = models.CharField("PRPTL_DBT_SCRTY_INDCTR",max_length=255, choices=PRPTL_DBT_SCRTY_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="PRPTL_DBT_SCRTY_INDCTR_INPT_domain")

	ISO3166_INPT_domain = {		"0":"Not_applicable",
		"AD":"Andorra",
		"AE":"United_Arab_Emirates_the",
		"AF":"Afghanistan",
		"AG":"Antigua_and_Barbuda",
		"AI":"Anguilla",
		"AL":"Albania",
		"AM":"Armenia",
		"AO":"Angola",
		"AQ":"Antarctica",
		"AR":"Argentina",
		"AS":"American_Samoa",
		"AT":"Austria",
		"AU":"Australia",
		"AW":"Aruba",
		"AX":"Aland_Islands",
		"AZ":"Azerbaijan",
		"BA":"Bosnia_and_Herzegovina",
		"BB":"Barbados",
		"BD":"Bangladesh",
		"BE":"Belgium",
		"BF":"Burkina_Faso",
		"BG":"Bulgaria",
		"BH":"Bahrain",
		"BI":"Burundi",
		"BJ":"Benin",
		"BL":"Saint_Barthelemy",
		"BM":"Bermuda",
		"BN":"Brunei_Darussalam",
		"BO":"Bolivia_Plurinational_State_of",
		"BQ":"Bonaire_Saint_Eustatius_and_Saba",
		"BR":"Brazil",
		"BS":"Bahamas_the",
		"BT":"Bhutan",
		"BV":"Bouvet_Island",
		"BW":"Botswana",
		"BY":"Belarus",
		"BZ":"Belize",
		"CA":"Canada",
		"CC":"Cocos_Keeling_Islands_the",
		"CD":"Congo_the_Democratic_Republic_of_the",
		"CF":"Central_African_Republic_the",
		"CG":"Congo_the",
		"CH":"Switzerland",
		"CI":"Cote_d_Ivoire",
		"CK":"Cook_Islands_the",
		"CL":"Chile",
		"CM":"Cameroon",
		"CN":"China_China_excluding_Taiwan_TW_Hong_Kong_HK_Macao_MO",
		"CO":"Colombia",
		"CR":"Costa_Rica",
		"CU":"Cuba",
		"CV":"Cabo_Verde",
		"CW":"Curacao",
		"CX":"Christmas_Island",
		"CY":"Cyprus",
		"CZ":"Czechia",
		"DE":"Germany",
		"DJ":"Djibouti",
		"DK":"Denmark",
		"DM":"Dominica",
		"DO":"Dominican_Republic_the",
		"DZ":"Algeria",
		"EC":"Ecuador",
		"EE":"Estonia",
		"EG":"Egypt",
		"EH":"Western_Sahara",
		"ER":"Eritrea",
		"ES":"Spain",
		"ET":"Ethiopia",
		"FI":"Finland_Finland_excluding_Aland_AX",
		"FJ":"Fiji",
		"FK":"Falkland_Islands_the_Malvinas",
		"FM":"Micronesia_Federated_States_of",
		"FO":"Faroe_Islands_the",
		"FR":"France_France_excluding_Guadeloupe_GP_Guyane_GF_La_Reunion_RE_Martinique_MQ_Mayotte_YT_Nouvelle_Caledonie_NC_Polynesie_francaise_PF_Saint_Barthelemy_BL_Saint_Martin_MF_Saint_Pierre_et_Miquelon_PM_Terres_australes_francaises_TF_Wallis_et_Futuna_WF",
		"GA":"Gabon",
		"GB":"United_Kingdom_of_Great_Britain_and_Northern_Ireland_the",
		"GD":"Grenada",
		"GE":"Georgia",
		"GF":"French_Guiana",
		"GG":"Guernsey",
		"GH":"Ghana",
		"GI":"Gibraltar",
		"GL":"Greenland",
		"GM":"Gambia_the",
		"GN":"Guinea",
		"GP":"Guadeloupe",
		"GQ":"Equatorial_Guinea",
		"GR":"Greece",
		"GS":"South_Georgia_and_the_South_Sandwich_Islands",
		"GT":"Guatemala",
		"GU":"Guam",
		"GW":"Guinea_Bissau",
		"GY":"Guyana",
		"HK":"Hong_Kong",
		"HM":"Heard_Island_and_McDonald_Islands",
		"HN":"Honduras",
		"HR":"Croatia",
		"HT":"Haiti",
		"HU":"Hungary",
		"ID":"Indonesia",
		"IE":"Ireland",
		"IL":"Israel",
		"IM":"Isle_of_Man",
		"IN":"India",
		"IO":"British_Indian_Ocean_Territory_the",
		"IQ":"Iraq",
		"IR":"Iran_Islamic_Republic_of",
		"IS":"Iceland",
		"IT":"Italy",
		"JE":"Jersey",
		"JM":"Jamaica",
		"JO":"Jordan",
		"JP":"Japan",
		"KE":"Kenya",
		"KG":"Kyrgyzstan",
		"KH":"Cambodia",
		"KI":"Kiribati",
		"KM":"Comoros_the",
		"KN":"Saint_Kitts_and_Nevis",
		"KP":"Korea_the_Democratic_People_s_Republic_of",
		"KR":"Korea_the_Republic_of",
		"KW":"Kuwait",
		"KY":"Cayman_Islands_the",
		"KZ":"Kazakhstan",
		"LA":"Lao_People_s_Democratic_Republic_the",
		"LB":"Lebanon",
		"LC":"Saint_Lucia",
		"LI":"Liechtenstein",
		"LK":"Sri_Lanka",
		"LR":"Liberia",
		"LS":"Lesotho",
		"LT":"Lithuania",
		"LU":"Luxembourg",
		"LV":"Latvia",
		"LY":"Libya",
		"MA":"Morocco",
		"MC":"Monaco",
		"MD":"Moldova_the_Republic_of",
		"ME":"Montenegro",
		"MF":"Saint_Martin_French_part",
		"MG":"Madagascar",
		"MH":"Marshall_Islands_the",
		"MK":"Macedonia_the_former_Yugoslav_Republic_of",
		"ML":"Mali",
		"MM":"Myanmar",
		"MN":"Mongolia",
		"MO":"Macao",
		"MP":"Northern_Mariana_Islands_the",
		"MQ":"Martinique",
		"MR":"Mauritania",
		"MS":"Montserrat",
		"MT":"Malta",
		"MU":"Mauritius",
		"MV":"Maldives",
		"MW":"Malawi",
		"MX":"Mexico",
		"MY":"Malaysia",
		"MZ":"Mozambique",
		"NA":"Namibia",
		"NC":"New_Caledonia",
		"NE":"Niger_the",
		"NF":"Norfolk_Island",
		"NG":"Nigeria",
		"NI":"Nicaragua",
		"NL":"Netherlands_the_Netherlands_excluding_Aruba_AW_Bonaire_Saint_Eustatius_and_Saba_BQ_Curacao_CW_Sint_Maarten_SX",
		"NO":"Norway_Norway_excluding_Svalbard_and_Jan_Mayen_SJ",
		"NP":"Nepal",
		"NR":"Nauru",
		"NU":"Niue",
		"NZ":"New_Zealand",
		"OM":"Oman",
		"PA":"Panama",
		"PE":"Peru",
		"PF":"French_Polynesia",
		"PG":"Papua_New_Guinea",
		"PH":"Philippines_the",
		"PK":"Pakistan",
		"PL":"Poland",
		"PM":"Saint_Pierre_and_Miquelon",
		"PN":"Pitcairn",
		"PR":"Puerto_Rico",
		"PS":"Palestine_State_of",
		"PT":"Portugal",
		"PW":"Palau",
		"PY":"Paraguay",
		"QA":"Qatar",
		"RE":"Reunion",
		"RO":"Romania",
		"RS":"Serbia",
		"RU":"Russian_Federation_the",
		"RW":"Rwanda",
		"SA":"Saudi_Arabia",
		"SB":"Solomon_Islands",
		"SC":"Seychelles",
		"SD":"Sudan_the",
		"SE":"Sweden",
		"SG":"Singapore",
		"SH":"Saint_Helena_Ascension_and_Tristan_da_Cunha",
		"SI":"Slovenia",
		"SJ":"Svalbard_and_Jan_Mayen",
		"SK":"Slovakia",
		"SL":"Sierra_Leone",
		"SM":"San_Marino",
		"SN":"Senegal",
		"SO":"Somalia",
		"SR":"Suriname",
		"SS":"South_Sudan",
		"ST":"Sao_Tome_and_Principe",
		"SV":"El_Salvador",
		"SX":"Sint_Maarten_Dutch_part",
		"SY":"Syrian_Arab_Republic",
		"SZ":"Swaziland",
		"TC":"Turks_and_Caicos_Islands_the",
		"TD":"Chad",
		"TF":"French_Southern_Territories_the",
		"TG":"Togo",
		"TH":"Thailand",
		"TJ":"Tajikistan",
		"TK":"Tokelau",
		"TL":"Timor_Leste",
		"TM":"Turkmenistan",
		"TN":"Tunisia",
		"TO":"Tonga",
		"TR":"Turkey",
		"TT":"Trinidad_and_Tobago",
		"TV":"Tuvalu",
		"TW":"Taiwan_Province_of_China",
		"TZ":"Tanzania_United_Republic_of",
		"UA":"Ukraine",
		"UG":"Uganda",
		"UM":"United_States_Minor_Outlying_Islands_the",
		"US":"United_States_of_America_the_United_States_excluding_American_Samoa_AS_Guam_GU_Northern_Mariana_Islands_MP_Puerto_Rico_PR_United_States_Minor_Outlying_Islands_UM_Virgin_Islands_U_S_VI",
		"UY":"Uruguay",
		"UZ":"Uzbekistan",
		"VA":"Holy_See_the",
		"VC":"Saint_Vincent_and_the_Grenadines",
		"VE":"Venezuela_Bolivarian_Republic_of",
		"VG":"Virgin_Islands_British",
		"VI":"Virgin_Islands_U_S",
		"VN":"Viet_Nam",
		"VU":"Vanuatu",
		"WF":"Wallis_and_Futuna",
		"WS":"Samoa",
		"YE":"Yemen",
		"YT":"Mayotte",
		"ZA":"South_Africa",
		"ZM":"Zambia",
		"ZW":"Zimbabwe",
}

	RL_ESTT_CLLTRL_LCTN = models.CharField("RL_ESTT_CLLTRL_LCTN",max_length=255, choices=ISO3166_INPT_domain,default=None, blank=True, null=True, db_comment="ISO3166_INPT_domain")

	SBRDNTD_DBT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Subordinated_debt",
		"2":"Not_subordinated_debt",
}

	SBRDNTD_DBT = models.CharField("SBRDNTD_DBT",max_length=255, choices=SBRDNTD_DBT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="SBRDNTD_DBT_INDCTR_INPT_domain")

	SCRTY_GRNT_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Unguaranteed",
		"2":"Government_Treasury_guarantee",
		"8":"Other_guarantee",
		"9":"Guarantee_level_No_detailed_information_available",
}

	SCRTY_GRNT_LVL = models.CharField("SCRTY_GRNT_LVL",max_length=255, choices=SCRTY_GRNT_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="SCRTY_GRNT_LVL_INPT_domain")

	SCRTY_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Unsecured",
		"2":"Secured",
		"9":"Security_level_No_detailed_information_available",
}

	SCRTY_LVL = models.CharField("SCRTY_LVL",max_length=255, choices=SCRTY_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="SCRTY_LVL_INPT_domain")

	SCRTY_RNK_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Subordinated_Junior_level",
		"2":"Subordinated_Senior_level",
		"3":"Subordinated_No_further_breakdown_available",
		"4":"Senior",
		"5":"ABS_Class_Junior",
		"6":"ABS_Class_Mezzanine",
		"7":"ABS_Class_Senior",
		"9":"Rank_level_No_detailed_information_available",
}

	SCRTY_RNK_LVL = models.CharField("SCRTY_RNK_LVL",max_length=255, choices=SCRTY_RNK_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="SCRTY_RNK_LVL_INPT_domain")

	SCRTY_STTS_INPT_domain = {		"0":"Not_applicable",
		"100":"alive",
		"101":"Alive_under_judicial_administration_receivership_or_similar_measures",
		"200":"not_alive_reason_not_specified",
		"201":"not_alive_matured_planned_redemption",
		"202":"not_alive_matured_early_redemption",
		"203":"not_alive_issuer_default_bankrupt",
		"204":"not_alive_instrument_in_default",
		"205":"not_alive_split",
		"206":"not_alive_reverse_split",
		"207":"not_alive_knocked_out",
		"208":"not_alive_merger",
		"209":"not_alive_demerger",
		"210":"not_alive_repurchase_of_own_securities",
		"211":"not_alive_converted_exercised",
		"212":"not_alive_issue_withdrawn",
		"213":"not_alive_Dissolution_of_company",
		"214":"not_alive_assimilation",
		"215":"not_alive_temporary_ISIN",
		"216":"not_alive_other_reason",
		"217":"not_alive_old_rights_issue",
		"218":"not_alive_not_covered_by_IF_list",
}

	SCRTY_STTS = models.CharField("SCRTY_STTS",max_length=255, choices=SCRTY_STTS_INPT_domain,default=None, blank=True, null=True, db_comment="SCRTY_STTS_INPT_domain")

	SCRTY_TYP_BY_IDNTFR_INPT_domain = {		"0":"Not_applicable",
		"8":"International_securities_identification_number_ISIN_security",
		"9":"Non_International_securities_identification_number_Non_ISIN_security",
}

	SCRTY_TYP_BY_IDNTFR = models.CharField("SCRTY_TYP_BY_IDNTFR",max_length=255, choices=SCRTY_TYP_BY_IDNTFR_INPT_domain,default=None, blank=True, null=True, db_comment="SCRTY_TYP_BY_IDNTFR_INPT_domain")

	SGNFCNT_ASST_CLSS_INPT_domain = {		"0":"Not_applicable",
		"1":"Interest_rate",
		"2":"Equity",
		"3":"Credit",
		"4":"Commodity",
		"5":"Other",
}

	SGNFCNT_ASST_CLSS = models.CharField("SGNFCNT_ASST_CLSS",max_length=255, choices=SGNFCNT_ASST_CLSS_INPT_domain,default=None, blank=True, null=True, db_comment="SGNFCNT_ASST_CLSS_INPT_domain")

	SHRT_NM_INSTRMNT = models.CharField("SHRT_NM_INSTRMNT",max_length=255,default=None, blank=True, null=True)

	SNRTY_INPT_domain = {		"0":"Not_applicable",
		"5":"ABS_Class_Junior",
		"6":"ABS_Class_Mezzanine",
		"7":"ABS_Class_Senior",
}

	SNRTY = models.CharField("SNRTY",max_length=255, choices=SNRTY_INPT_domain,default=None, blank=True, null=True, db_comment="SNRTY_INPT_domain")

	STRCTRD_NT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Structured_note",
		"2":"Not_structured_note",
}

	STRCTRD_NT_INDCTR = models.CharField("STRCTRD_NT_INDCTR",max_length=255, choices=STRCTRD_NT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="STRCTRD_NT_INDCTR_INPT_domain")

	TM_PST_DU_BND_domain = {		"1002":"_0_days",
		"12":"_gt_3_months_lt_eq_6_months",
		"16":"_gt_6_months_lt_eq_12_months",
		"21":"_gt_1_year_lt_eq_2_years",
		"29":"_gt_2_years_lt_eq_5_years",
		"75":"_gt_eq_1_day_lt_eq_30_days",
		"84":"_gt_5_year_lt_eq_7_years",
		"85":"_gt_7_years",
		"9":"_gt_30_days_lt_eq_90_days",
}

	TM_PST_DU_BND = models.CharField("TM_PST_DU_BND",max_length=255, choices=TM_PST_DU_BND_domain,default=None, blank=True, null=True, db_comment="TM_PST_DU_BND_domain")

	TTL_AMNT_CPTL_ISSD = models.BigIntegerField("TTL_AMNT_CPTL_ISSD",default=None, blank=True, null=True)

	TTL_NMBR_SHRS_ISSD = models.BigIntegerField("TTL_NMBR_SHRS_ISSD",default=None, blank=True, null=True)

	TYP_ASST_SCRTSTN_INPT_WNA_domain = {		"0":"Not_applicable",
		"1000":"Securitisation",
		"1100":"Asset_backed_security_ABS",
		"1101":"Auto_loans_ABS",
		"1102":"Consumer_loans_ABS",
		"1103":"Credit_card_receivables_ABS",
		"1104":"Equipment_leases_ABS",
		"1105":"Home_equity_loans_ABS",
		"1106":"Manufactured_housing_leases_ABS",
		"1107":"Small_and_medium_sized_enterprises_SME_loans_ABS",
		"1108":"Student_loans_ABS",
		"1109":"Whole_Business_Securitisation_WBS_ABS",
		"1110":"Mixed_ABS",
		"1198":"Other_Assets_ABS",
		"1199":"ABS_No_detailed_classification_available",
		"1200":"Mortgage_backed_security_MBS",
		"1201":"Residential_mortgage_backed_security_RMBS",
		"12011":"Residential_mortgage_backed_security_Prime_RMBS_Prime",
		"12012":"Residential_mortgage_backed_security_Mid_prime_RMBS_Mid_prime",
		"12013":"Residential_mortgage_backed_security_Sub_prime_RMBS_Sub_prime",
		"1202":"Commercial_mortgage_backed_security_CMBS",
		"1203":"Mixed_MBS",
		"1298":"Other_MBS",
		"1299":"MBS_No_detailed_classification_available",
		"1300":"Collateralised_Debt_Obligation_CDO",
		"1400":"Collateralised_Mortgage_Obligation_CMO",
		"1500":"Mixed_securitisation",
		"1800":"Other_securitisation",
		"1900":"Securitisation_No_detailed_classification_available",
		"2000":"Covered_Bond",
		"2100":"Public_sector_Covered_bond",
		"2200":"Mortgage_Covered_bond",
		"2300":"Ship_Covered_bond",
		"2400":"Aircraft_Covered_bond",
		"2500":"Mixed_Covered_bond",
		"2800":"Other_Covered_bond",
		"2900":"Covered_Bond_No_detailed_classification_available",
		"9999":"Securitisation_and_Covered_Bond_No_detailed_classification_available",
}

	TYP_ASST_PRVDD_SCRTY = models.CharField("TYP_ASST_PRVDD_SCRTY",max_length=255, choices=TYP_ASST_SCRTSTN_INPT_WNA_domain,default=None, blank=True, null=True, db_comment="TYP_ASST_SCRTSTN_INPT_WNA_domain")

	TYP_SCRTY_EXCHNG_TRDBL_DRVTV_INPT_domain = {		"11":"Debt_security_without_underlying_assets",
		"13":"Asset_backed_security",
		"14":"Covered_bond",
		"3":"Exchange_tradable_option",
		"4":"Exchange_tradable_future",
		"5":"Fund_security",
		"6":"Equity_security",
}

	TYP_SCRTY_EXCHNG_TRDBL_DRVTV = models.CharField("TYP_SCRTY_EXCHNG_TRDBL_DRVTV",max_length=255, choices=TYP_SCRTY_EXCHNG_TRDBL_DRVTV_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_SCRTY_EXCHNG_TRDBL_DRVTV_INPT_domain")

	class Meta:

		verbose_name = 'SCRTY_EXCHNG_TRDBL_DRVTV'

		verbose_name_plural = 'SCRTY_EXCHNG_TRDBL_DRVTVs'

class SCRTY_HDGD_EXCHNG_TRDBL_DRVTV(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SCRTY_HDGD_EXCHNG_TRDBL_DRVTV_uniqueID = models.CharField("SCRTY_HDGD_EXCHNG_TRDBL_DRVTV_uniqueID",max_length=255, primary_key=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255,default=None, blank=True, null=True)

	BYR_PRTY_ID = models.DateTimeField("BYR_PRTY_ID",default=None, blank=True, null=True)

	BYR_PRTY_RL_TYP = models.CharField("BYR_PRTY_RL_TYP",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	EXCHNG_TRDBL_DRVTV_SCRTY_ID = models.CharField("EXCHNG_TRDBL_DRVTV_SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain = {		"3":"Long_security_position_trading_book_assignment_International_Financial_Reporting_Standard_IFRS",
		"4":"Long_security_position_trading_book_assignment_national_general_accepted_accounting_principles_nGAAP",
		"5":"Long_security_position_banking_book_assignment",
}

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP = models.CharField("LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP",max_length=255, choices=LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	SLLR_PRTY_ID = models.CharField("SLLR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	SLLR_PRTY_RL_TYP = models.CharField("SLLR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	TYP_EXCHNG_TRDBL_DRVTV_PSTN_RL = models.CharField("TYP_EXCHNG_TRDBL_DRVTV_PSTN_RL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	theEXCHNG_TRDBL_DRVTV_PSTN_RL = models.ForeignKey("EXCHNG_TRDBL_DRVTV_PSTN_RL", models.SET_NULL,blank=True,null=True,related_name="SCRTY_HDGD_EXCHNG_TRDBL_DRVTV_to_theEXCHNG_TRDBL_DRVTV_PSTN_RLs")

	theLNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT = models.ForeignKey("LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT", models.SET_NULL,blank=True,null=True,related_name="SCRTY_HDGD_EXCHNG_TRDBL_DRVTV_to_theLNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNTs")

	class Meta:

		verbose_name = 'SCRTY_HDGD_EXCHNG_TRDBL_DRVTV'

		verbose_name_plural = 'SCRTY_HDGD_EXCHNG_TRDBL_DRVTVs'

class SCRTY_LNDNG_CMPNNT_SCRTY_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SCRTY_LNDNG_CMPNNT_SCRTY_ASSGNMNT_uniqueID = models.CharField("SCRTY_LNDNG_CMPNNT_SCRTY_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	theSCRTY_EXCHNG_TRDBL_DRVTV = models.ForeignKey("SCRTY_EXCHNG_TRDBL_DRVTV", models.SET_NULL,blank=True,null=True,related_name="SCRTY_LNDNG_CMPNNT_SCRTY_ASSGNMNT_to_theSCRTY_EXCHNG_TRDBL_DRVTVs")

	theSCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL = models.ForeignKey("SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL", models.SET_NULL,blank=True,null=True,related_name="SCRTY_LNDNG_CMPNNT_SCRTY_ASSGNMNT_to_theSCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRLs")

	class Meta:

		verbose_name = 'SCRTY_LNDNG_CMPNNT_SCRTY_ASSGNMNT'

		verbose_name_plural = 'SCRTY_LNDNG_CMPNNT_SCRTY_ASSGNMNTs'

class SCRTY_PSTN(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SCRTY_PSTN_uniqueID = models.CharField("SCRTY_PSTN_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	ACCMLTD_CHNGS_FV = models.BigIntegerField("ACCMLTD_CHNGS_FV",default=None, blank=True, null=True)

	DT_OPNNG_BLNC_F_24_01_INTL_RCGNTN_DT_REF_domain = {		"-1":"Any_date_Total",
		"2":"Current_reference_period_date",
}

	APPLCTN_FRBRNC_STTS_DT = models.CharField("APPLCTN_FRBRNC_STTS_DT",max_length=255, choices=DT_OPNNG_BLNC_F_24_01_INTL_RCGNTN_DT_REF_domain,default=None, blank=True, null=True, db_comment="DT_OPNNG_BLNC_F_24_01_INTL_RCGNTN_DT_REF_domain")

	AVLBL_ENCMBRNC_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Available_for_encumbrance",
		"2":"Not_available_for_encumbrance",
}

	AVLBL_ENCMBRNC_INDCTR = models.CharField("AVLBL_ENCMBRNC_INDCTR",max_length=255, choices=AVLBL_ENCMBRNC_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="AVLBL_ENCMBRNC_INDCTR_INPT_domain")

	CRRNT_LTV_RT = models.FloatField("CRRNT_LTV_RT",default=None, blank=True, null=True)

	CRRYNG_AMNT = models.BigIntegerField("CRRYNG_AMNT",default=None, blank=True, null=True)

	DFLT_STTS_TYP_INPT_domain = {		"0":"Not_applicable",
		"18":"Default_because_both_unlikely_to_pay_and_more_than_90_180_days_past_due",
		"19":"Default_because_unlikely_to_pay",
		"20":"Default_because_more_than_90_180_days_past_due",
}

	DFLT_STTS = models.CharField("DFLT_STTS",max_length=255, choices=DFLT_STTS_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="DFLT_STTS_TYP_INPT_domain")

	DRVD_DFLT_STTS_domain = {		"14":"Not_in_default",
		"6":"Default",
}

	DFLT_STTS_DRVD = models.CharField("DFLT_STTS_DRVD",max_length=255, choices=DRVD_DFLT_STTS_domain,default=None, blank=True, null=True, db_comment="DRVD_DFLT_STTS_domain")

	DT_FRBRNC_STTS = models.DateTimeField("DT_FRBRNC_STTS",default=None, blank=True, null=True)

	ENCMBRD_NMNL_AMNT = models.BigIntegerField("ENCMBRD_NMNL_AMNT",default=None, blank=True, null=True)

	FDCRY_INSTRMNT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Fiduciary_asset",
		"2":"Non_fiduciary_asset",
}

	FDCRY = models.CharField("FDCRY",max_length=255, choices=FDCRY_INSTRMNT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="FDCRY_INSTRMNT_INDCTR_INPT_domain")

	FRBRNC_MSR_GRNTD_DRNG_RFRNC_PRD_domain = {		"1":"Forbearance_measure_granted_during_the_reference_period",
		"2":"No_Forbearance_measure_granted_during_the_reference_period",
}

	FRBRNC_MSR_GRNTD_RFRNC_PRD_INDCTR = models.CharField("FRBRNC_MSR_GRNTD_RFRNC_PRD_INDCTR",max_length=255, choices=FRBRNC_MSR_GRNTD_DRNG_RFRNC_PRD_domain,default=None, blank=True, null=True, db_comment="FRBRNC_MSR_GRNTD_DRNG_RFRNC_PRD_domain")

	FRBRNC_MSR_TYP_domain = {		"0":"Not_applicable",
		"1":"Grace_period_payment_moratorium",
		"10":"Forborne_instruments_with_modified_interest_rate_below_market_conditions",
		"11":"Forborne_instruments_with_modified_interest_rate_not_below_market_conditions",
		"3":"Extension_of_maturity_term",
		"4":"Rescheduled_payments",
		"5":"Debt_forgiveness",
		"6":"Debt_asset_swaps",
		"7":"Other_forbearance_measures",
		"8":"Forborne_Refinanced_debt",
		"9":"Forborne_instruments_with_other_modified_terms_and_conditions",
}

	FRBRNC_MSR_TYP = models.CharField("FRBRNC_MSR_TYP",max_length=255, choices=FRBRNC_MSR_TYP_domain,default=None, blank=True, null=True, db_comment="FRBRNC_MSR_TYP_domain")

	FV = models.BigIntegerField("FV",default=None, blank=True, null=True)

	FV_CHNG = models.BigIntegerField("FV_CHNG",default=None, blank=True, null=True)

	FV_HRRCHY_INPT_domain = {		"0":"Not_applicable",
		"1":"Level_1_Level_1_inputs_used_for_the_measurement_of_fair_value_Level_1_inputs_are_quoted_prices_in_active_markets_for_identical_assets_or_liabilities_that_the_entity_can_access_at_the_measurement_date",
		"2":"Level_2_Level_2_inputs_used_for_the_measurment_of_fair_value_Level_2_inputs_are_inputs_other_than_quoted_prices_included_within_Level_1_that_are_observable_for_the_asset_or_liability_either_directly_or_indirectly",
		"3":"Level_3_Level_3_inputs_used_for_the_measurment_of_fair_value_Level_3_inputs_are_unobservable_inputs_for_the_asset_or_liability",
}

	FV_HRRCHY = models.CharField("FV_HRRCHY",max_length=255, choices=FV_HRRCHY_INPT_domain,default=None, blank=True, null=True, db_comment="FV_HRRCHY_INPT_domain")

	LTGTN_STTS_INPT_domain = {		"0":"Not_applicable",
		"1":"In_pre_litigation",
		"2":"In_litigation",
		"3":"Not_in_litigation_pre_litigation",
}

	LTGTN_STTS = models.CharField("LTGTN_STTS",max_length=255, choices=LTGTN_STTS_INPT_domain,default=None, blank=True, null=True, db_comment="LTGTN_STTS_INPT_domain")

	NGTBL_SCTRY_PSTN_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"17":"Forborne_long_non_negotiable_security_position",
		"18":"Non_forborne_long_non_negotiable_security_position",
		"20":"Long_negotiable_security_position",
}

	NGTBL_SCRTY_PSTN_INDCTR = models.CharField("NGTBL_SCRTY_PSTN_INDCTR",max_length=255, choices=NGTBL_SCTRY_PSTN_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="NGTBL_SCTRY_PSTN_INDCTR_INPT_domain")

	NMBR_SHRS = models.BigIntegerField("NMBR_SHRS",default=None, blank=True, null=True)

	NMNL_AMNT = models.BigIntegerField("NMNL_AMNT",default=None, blank=True, null=True)

	OWN_CMPNY_INVSTMNT_INDCTR_INPT_domain = {		"0":"Not_applicable",
		"1":"Own_company_investment",
		"2":"Non_own_company_investment",
}

	OWN_CMPNY_INVSTMNT_INDCTR = models.CharField("OWN_CMPNY_INVSTMNT_INDCTR",max_length=255, choices=OWN_CMPNY_INVSTMNT_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="OWN_CMPNY_INVSTMNT_INDCTR_INPT_domain")

	PRCNTG_RTND = models.FloatField("PRCNTG_RTND",default=None, blank=True, null=True)

	RTND_DBT_SCRTY_INDCTR_INPT_domain = {		"0":"Not_Applicable",
		"1":"Retained_debt_security",
		"2":"Not_retained_debt_security",
}

	RTND_DBT_SCRTY_INDCTR = models.CharField("RTND_DBT_SCRTY_INDCTR",max_length=255, choices=RTND_DBT_SCRTY_INDCTR_INPT_domain,default=None, blank=True, null=True, db_comment="RTND_DBT_SCRTY_INDCTR_INPT_domain")

	SCRTY_PSTN_BY_ACCNTNG_STNDRD_INPT_domain = {		"0":"Not_applicable",
		"41":"Security_position_International_Financial_Reporting_Standard_IFRS",
		"42":"Security_position_national_general_accepted_accounting_principles_nGAAP",
}

	SCRTY_PSTN_BY_ACCNTNG_STNDRD = models.CharField("SCRTY_PSTN_BY_ACCNTNG_STNDRD",max_length=255, choices=SCRTY_PSTN_BY_ACCNTNG_STNDRD_INPT_domain,default=None, blank=True, null=True, db_comment="SCRTY_PSTN_BY_ACCNTNG_STNDRD_INPT_domain")

	SCRTY_PSTN_RL_TYP_INPT_domain = {		"0":"Not_applicable",
		"1":"Asset_security_position",
		"2":"Liability_security_position",
		"3":"Undetermined_asset_or_liability_security_position",
}

	SCRTY_PSTN_RL_TYP = models.CharField("SCRTY_PSTN_RL_TYP",max_length=255, choices=SCRTY_PSTN_RL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="SCRTY_PSTN_RL_TYP_INPT_domain")

	TYP_SCRTY_PSTN_INPT_domain = {		"1":"Long_debt_security_position",
		"2":"Long_equity_or_fund_security_position",
		"6":"Short_security_position",
}

	TYP_SCRTY_PSTN = models.CharField("TYP_SCRTY_PSTN",max_length=255, choices=TYP_SCRTY_PSTN_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_SCRTY_PSTN_INPT_domain")

	theENTTY_RL = models.ForeignKey("ENTTY_RL", models.SET_NULL,blank=True,null=True,related_name="SCRTY_PSTN_to_theENTTY_RLs")

	theSCRTY_EXCHNG_TRDBL_DRVTV = models.ForeignKey("SCRTY_EXCHNG_TRDBL_DRVTV", models.SET_NULL,blank=True,null=True,related_name="SCRTY_PSTN_to_theSCRTY_EXCHNG_TRDBL_DRVTVs")

	class Meta:

		verbose_name = 'SCRTY_PSTN'

		verbose_name_plural = 'SCRTY_PSTNs'

class SCRTY_PSTN_HDGD_OTC_DRVTV(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SCRTY_PSTN_HDGD_OTC_DRVTV_uniqueID = models.CharField("SCRTY_PSTN_HDGD_OTC_DRVTV_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain = {		"3":"Long_security_position_trading_book_assignment_International_Financial_Reporting_Standard_IFRS",
		"4":"Long_security_position_trading_book_assignment_national_general_accepted_accounting_principles_nGAAP",
		"5":"Long_security_position_banking_book_assignment",
}

	LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP = models.CharField("LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP",max_length=255, choices=LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="LNG_SCRTY_PSTN_PRDNTL_PRTFL_TYP_INPT_domain")

	OTC_DRVTV_ID = models.CharField("OTC_DRVTV_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	NMBR_SHRS = models.BigIntegerField("NMBR_SHRS",default=None, blank=True, null=True)

	NMNL_AMNT = models.BigIntegerField("NMNL_AMNT",default=None, blank=True, null=True)

	SCRTY_PSTN_HDGD_OTC_DRVTV_TYP_domain = {		"40":"Debt_security_position_hedged_by_Over_the_counter_OTC_derivative",
		"41":"Equity_or_fund_security_position_hedged_by_Over_the_counter_OTC_derivative",
}

	SCRTY_PSTN_HDGD_OTC_DRVTV_TYP = models.CharField("SCRTY_PSTN_HDGD_OTC_DRVTV_TYP",max_length=255, choices=SCRTY_PSTN_HDGD_OTC_DRVTV_TYP_domain,default=None, blank=True, null=True, db_comment="SCRTY_PSTN_HDGD_OTC_DRVTV_TYP_domain")

	theLNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT = models.ForeignKey("LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT", models.SET_NULL,blank=True,null=True,related_name="SCRTY_PSTN_HDGD_OTC_DRVTV_to_theLNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNTs")

	theOTC_DRVTV_HDG = models.ForeignKey("OTC_DRVTV_HDG", models.SET_NULL,blank=True,null=True,related_name="SCRTY_PSTN_HDGD_OTC_DRVTV_to_theOTC_DRVTV_HDGs")

	class Meta:

		verbose_name = 'SCRTY_PSTN_HDGD_OTC_DRVTV'

		verbose_name_plural = 'SCRTY_PSTN_HDGD_OTC_DRVTVs'

class SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT_uniqueID = models.CharField("SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	CLLTRL_ID = models.CharField("CLLTRL_ID",max_length=255,default=None, blank=True, null=True)

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain = {		"3":"Security_leg",
		"4":"Loans_and_advances_leg",
		"5":"Equity_instrument_leg",
		"6":"Reverse_repurchase_agreement_cash_leg",
		"7":"Repurchase_agreement_cash_leg",
		"8":"Gold_collateral_leg",
}

	RPRCHS_AGRMNT_CMPNNT_TYP = models.CharField("RPRCHS_AGRMNT_CMPNNT_TYP",max_length=255, choices=RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain")

	RPRCHS_AGRMNT_INSTRMNT_ID = models.CharField("RPRCHS_AGRMNT_INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	NMBR_SHRS = models.BigIntegerField("NMBR_SHRS",default=None, blank=True, null=True)

	NMNL_AMNT = models.BigIntegerField("NMNL_AMNT",default=None, blank=True, null=True)

	SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT_TYP_domain = {		"11":"Debt_security_Security_repurchase_agreement_component_assignment",
		"12":"Equity_or_fund_security_Security_repurchase_agreement_component_assignment",
}

	SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT_TYP = models.CharField("SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT_TYP",max_length=255, choices=SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT_TYP_domain")

	theCLLTRL = models.ForeignKey("CLLTRL", models.SET_NULL,blank=True,null=True,related_name="SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT_to_theCLLTRLs")

	theRPRCHS_AGRMNT_CMPNNT = models.ForeignKey("RPRCHS_AGRMNT_CMPNNT", models.SET_NULL,blank=True,null=True,related_name="SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT_to_theRPRCHS_AGRMNT_CMPNNTs")

	class Meta:

		verbose_name = 'SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT'

		verbose_name_plural = 'SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNTs'

class SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL_uniqueID = models.CharField("SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ISO4217_INPT_domain = {		"0":"Not_applicable",
		"AED":"UAE_Dirham",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"ARS":"Argentine_Peso",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYN":"Belarussian_Ruble",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHE":"WIR_Euro",
		"CHF":"Swiss_franc",
		"CHW":"WIR_Franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CZK":"Czech_koruna",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GTQ":"Quetzal",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"ILS":"New_Israeli_Sheqel",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MRU":"Ouguiya_x2",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDG":"Sudanese_Pound",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SRD":"Surinam_Dollar",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"STN":"Dobra_x2",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJS":"Somoni",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"USN":"US_Dollar_Next_day",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UYW":"Unidad_Previsional",
		"UZS":"Uzbekistan_Sum",
		"VEF":"Bolivar",
		"VES":"Bolivar_Soberano",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XAG":"Silver_one_Troy_ounce",
		"XAU":"Gold_one_Troy_ounce",
		"XBA":"Bond_Markets_Unit_European_Composite_Unit_EURCO",
		"XBB":"Bond_Markets_Unit_European_Monetary_Unit_E_M_U_6",
		"XBC":"Bond_Markets_Unit_European_Unit_of_Account_9_E_U_A_9",
		"XBD":"Bond_Markets_Unit_European_Unit_of_Account_17_E_U_A_17",
		"XCD":"East_Caribbean_Dollar",
		"XDR":"Special_Drawing_Rights_SDR",
		"XOF":"CFA_Franc_BCEAO",
		"XPD":"Palladium_one_Troy_ounce",
		"XPF":"CFP_Franc",
		"XPT":"Platinum_one_Troy_ounce",
		"XSU":"Sucre",
		"XTS":"Codes_specifically_reserved_for_testing_purposes",
		"XUA":"ADB_Unit_of_Account",
		"XXX":"Code_assigned_for_transactions_where_no_currency_is_involved",
		"YER":"Yemeni_Rial",
		"ZAR":"South_African_Rand",
		"ZMW":"Zambian_Kwacha",
		"ZWL":"Zimbabwe_Dollar",
}

	CRRNCY = models.CharField("CRRNCY",max_length=255, choices=ISO4217_INPT_domain,default=None, blank=True, null=True, db_comment="ISO4217_INPT_domain")

	NMBR_SHRS = models.BigIntegerField("NMBR_SHRS",default=None, blank=True, null=True)

	NMNL_AMNT = models.BigIntegerField("NMNL_AMNT",default=None, blank=True, null=True)

	SCRTY_BRRWNG_LNDNG_TRNSCTN_CMPNNT_BY_DRCTN_INPT_domain = {		"0":"Not_applicable",
		"10":"Security_lending_component",
		"11":"Security_collateral_lending_component",
		"5":"Security_borrowing_component",
}

	SCRTY_BRRWNG_LNDNG_TRNSCTN_CMPNNT_TYP_BY_DRCTN = models.CharField("SCRTY_BRRWNG_LNDNG_TRNSCTN_CMPNNT_TYP_BY_DRCTN",max_length=255, choices=SCRTY_BRRWNG_LNDNG_TRNSCTN_CMPNNT_BY_DRCTN_INPT_domain,default=None, blank=True, null=True, db_comment="SCRTY_BRRWNG_LNDNG_TRNSCTN_CMPNNT_BY_DRCTN_INPT_domain")

	TYP_SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL_INPT_domain = {		"1":"Security_borrowing_and_lending_transaction_cash_as_collateral_component",
		"3":"Debt_security_borrowing_and_lending_transaction_component",
		"4":"Equity_or_fund_security_borrowing_and_lending_transaction_component",
}

	TYP_SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL = models.CharField("TYP_SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL",max_length=255, choices=TYP_SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL_INPT_domain")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL_to_theINSTRMNTs")

	class Meta:

		verbose_name = 'SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL'

		verbose_name_plural = 'SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRLs'

class SGNFCNT_CRRNCY_DPRCTN_CNTNGNT_ENCMBRNC(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SGNFCNT_CRRNCY_DPRCTN_CNTNGNT_ENCMBRNC_uniqueID = models.CharField("SGNFCNT_CRRNCY_DPRCTN_CNTNGNT_ENCMBRNC_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_domain = {		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_domain")

	ACCNTNG_FRMWRK_domain = {		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	ISO4217_domain = {		"AED":"UAE_Dirham",
		"AFN":"Afghani",
		"ALL":"Lek",
		"AMD":"Armenian_Dram",
		"ANG":"Netherlands_Antillean_Guilder",
		"AOA":"Kwanza",
		"ARS":"Argentine_Peso",
		"AUD":"Australian_Dollar",
		"AWG":"Aruban_Florin",
		"AZN":"Azerbaijanian_Manat",
		"BAM":"Convertible_Mark",
		"BBD":"Barbados_Dollar",
		"BDT":"Taka",
		"BGN":"Bulgarian_lev",
		"BHD":"Bahraini_Dinar",
		"BIF":"Burundi_Franc",
		"BMD":"Bermudian_Dollar",
		"BND":"Brunei_Dollar",
		"BOB":"Boliviano",
		"BOV":"Mvdol",
		"BRL":"Brazilian_Real",
		"BSD":"Bahamian_Dollar",
		"BTN":"Ngultrum",
		"BWP":"Pula",
		"BYN":"Belarussian_Ruble",
		"BZD":"Belize_Dollar",
		"CAD":"Canadian_Dollar",
		"CDF":"Congolese_Franc",
		"CHE":"WIR_Euro",
		"CHF":"Swiss_franc",
		"CHW":"WIR_Franc",
		"CLF":"Unidades_de_fomento",
		"CLP":"Chilean_Peso",
		"CNY":"Yuan_Renminbi",
		"COP":"Colombian_Peso",
		"COU":"Unidad_de_Valor_Real",
		"CRC":"Costa_Rican_Colon",
		"CUC":"Peso_Convertible",
		"CUP":"Cuban_Peso",
		"CVE":"Cape_Verde_Escudo",
		"CZK":"Czech_koruna",
		"DJF":"Djibouti_Franc",
		"DKK":"Danish_krone",
		"DOP":"Dominican_Peso",
		"DZD":"Algerian_Dinar",
		"EGP":"Egyptian_Pound",
		"ERN":"Nakfa",
		"ETB":"Ethiopian_Birr",
		"EUR":"Euro",
		"FJD":"Fiji_Dollar",
		"FKP":"Falkland_Islands_Pound",
		"GBP":"UK_pound_sterling",
		"GEL":"Lari",
		"GHS":"Ghana_Cedi",
		"GIP":"Gibraltar_Pound",
		"GMD":"Dalasi",
		"GNF":"Guinea_Franc",
		"GTQ":"Quetzal",
		"GYD":"Guyana_Dollar",
		"HKD":"Hong_Kong_Dollar",
		"HNL":"Lempira",
		"HRK":"Croatian_kuna",
		"HTG":"Gourde",
		"HUF":"Hungarian_forint",
		"IDR":"Rupiah",
		"ILS":"New_Israeli_Sheqel",
		"INR":"Indian_Rupee",
		"IQD":"Iraqi_Dinar",
		"IRR":"Iranian_Rial",
		"ISK":"Iceland_Krona",
		"JMD":"Jamaican_Dollar",
		"JOD":"Jordanian_Dinar",
		"JPY":"Japanese_yen",
		"KES":"Kenyan_Shilling",
		"KGS":"Som",
		"KHR":"Riel",
		"KMF":"Comoro_Franc",
		"KPW":"North_Korean_Won",
		"KRW":"Won",
		"KWD":"Kuwaiti_Dinar",
		"KYD":"Cayman_Islands_Dollar",
		"KZT":"Tenge",
		"LAK":"Kip",
		"LBP":"Lebanese_Pound",
		"LKR":"Sri_Lanka_Rupee",
		"LRD":"Liberian_Dollar",
		"LSL":"Loti",
		"LYD":"Libyan_Dinar",
		"MAD":"Moroccan_Dirham",
		"MDL":"Moldovan_Leu",
		"MGA":"Malagasy_Ariary",
		"MKD":"Denar",
		"MMK":"Kyat",
		"MNT":"Tugrik",
		"MOP":"Pataca",
		"MRO":"Ouguiya",
		"MRU":"Ouguiya_x2",
		"MUR":"Mauritius_Rupee",
		"MVR":"Rufiyaa",
		"MWK":"Kwacha",
		"MXN":"Mexican_Peso",
		"MXV":"Mexican_Unidad_de_Inversion_UDI",
		"MYR":"Malaysian_Ringgit",
		"MZN":"Mozambique_Metical",
		"NAD":"Namibia_Dollar",
		"NGN":"Naira",
		"NIO":"Cordoba_Oro",
		"NOK":"Norwegian_Krone",
		"NPR":"Nepalese_Rupee",
		"NZD":"New_Zealand_Dollar",
		"OMR":"Rial_Omani",
		"PAB":"Balboa",
		"PEN":"Nuevo_Sol",
		"PGK":"Kina",
		"PHP":"Philippine_Peso",
		"PKR":"Pakistan_Rupee",
		"PLN":"Polish_zloty",
		"PYG":"Guarani",
		"QAR":"Qatari_Rial",
		"RON":"Romanian_leu",
		"RSD":"Serbian_Dinar",
		"RUB":"Russian_Ruble",
		"RWF":"Rwanda_Franc",
		"SAR":"Saudi_Riyal",
		"SBD":"Solomon_Islands_Dollar",
		"SCR":"Seychelles_Rupee",
		"SDG":"Sudanese_Pound",
		"SEK":"Swedish_krona",
		"SGD":"Singapore_Dollar",
		"SHP":"Saint_Helena_Pound",
		"SLL":"Leone",
		"SOS":"Somali_Shilling",
		"SRD":"Surinam_Dollar",
		"SSP":"South_Sudanese_Pound",
		"STD":"Dobra",
		"STN":"Dobra_x2",
		"SVC":"El_Salvador_Colon",
		"SYP":"Syrian_Pound",
		"SZL":"Lilangeni",
		"THB":"Baht",
		"TJS":"Somoni",
		"TMT":"Turkmenistan_New_Manat",
		"TND":"Tunisian_Dinar",
		"TOP":"Pa_anga",
		"TRY":"Turkish_Lira",
		"TTD":"Trinidad_and_Tobago_Dollar",
		"TWD":"New_Taiwan_Dollar",
		"TZS":"Tanzanian_Shilling",
		"UAH":"Hryvnia",
		"UGX":"Uganda_Shilling",
		"USD":"US_dollar",
		"USN":"US_Dollar_Next_day",
		"UYI":"Uruguay_Peso_en_Unidades_Indexadas_URUIURUI",
		"UYU":"Peso_Uruguayo",
		"UYW":"Unidad_Previsional",
		"UZS":"Uzbekistan_Sum",
		"VEF":"Bolivar",
		"VES":"Bolivar_Soberano",
		"VND":"Dong",
		"VUV":"Vatu",
		"WST":"Tala",
		"XAF":"CFA_Franc_BEAC",
		"XAG":"Silver_one_Troy_ounce",
		"XAU":"Gold_one_Troy_ounce",
		"XBA":"Bond_Markets_Unit_European_Composite_Unit_EURCO",
		"XBB":"Bond_Markets_Unit_European_Monetary_Unit_E_M_U_6",
		"XBC":"Bond_Markets_Unit_European_Unit_of_Account_9_E_U_A_9",
		"XBD":"Bond_Markets_Unit_European_Unit_of_Account_17_E_U_A_17",
		"XCD":"East_Caribbean_Dollar",
		"XDR":"Special_Drawing_Rights_SDR",
		"XOF":"CFA_Franc_BCEAO",
		"XPD":"Palladium_one_Troy_ounce",
		"XPF":"CFP_Franc",
		"XPT":"Platinum_one_Troy_ounce",
		"XSU":"Sucre",
		"XTS":"Codes_specifically_reserved_for_testing_purposes",
		"XUA":"ADB_Unit_of_Account",
		"XXX":"Code_assigned_for_transactions_where_no_currency_is_involved",
		"YER":"Yemeni_Rial",
		"ZAR":"South_African_Rand",
		"ZMW":"Zambian_Kwacha",
		"ZWL":"Zimbabwe_Dollar",
}

	SGNFCNT_CRRNCY = models.CharField("SGNFCNT_CRRNCY",max_length=255, choices=ISO4217_domain,default=None, blank=True, null=True, db_comment="ISO4217_domain")

	CLLTRLSD_DPSTS_OTHR_RPRCHS_AGRMNTS_CNTRL_BNKS_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("CLLTRLSD_DPSTS_OTHR_RPRCHS_AGRMNTS_CNTRL_BNKS_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	CLLTRLSD_DPSTS_OTHR_RPRCHS_AGRMNTS_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("CLLTRLSD_DPSTS_OTHR_RPRCHS_AGRMNTS_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_ASST_BCKD_SCRTS_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("DBT_SCRTY_ISSD_ASST_BCKD_SCRTS_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("DBT_SCRTY_ISSD_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	DBT_SCRTY_ISSD_CVRD_BNDS_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("DBT_SCRTY_ISSD_CVRD_BNDS_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	DPSTS_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("DPSTS_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	DRVTVS_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("DRVTVS_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	OTC_DRVTV_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("OTC_DRVTV_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	OTHR_SRCS_ENCMBRNC_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("OTHR_SRCS_ENCMBRNC_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	RPRCHS_AGRMNT_CNTRL_BNK_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("RPRCHS_AGRMNT_CNTRL_BNK_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	RPRCHS_AGRMNT_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("RPRCHS_AGRMNT_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	SLCTD_FNNCL_LBLT_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("SLCTD_FNNCL_LBLT_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	TTL_SRCS_ENCMBRNC_CRRNCY_DPRCTN_CRRYNG_AMNT = models.BigIntegerField("TTL_SRCS_ENCMBRNC_CRRNCY_DPRCTN_CRRYNG_AMNT",default=None, blank=True, null=True)

	class Meta:

		verbose_name = 'SGNFCNT_CRRNCY_DPRCTN_CNTNGNT_ENCMBRNC'

		verbose_name_plural = 'SGNFCNT_CRRNCY_DPRCTN_CNTNGNT_ENCMBRNCs'

class SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_uniqueID = models.CharField("SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INVSTR_PRTY_ID = models.CharField("INVSTR_PRTY_ID",max_length=255,default=None, blank=True, null=True)

	TYP_PRTY_RL_INPT_domain = {		"0":"Not_applicable",
		"10":"Securitisation_special_purpose_entity_SSPE",
		"11":"Master_netting_counterparty",
		"12":"Security_debtor",
		"13":"Investor",
		"14":"Buyer",
		"15":"Lessor",
		"16":"Factor",
		"17":"Creditor",
		"18":"Depositor",
		"19":"Lessee",
		"20":"Seller",
		"21":"Original_lender",
		"22":"Servicer",
		"23":"Swap_provider",
		"24":"Protection_provider",
		"25":"Originator",
		"26":"Central_counterparty_client",
		"27":"Deposit_taking_corporation",
		"28":"Loan_debtor",
		"30":"Subsidiary",
		"31":"Joint_venture",
		"32":"Associate",
		"33":"Lender",
		"35":"Borrower",
		"36":"Beneficiary",
		"4":"Assigned_debtor",
		"41":"Partner_enterprise",
		"42":"Linked_enterprise",
		"43":"Immediate_parent_enterprise",
		"44":"Key_management_personnel",
		"5":"Non_qualifying_central_counterparty",
		"6":"Qualifying_central_counterparty_QCCP",
		"7":"Clearing_member",
		"8":"Issuer",
		"9":"Sponsor",
}

	INVSTR_PRTY_RL_TYP = models.CharField("INVSTR_PRTY_RL_TYP",max_length=255, choices=TYP_PRTY_RL_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_PRTY_RL_INPT_domain")

	PRDNTL_PRTFL_domain = {		"1":"Trading_book",
		"2":"Non_trading_book",
}

	PRDNTL_PRTFL_TYP = models.CharField("PRDNTL_PRTFL_TYP",max_length=255, choices=PRDNTL_PRTFL_domain,default=None, blank=True, null=True, db_comment="PRDNTL_PRTFL_domain")

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	HRCTS_TRDNG_PSTNS_FV = models.BigIntegerField("HRCTS_TRDNG_PSTNS_FV",default=None, blank=True, null=True)

	SHRT_PSTN_ACCNTNG_CLSSFCTN_domain = {		"23":"IFRS_Financial_liabilities_held_for_trading_Financial_liabilities_held_for_trading_in_accordance_with_IFRS",
		"33":"nGAAP_Trading_financial_liabilities_Trading_financial_liabilities_in_accordance_with_national_GAAP_based_on_BAD",
}

	SHRT_PSTN_ACCNTNG_CLSSFCTN = models.CharField("SHRT_PSTN_ACCNTNG_CLSSFCTN",max_length=255, choices=SHRT_PSTN_ACCNTNG_CLSSFCTN_domain,default=None, blank=True, null=True, db_comment="SHRT_PSTN_ACCNTNG_CLSSFCTN_domain")

	TYP_SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_INPT_domain = {		"2":"Short_banking_book_security_position",
		"3":"Short_trading_book_security_position_International_Financial_Reporting_Standard_IFRS",
		"4":"Short_trading_book_security_position_national_general_accepted_accounting_principles_nGAAP",
}

	TYP_SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT = models.CharField("TYP_SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT",max_length=255, choices=TYP_SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_INPT_domain,default=None, blank=True, null=True, db_comment="TYP_SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_INPT_domain")

	theSCRTY_PSTN = models.ForeignKey("SCRTY_PSTN", models.SET_NULL,blank=True,null=True,related_name="SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_to_theSCRTY_PSTNs")

	class Meta:

		verbose_name = 'SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT'

		verbose_name_plural = 'SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNTs'

class SNTHTC_SCRTSTN(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SNTHTC_SCRTSTN_uniqueID = models.CharField("SNTHTC_SCRTSTN_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSTN_ID = models.CharField("SCRTSTN_ID",max_length=255,default=None, blank=True, null=True)

	AMNT_DRCGNSD_CPTL_PRPS = models.BigIntegerField("AMNT_DRCGNSD_CPTL_PRPS",default=None, blank=True, null=True)

	PRCNTG_RTND = models.FloatField("PRCNTG_RTND",default=None, blank=True, null=True)

	RSCRTSTN_INDCTR_domain = {		"1":"Re_securitisation",
		"2":"Not_re_securitisation",
}

	RSCRTSTN_INDCTR = models.CharField("RSCRTSTN_INDCTR",max_length=255, choices=RSCRTSTN_INDCTR_domain,default=None, blank=True, null=True, db_comment="RSCRTSTN_INDCTR_domain")

	SCRTSN_OTHR_CRDT_TRNSFR_TYP_domain = {		"5":"Covered_bond_programme",
		"6":"Credit_transfer_other_than_securitisation_and_covered_bond_program",
		"7":"Securitisation",
}

	SCRTSN_OTHR_CRDT_TRNSFR_TYP = models.CharField("SCRTSN_OTHR_CRDT_TRNSFR_TYP",max_length=255, choices=SCRTSN_OTHR_CRDT_TRNSFR_TYP_domain,default=None, blank=True, null=True, db_comment="SCRTSN_OTHR_CRDT_TRNSFR_TYP_domain")

	SCRTSN_TYP_domain = {		"1":"Traditional_securititsation",
		"2":"Synthetic_securitisation",
}

	SCRTSN_TYP = models.CharField("SCRTSN_TYP",max_length=255, choices=SCRTSN_TYP_domain,default=None, blank=True, null=True, db_comment="SCRTSN_TYP_domain")

	SGNFCNT_RSK_TRNSFR_INDCTR_domain = {		"1":"Significant_risk_transfer_securitisation",
		"2":"Not_significant_risk_transfer_securitisation",
}

	SGNFCNT_RSK_TRNSFR_INDCTR = models.CharField("SGNFCNT_RSK_TRNSFR_INDCTR",max_length=255, choices=SGNFCNT_RSK_TRNSFR_INDCTR_domain,default=None, blank=True, null=True, db_comment="SGNFCNT_RSK_TRNSFR_INDCTR_domain")

	SNTHTC_SCRTSTN_TYP_domain = {		"3":"Synthetic_securitisation_without_involvement_of_an_SSPE",
		"4":"Synthetic_securitisation_involving_an_SSPE",
}

	SNTHTC_SCRTSTN_TYP = models.CharField("SNTHTC_SCRTSTN_TYP",max_length=255, choices=SNTHTC_SCRTSTN_TYP_domain,default=None, blank=True, null=True, db_comment="SNTHTC_SCRTSTN_TYP_domain")

	STS_SCRTSTN_INDCTR_domain = {		"1":"Simple_transparent_and_standardised_STS_securitisation",
		"2":"Not_simple_transparent_and_standardised_STS_securitisation",
}

	STS_SCRTSTN_INDCTR = models.CharField("STS_SCRTSTN_INDCTR",max_length=255, choices=STS_SCRTSTN_INDCTR_domain,default=None, blank=True, null=True, db_comment="STS_SCRTSTN_INDCTR_domain")

	theASST_PL = models.ForeignKey("ASST_PL", models.SET_NULL,blank=True,null=True,related_name="SNTHTC_SCRTSTN_to_theASST_PLs")

	class Meta:

		verbose_name = 'SNTHTC_SCRTSTN'

		verbose_name_plural = 'SNTHTC_SCRTSTNs'

class SYNDCTD_CNTRCT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	SYNDCTD_CNTRCT_uniqueID = models.CharField("SYNDCTD_CNTRCT_uniqueID",max_length=255, primary_key=True)

	SYNDCTD_CNTRCT_ID = models.CharField("SYNDCTD_CNTRCT_ID",max_length=255,default=None, blank=True, null=True)

	class Meta:

		verbose_name = 'SYNDCTD_CNTRCT'

		verbose_name_plural = 'SYNDCTD_CNTRCTs'

class TRDTNL_SCRTSTN(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	TRDTNL_SCRTSTN_uniqueID = models.CharField("TRDTNL_SCRTSTN_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSTN_ID = models.CharField("SCRTSTN_ID",max_length=255,default=None, blank=True, null=True)

	AMNT_DRCGNSD_CPTL_PRPS = models.BigIntegerField("AMNT_DRCGNSD_CPTL_PRPS",default=None, blank=True, null=True)

	DSCNT_EXCSS_SPRD_AMNT = models.FloatField("DSCNT_EXCSS_SPRD_AMNT",default=None, blank=True, null=True)

	PRCNTG_RTND = models.FloatField("PRCNTG_RTND",default=None, blank=True, null=True)

	RSCRTSTN_INDCTR_domain = {		"1":"Re_securitisation",
		"2":"Not_re_securitisation",
}

	RSCRTSTN_INDCTR = models.CharField("RSCRTSTN_INDCTR",max_length=255, choices=RSCRTSTN_INDCTR_domain,default=None, blank=True, null=True, db_comment="RSCRTSTN_INDCTR_domain")

	SCRTSN_OTHR_CRDT_TRNSFR_TYP_domain = {		"5":"Covered_bond_programme",
		"6":"Credit_transfer_other_than_securitisation_and_covered_bond_program",
		"7":"Securitisation",
}

	SCRTSN_OTHR_CRDT_TRNSFR_TYP = models.CharField("SCRTSN_OTHR_CRDT_TRNSFR_TYP",max_length=255, choices=SCRTSN_OTHR_CRDT_TRNSFR_TYP_domain,default=None, blank=True, null=True, db_comment="SCRTSN_OTHR_CRDT_TRNSFR_TYP_domain")

	SCRTSN_TYP_domain = {		"1":"Traditional_securititsation",
		"2":"Synthetic_securitisation",
}

	SCRTSN_TYP = models.CharField("SCRTSN_TYP",max_length=255, choices=SCRTSN_TYP_domain,default=None, blank=True, null=True, db_comment="SCRTSN_TYP_domain")

	SGNFCNT_RSK_TRNSFR_INDCTR_domain = {		"1":"Significant_risk_transfer_securitisation",
		"2":"Not_significant_risk_transfer_securitisation",
}

	SGNFCNT_RSK_TRNSFR_INDCTR = models.CharField("SGNFCNT_RSK_TRNSFR_INDCTR",max_length=255, choices=SGNFCNT_RSK_TRNSFR_INDCTR_domain,default=None, blank=True, null=True, db_comment="SGNFCNT_RSK_TRNSFR_INDCTR_domain")

	STS_SCRTSTN_INDCTR_domain = {		"1":"Simple_transparent_and_standardised_STS_securitisation",
		"2":"Not_simple_transparent_and_standardised_STS_securitisation",
}

	STS_SCRTSTN_INDCTR = models.CharField("STS_SCRTSTN_INDCTR",max_length=255, choices=STS_SCRTSTN_INDCTR_domain,default=None, blank=True, null=True, db_comment="STS_SCRTSTN_INDCTR_domain")

	theASST_PL = models.ForeignKey("ASST_PL", models.SET_NULL,blank=True,null=True,related_name="TRDTNL_SCRTSTN_to_theASST_PLs")

	theCRDT_FCLTY = models.ForeignKey("CRDT_FCLTY", models.SET_NULL,blank=True,null=True,related_name="TRDTNL_SCRTSTN_to_theCRDT_FCLTYs")

	class Meta:

		verbose_name = 'TRDTNL_SCRTSTN'

		verbose_name_plural = 'TRDTNL_SCRTSTNs'

class TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_DPST(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_DPST_uniqueID = models.CharField("TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_DPST_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSTN_ID = models.CharField("SCRTSTN_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSTN_TRNCH_TYP_INPT_domain = {		"1":"Tranche_in_a_synthetic_securitisation_with_SSPE",
		"2":"Tranche_in_a_synthetic_securitisation_without_SSPE",
		"3":"Tranche_in_a_Traditional_securitisation",
}

	SCRTSTN_TRNCH_TYP = models.CharField("SCRTSTN_TRNCH_TYP",max_length=255, choices=SCRTSTN_TRNCH_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="SCRTSTN_TRNCH_TYP_INPT_domain")

	TRNCH_ID = models.CharField("TRNCH_ID",max_length=255,default=None, blank=True, null=True)

	TRNCH_NM = models.CharField("TRNCH_NM",max_length=255,default=None, blank=True, null=True)

	TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_TYP_domain = {		"1":"Tranche_in_a_synthetic_securitisation_without_SSPE_being_a_deposit",
		"2":"Tranche_in_a_synthetic_securitisation_without_SSPE_being_a_financial_guarantee",
}

	TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_TYP = models.CharField("TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_TYP",max_length=255, choices=TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_TYP_domain,default=None, blank=True, null=True, db_comment="TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_TYP_domain")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_DPST_to_theINSTRMNTs")

	theSNTHTC_SCRTSTN = models.ForeignKey("SNTHTC_SCRTSTN", models.SET_NULL,blank=True,null=True,related_name="TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_DPST_to_theSNTHTC_SCRTSTNs")

	class Meta:

		verbose_name = 'TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_DPST'

		verbose_name_plural = 'TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_DPSTs'

class TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_FNNCL_GRNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_FNNCL_GRNT_uniqueID = models.CharField("TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_FNNCL_GRNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSTN_ID = models.CharField("SCRTSTN_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSTN_TRNCH_TYP_INPT_domain = {		"1":"Tranche_in_a_synthetic_securitisation_with_SSPE",
		"2":"Tranche_in_a_synthetic_securitisation_without_SSPE",
		"3":"Tranche_in_a_Traditional_securitisation",
}

	SCRTSTN_TRNCH_TYP = models.CharField("SCRTSTN_TRNCH_TYP",max_length=255, choices=SCRTSTN_TRNCH_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="SCRTSTN_TRNCH_TYP_INPT_domain")

	TRNCH_ID = models.CharField("TRNCH_ID",max_length=255,default=None, blank=True, null=True)

	TRNCH_NM = models.CharField("TRNCH_NM",max_length=255,default=None, blank=True, null=True)

	TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_TYP_domain = {		"1":"Tranche_in_a_synthetic_securitisation_without_SSPE_being_a_deposit",
		"2":"Tranche_in_a_synthetic_securitisation_without_SSPE_being_a_financial_guarantee",
}

	TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_TYP = models.CharField("TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_TYP",max_length=255, choices=TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_TYP_domain,default=None, blank=True, null=True, db_comment="TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_TYP_domain")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_FNNCL_GRNT_to_theINSTRMNTs")

	theSNTHTC_SCRTSTN = models.ForeignKey("SNTHTC_SCRTSTN", models.SET_NULL,blank=True,null=True,related_name="TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_FNNCL_GRNT_to_theSNTHTC_SCRTSTNs")

	class Meta:

		verbose_name = 'TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_FNNCL_GRNT'

		verbose_name_plural = 'TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_FNNCL_GRNTs'

class TRNCH_TRDTNL_SCRTSTN(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	TRNCH_TRDTNL_SCRTSTN_uniqueID = models.CharField("TRNCH_TRDTNL_SCRTSTN_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	ACCNTNG_FRMWRK_INPT_domain = {		"0":"Not_applicable",
		"1":"National_GAAP_not_consistent_with_IFRS",
		"2":"IFRS",
		"3":"National_GAAP_consistent_with_IFRS",
}

	SCRTSTN = models.CharField("SCRTSTN",max_length=255, choices=ACCNTNG_FRMWRK_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_FRMWRK_INPT_domain")

	SCRTSTN_ID = models.CharField("SCRTSTN_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_ID = models.CharField("SCRTY_ID",max_length=255,default=None, blank=True, null=True)

	SCRTY_RPRTNG_AGNT_ID = models.CharField("SCRTY_RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	SCRTSTN_TRNCH_TYP_INPT_domain = {		"1":"Tranche_in_a_synthetic_securitisation_with_SSPE",
		"2":"Tranche_in_a_synthetic_securitisation_without_SSPE",
		"3":"Tranche_in_a_Traditional_securitisation",
}

	SCRTSTN_TRNCH_TYP = models.CharField("SCRTSTN_TRNCH_TYP",max_length=255, choices=SCRTSTN_TRNCH_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="SCRTSTN_TRNCH_TYP_INPT_domain")

	TRNCH_ID = models.CharField("TRNCH_ID",max_length=255,default=None, blank=True, null=True)

	TRNCH_NM = models.CharField("TRNCH_NM",max_length=255,default=None, blank=True, null=True)

	theSCRTY_EXCHNG_TRDBL_DRVTV = models.ForeignKey("SCRTY_EXCHNG_TRDBL_DRVTV", models.SET_NULL,blank=True,null=True,related_name="TRNCH_TRDTNL_SCRTSTN_to_theSCRTY_EXCHNG_TRDBL_DRVTVs")

	theTRDTNL_SCRTSTN = models.ForeignKey("TRDTNL_SCRTSTN", models.SET_NULL,blank=True,null=True,related_name="TRNCH_TRDTNL_SCRTSTN_to_theTRDTNL_SCRTSTNs")

	class Meta:

		verbose_name = 'TRNCH_TRDTNL_SCRTSTN'

		verbose_name_plural = 'TRNCH_TRDTNL_SCRTSTNs'

class TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNT(models.Model):

	test_id = models.CharField("test_id",max_length=255,default=None, blank=True, null=True)

	TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNT_uniqueID = models.CharField("TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNT_uniqueID",max_length=255, primary_key=True)

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_CNSLDTN_LVL = models.CharField("ACCNTNG_CNSLDTN_LVL",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	ACCNTNG_CNSLDTN_LVL_INPT_domain = {		"0":"Not_applicable",
		"1":"Solo_consolidation_level",
		"2":"Group_consolidation_level",
}

	ACCNTNG_STNDRD = models.CharField("ACCNTNG_STNDRD",max_length=255, choices=ACCNTNG_CNSLDTN_LVL_INPT_domain,default=None, blank=True, null=True, db_comment="ACCNTNG_CNSLDTN_LVL_INPT_domain")

	DT_RFRNC = models.DateTimeField("DT_RFRNC",default=None, blank=True, null=True)

	INSTRMNT_ID = models.CharField("INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain = {		"3":"Security_leg",
		"4":"Loans_and_advances_leg",
		"5":"Equity_instrument_leg",
		"6":"Reverse_repurchase_agreement_cash_leg",
		"7":"Repurchase_agreement_cash_leg",
		"8":"Gold_collateral_leg",
}

	RPRCHS_AGRMNT_CMPNNT_TYP = models.CharField("RPRCHS_AGRMNT_CMPNNT_TYP",max_length=255, choices=RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain,default=None, blank=True, null=True, db_comment="RPRCHS_AGRMNT_CMPNNT_TYP_INPT_domain")

	RPRCHS_AGRMNT_INSTRMNT_ID = models.CharField("RPRCHS_AGRMNT_INSTRMNT_ID",max_length=255,default=None, blank=True, null=True)

	RPRTNG_AGNT_ID = models.CharField("RPRTNG_AGNT_ID",max_length=255,default=None, blank=True, null=True)

	TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNT_TYP_domain = {		"1":"Equity_instrument_leg_Equity_instrument_that_is_not_a_security_assignment",
		"2":"Loan_and_advance_leg_Loan_and_advance_assignment",
}

	TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNT_TYP = models.CharField("TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNT_TYP",max_length=255, choices=TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNT_TYP_domain,default=None, blank=True, null=True, db_comment="TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNT_TYP_domain")

	theINSTRMNT = models.ForeignKey("INSTRMNT", models.SET_NULL,blank=True,null=True,related_name="TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNT_to_theINSTRMNTs")

	theRPRCHS_AGRMNT_CMPNNT = models.ForeignKey("RPRCHS_AGRMNT_CMPNNT", models.SET_NULL,blank=True,null=True,related_name="TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNT_to_theRPRCHS_AGRMNT_CMPNNTs")

	class Meta:

		verbose_name = 'TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNT'

		verbose_name_plural = 'TRNSFRRD_ASST_LG_INSTRMNT_ASSGNMNTs'

