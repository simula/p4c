#include <core.p4>
#define V1MODEL_VERSION 20180101
#include <v1model.p4>

header H {
    bit<8> a;
}

struct Headers {
    H h;
}

struct Meta {
}

control ingress(inout Headers h, inout Meta m, inout standard_metadata_t sm) {
    @name("ingress.tmp") bit<8> tmp;
    @name("ingress.action_thing") action action_thing(inout bit<32> c) {
        {
            @name("ingress.d_0") bit<32> d_0;
            @name("ingress.hasReturned") bool hasReturned = false;
            @name("ingress.retval") bit<8> retval;
            hasReturned = true;
            retval = 8w1;
            c = d_0;
            tmp = retval;
        }
        c = (bit<32>)tmp;
    }
    apply {
        action_thing(sm.enq_timestamp);
    }
}

parser p(packet_in b, out Headers h, inout Meta m, inout standard_metadata_t sm) {
    state start {
        transition accept;
    }
}

control vrfy(inout Headers h, inout Meta m) {
    apply {
    }
}

control update(inout Headers h, inout Meta m) {
    apply {
    }
}

control egress(inout Headers h, inout Meta m, inout standard_metadata_t sm) {
    apply {
    }
}

control deparser(packet_out pkt, in Headers h) {
    apply {
        pkt.emit<Headers>(h);
    }
}

V1Switch<Headers, Meta>(p(), vrfy(), ingress(), egress(), update(), deparser()) main;

