

struct ethernet_t {
	bit<48> dstAddr
	bit<48> srcAddr
	bit<16> etherType
}

struct metadata_t {
	bit<32> psa_ingress_parser_input_metadata_ingress_port
	bit<32> psa_ingress_parser_input_metadata_packet_path
	bit<32> psa_egress_parser_input_metadata_egress_port
	bit<32> psa_egress_parser_input_metadata_packet_path
	bit<32> psa_ingress_input_metadata_ingress_port
	bit<32> psa_ingress_input_metadata_packet_path
	bit<64> psa_ingress_input_metadata_ingress_timestamp
	bit<8> psa_ingress_input_metadata_parser_error
	bit<8> psa_ingress_output_metadata_class_of_service
	bit<8> psa_ingress_output_metadata_clone
	bit<16> psa_ingress_output_metadata_clone_session_id
	bit<8> psa_ingress_output_metadata_drop
	bit<8> psa_ingress_output_metadata_resubmit
	bit<32> psa_ingress_output_metadata_multicast_group
	bit<32> psa_ingress_output_metadata_egress_port
	bit<8> psa_egress_input_metadata_class_of_service
	bit<32> psa_egress_input_metadata_egress_port
	bit<32> psa_egress_input_metadata_packet_path
	bit<16> psa_egress_input_metadata_instance
	bit<64> psa_egress_input_metadata_egress_timestamp
	bit<8> psa_egress_input_metadata_parser_error
	bit<32> psa_egress_deparser_input_metadata_egress_port
	bit<8> psa_egress_output_metadata_clone
	bit<16> psa_egress_output_metadata_clone_session_id
	bit<8> psa_egress_output_metadata_drop
}
metadata instanceof metadata_t

header ethernet instanceof ethernet_t

action execute args none {
	counter_count counter_0 0x100
	return
}

table tbl {
	actions {
		execute
	}
	default_action execute args none 
	size 0
}


apply {
	rx m.psa_ingress_input_metadata_ingress_port
	mov m.psa_ingress_output_metadata_drop 0x0
	extract h.ethernet
	mov m.psa_ingress_output_metadata_drop 0
	mov m.psa_ingress_output_metadata_multicast_group 0x0
	cast  h.ethernet.dstAddr bit_32 m.psa_ingress_output_metadata_egress_port
	table tbl
	jmpneq LABEL_DROP m.psa_ingress_output_metadata_drop 0x0
	emit h.ethernet
	extract h.ethernet
	emit h.ethernet
	tx m.psa_ingress_output_metadata_egress_port
	LABEL_DROP : drop
}


