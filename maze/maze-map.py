#!/usr/local/bin/python3

import string

#prepare data structure

cardinals = { "a":"n",
              "b":"e",
              "c":"s",
              "d":"w" };

tiles = { "x" :"crossroads.jpg",
          "st":"straight-t.jpg",
          "lt":"left-t.jpg",
          "rt":"right-t.jpg",
          "s" :"straight.jpg",
          "lb":"left-b.jpg",
          "rb":"right-b.jpg",
          "oc":"orb-cyan.jpg",
          "or":"orb-red.jpg",
          "op":"orb-purple.jpg",
          "de":"dead-end.jpg" };

maze = { "n" : { 
  "aa":"rb", "ab":"", "ac":"", "ad":"", "ae":"st", "af":"", "ag":"", "ah":"", "ai":"", "aj":"st", "ak":"", "al":"", "am":"lb", "an":"rb", "ao":"", "ap":"", "aq":"st", "ar":"", "as":"", "at":"lb", "au":"rb", "av":"lb", "aw":"rb", "ax":"st", "ay":"lb", "az":"rb", "a1":"", "a2":"", "a3":"st", "a4":"lb",
  "ba":"s", "bb":"rb", "bc":"", "bd":"", "be":"", "bf":"rb", "bg":"", "bh":"", "bi":"lb", "bj":"s", "bk":"rb", "bl":"", "bm":"lt", "bn":"rt", "bo":"", "bp":"", "bq":"s", "br":"", "bs":"", "bt":"", "bu":"s", "bv":"", "bw":"", "bx":"s", "by":"", "bz":"s", "b1":"rb", "b2":"", "b3":"s", "b4":"s",
  "ca":"s", "cb":"s", "cc":"rb", "cd":"", "ce":"st", "cf":"", "cg":"", "ch":"", "ci":"s", "cj":"s", "ck":"s", "cl":"de", "cm":"s", "cn":"s", "co":"rb", "cp":"", "cq":"s", "cr":"rb", "cs":"st", "ct":"lb", "cu":"s", "cv":"rb", "cw":"", "cx":"x", "cy":"", "cz":"", "c1":"s", "c2":"", "c3":"", "c4":"s",
  "da":"s", "db":"s", "dc":"", "dd":"", "de":"s", "df":"rb", "dg":"", "dh":"", "di":"", "dj":"s", "dk":"s", "dl":"", "dm":"", "dn":"s", "do":"rt", "dp":"", "dq":"", "dr":"s", "ds":"s", "dt":"s", "du":"s", "dv":"", "dw":"", "dx":"s", "dy":"or", "dz":"rb", "d1":"", "d2":"st", "d3":"lb", "d4":"s",
  "ea":"s", "eb":"", "ec":"", "ed":"", "ee":"lt", "ef":"", "eg":"", "eh":"", "ei":"", "ej":"", "ek":"rt", "el":"", "em":"", "en":"x", "eo":"", "ep":"", "eq":"", "er":"", "es":"s", "et":"", "eu":"s", "ev":"rb", "ew":"", "ex":"", "ey":"", "ez":"", "e1":"", "e2":"s", "e3":"", "e4":"",
  "fa":"rt", "fb":"", "fc":"st", "fd":"", "fe":"", "ff":"lb", "fg":"rb", "fh":"", "fi":"st", "fj":"lb", "fk":"s", "fl":"rb", "fm":"lb", "fn":"s", "fo":"rb", "fp":"lb", "fq":"rb", "fr":"", "fs":"", "ft":"", "fu":"lt", "fv":"", "fw":"", "fx":"lb", "fy":"rb", "fz":"", "f1":"", "f2":"x", "f3":"", "f4":"lb",
  "ga":"s", "gb":"de", "gc":"s", "gd":"rb", "ge":"lb", "gf":"s", "gg":"s", "gh":"de", "gi":"s", "gj":"s", "gk":"s", "gl":"s", "gm":"s", "gn":"s", "go":"s", "gp":"s", "gq":"s", "gr":"rb", "gs":"", "gt":"lb", "gu":"", "gv":"", "gw":"", "gx":"", "gy":"", "gz":"", "g1":"", "g2":"s", "g3":"", "g4":"s",
  "ha":"s", "hb":"s", "hc":"s", "hd":"", "he":"s", "hf":"s", "hg":"", "hh":"", "hi":"s", "hj":"s", "hk":"s", "hl":"s", "hm":"s", "hn":"s", "ho":"s", "hp":"rt", "hq":"lt", "hr":"s", "hs":"de", "ht":"s", "hu":"rb", "hv":"", "hw":"", "hx":"lb", "hy":"rb", "hz":"", "h1":"lb", "h2":"s", "h3":"s", "h4":"s",
  "ia":"s", "ib":"", "ic":"", "id":"", "ie":"", "if":"rt", "ig":"", "ih":"", "ii":"", "ij":"s", "ik":"s", "il":"", "im":"s", "in":"", "io":"", "ip":"s", "iq":"s", "ir":"", "is":"", "it":"s", "iu":"s", "iv":"rb", "iw":"", "ix":"s", "iy":"", "iz":"", "i1":"s", "i2":"s", "i3":"", "i4":"",
  "ja":"", "jb":"", "jc":"", "jd":"", "je":"", "jf":"", "jg":"", "jh":"", "ji":"", "jj":"s", "jk":"", "jl":"", "jm":"", "jn":"", "jo":"st", "jp":"", "jq":"", "jr":"", "js":"", "jt":"", "ju":"s", "jv":"", "jw":"", "jx":"", "jy":"", "jz":"", "j1":"", "j2":"", "j3":"", "j4":"",
  "ka":"rb", "kb":"lb", "kc":"rb", "kd":"", "ke":"", "kf":"", "kg":"rb", "kh":"", "ki":"", "kj":"lt", "kk":"rb", "kl":"st", "km":"", "kn":"lb", "ko":"s", "kp":"", "kq":"", "kr":"st", "ks":"", "kt":"lb", "ku":"s", "kv":"", "kw":"", "kx":"lb", "ky":"", "kz":"lb", "k1":"rb", "k2":"", "k3":"", "k4":"lb",
  "la":"", "lb":"s", "lc":"", "ld":"", "le":"st", "lf":"st", "lg":"", "lh":"", "li":"", "lj":"s", "lk":"", "ll":"s", "lm":"", "ln":"", "lo":"rt", "lp":"", "lq":"", "lr":"", "ls":"de", "lt":"s", "lu":"rt", "lv":"", "lw":"lb", "lx":"", "ly":"", "lz":"lt", "l1":"s", "l2":"rb", "l3":"lb", "l4":"s",
  "ma":"", "mb":"x", "mc":"", "md":"lb", "me":"s", "mf":"s", "mg":"rb", "mh":"", "mi":"", "mj":"lt", "mk":"rb", "ml":"", "mm":"", "mn":"", "mo":"lt", "mp":"rb", "mq":"st", "mr":"lb", "ms":"s", "mt":"s", "mu":"s", "mv":"rb", "mw":"", "mx":"st", "my":"lb", "mz":"s", "m1":"s", "m2":"", "m3":"s", "m4":"s",
  "na":"rb", "nb":"lt", "nc":"de", "nd":"s", "ne":"s", "nf":"", "ng":"", "nh":"st", "ni":"lb", "nj":"s", "nk":"s", "nl":"rb", "nm":"", "nn":"", "no":"s", "np":"s", "nq":"s", "nr":"s", "ns":"", "nt":"lt", "nu":"s", "nv":"s", "nw":"", "nx":"", "ny":"s", "nz":"", "n1":"rt", "n2":"", "n3":"", "n4":"s",
  "oa":"", "ob":"s", "oc":"", "od":"", "oe":"s", "of":"rb", "og":"lb", "oh":"s", "oi":"s", "oj":"s", "ok":"s", "ol":"", "om":"st", "on":"", "oo":"lt", "op":"s", "oq":"s", "or":"s", "os":"de", "ot":"s", "ou":"", "ov":"", "ow":"", "ox":"", "oy":"x", "oz":"", "o1":"", "o2":"rb", "o3":"", "o4":"",
  "pa":"rb", "pb":"", "pc":"", "pd":"", "pe":"lt", "pf":"s", "pg":"s", "ph":"", "pi":"s", "pj":"s", "pk":"", "pl":"", "pm":"s", "pn":"rb", "po":"", "pp":"s", "pq":"s", "pr":"s", "ps":"s", "pt":"s", "pu":"rb", "pv":"", "pw":"", "px":"lb", "py":"s", "pz":"rb", "p1":"", "p2":"", "p3":"", "p4":"lb",
  "qa":"s", "qb":"de", "qc":"rb", "qd":"", "qe":"", "qf":"s", "qg":"", "qh":"", "qi":"", "qj":"s", "qk":"", "ql":"", "qm":"lt", "qn":"", "qo":"", "qp":"", "qq":"s", "qr":"", "qs":"", "qt":"s", "qu":"s", "qv":"rb", "qw":"lb", "qx":"s", "qy":"s", "qz":"s", "q1":"rb", "q2":"", "q3":"lb", "q4":"s",
  "ra":"s", "rb":"s", "rc":"", "rd":"", "re":"", "rf":"", "rg":"", "rh":"", "ri":"lb", "rj":"rt", "rk":"", "rl":"", "rm":"", "rn":"st", "ro":"", "rp":"", "rq":"", "rr":"st", "rs":"", "rt":"", "ru":"s", "rv":"s", "rw":"", "rx":"s", "ry":"s", "rz":"s", "r1":"s", "r2":"de", "r3":"", "r4":"s",
  "sa":"s", "sb":"s", "sc":"", "sd":"", "se":"st", "sf":"lb", "sg":"rb", "sh":"", "si":"", "sj":"s", "sk":"rb", "sl":"", "sm":"", "sn":"s", "so":"", "sp":"", "sq":"lb", "sr":"s", "ss":"", "st":"lb", "su":"s", "sv":"", "sw":"", "sx":"", "sy":"s", "sz":"s", "s1":"", "s2":"", "s3":"", "s4":"",
  "ta":"", "tb":"", "tc":"", "td":"", "te":"", "tf":"s", "tg":"", "th":"", "ti":"", "tj":"", "tk":"", "tl":"", "tm":"", "tn":"", "to":"", "tp":"", "tq":"", "tr":"", "ts":"", "tt":"", "tu":"", "tv":"", "tw":"", "tx":"", "ty":"", "tz":"", "t1":"", "t2":"", "t3":"", "t4":"lb",
  "ua":"rb", "ub":"lb", "uc":"rb", "ud":"", "ue":"", "uf":"", "ug":"", "uh":"", "ui":"", "uj":"lb", "uk":"rb", "ul":"", "um":"", "un":"", "uo":"", "up":"", "uq":"", "ur":"", "us":"", "ut":"lb", "uu":"rb", "uv":"", "uw":"st", "ux":"", "uy":"", "uz":"", "u1":"lb", "u2":"rb", "u3":"", "u4":"s",
  "va":"s", "vb":"s", "vc":"s", "vd":"rb", "ve":"", "vf":"st", "vg":"st", "vh":"", "vi":"st", "vj":"lt", "vk":"s", "vl":"rb", "vm":"", "vn":"st", "vo":"", "vp":"st", "vq":"", "vr":"", "vs":"lb", "vt":"s", "vu":"s", "vv":"de", "vw":"s", "vx":"rb", "vy":"", "vz":"lb", "v1":"", "v2":"", "v3":"rb", "v4":"lt",
  "wa":"s", "wb":"s", "wc":"s", "wd":"", "we":"", "wf":"s", "wg":"s", "wh":"de", "wi":"s", "wj":"", "wk":"s", "wl":"", "wm":"", "wn":"s", "wo":"rb", "wp":"lt", "wq":"rb", "wr":"", "ws":"", "wt":"s", "wu":"", "wv":"", "ww":"s", "wx":"s", "wy":"de", "wz":"s", "w1":"", "w2":"", "w3":"lt", "w4":"s",
  "xa":"", "xb":"", "xc":"x", "xd":"", "xe":"", "xf":"lt", "xg":"rt", "xh":"lt", "xi":"rt", "xj":"lb", "xk":"rt", "xl":"", "xm":"", "xn":"lt", "xo":"", "xp":"s", "xq":"", "xr":"", "xs":"lb", "xt":"s", "xu":"rb", "xv":"", "xw":"", "xx":"s", "xy":"", "xz":"", "x1":"", "x2":"lb", "x3":"s", "x4":"s",
  "ya":"rb", "yb":"lb", "yc":"s", "yd":"rb", "ye":"lb", "yf":"s", "yg":"s", "yh":"s", "yi":"s", "yj":"s", "yk":"s", "yl":"rb", "ym":"", "yn":"", "yo":"", "yp":"", "yq":"", "yr":"lb", "ys":"", "yt":"lt", "yu":"", "yv":"", "yw":"lb", "yx":"rt", "yy":"", "yz":"st", "y1":"lb", "y2":"s", "y3":"", "y4":"lt",
  "za":"s", "zb":"s", "zc":"s", "zd":"s", "ze":"s", "zf":"s", "zg":"s", "zh":"s", "zi":"", "zj":"s", "zk":"s", "zl":"", "zm":"", "zn":"", "zo":"", "zp":"", "zq":"", "zr":"", "zs":"lb", "zt":"s", "zu":"rb", "zv":"", "zw":"", "zx":"s", "zy":"", "zz":"", "z1":"s", "z2":"", "z3":"lb", "z4":"s",
  "1a":"s", "1b":"", "1c":"s", "1d":"", "1e":"s", "1f":"rt", "1g":"", "1h":"s", "1i":"rb", "1j":"lt", "1k":"rt", "1l":"", "1m":"", "1n":"", "1o":"st", "1p":"", "1q":"", "1r":"lb", "1s":"s", "1t":"s", "1u":"s", "1v":"rb", "1w":"", "1x":"x", "1y":"", "1z":"", "11":"x", "12":"lb", "13":"s", "14":"s",
  "2a":"rt", "2b":"", "2c":"", "2d":"", "2e":"x", "2f":"", "2g":"", "2h":"", "2i":"s", "2j":"s", "2k":"s", "2l":"rb", "2m":"", "2n":"lb", "2o":"s", "2p":"rb", "2q":"", "2r":"s", "2s":"s", "2t":"s", "2u":"s", "2v":"s", "2w":"de", "2x":"s", "2y":"rb", "2z":"", "21":"lt", "22":"s", "23":"", "24":"",
  "3a":"s", "3b":"", "3c":"", "3d":"lb", "3e":"s", "3f":"rb", "3g":"", "3h":"", "3i":"", "3j":"", "3k":"s", "3l":"s", "3m":"", "3n":"", "3o":"s", "3p":"", "3q":"", "3r":"", "3s":"s", "3t":"s", "3u":"", "3v":"", "3w":"", "3x":"s", "3y":"", "3z":"", "31":"s", "32":"", "33":"", "34":"lb",
  "4a":"", "4b":"", "4c":"", "4d":"", "4e":"", "4f":"", "4g":"", "4h":"", "4i":"", "4j":"", "4k":"", "4l":"", "4m":"", "4n":"", "4o":"", "4p":"", "4q":"", "4r":"", "4s":"", "4t":"", "4u":"", "4v":"", "4w":"", "4x":"", "4y":"", "4z":"", "41":"", "42":"", "43":"", "44":""
               },
         "e" : {
  "aa":"", "ab":"", "ac":"", "ad":"", "ae":"", "af":"", "ag":"", "ah":"", "ai":"", "aj":"", "ak":"", "al":"", "am":"", "an":"", "ao":"", "ap":"", "aq":"", "ar":"", "as":"", "at":"", "au":"", "av":"", "aw":"", "ax":"", "ay":"", "az":"", "a1":"", "a2":"", "a3":"", "a4":"",
  "ba":"", "ab":"", "ac":"", "ad":"", "ae":"", "af":"", "ag":"", "ah":"", "ai":"", "aj":"", "ak":"", "al":"", "am":"", "an":"", "ao":"", "ap":"", "aq":"", "ar":"", "as":"", "at":"", "au":"", "av":"", "aw":"", "ax":"", "ay":"", "az":"", "a1":"", "a2":"", "a3":"", "a4":"",
  "ca":"", "cb":"", "cc":"", "cd":"", "ce":"", "cf":"", "cg":"", "ch":"", "ci":"", "cj":"", "ck":"", "cl":"", "cm":"", "cn":"", "co":"", "cp":"", "cq":"", "cr":"", "cs":"", "ct":"", "cu":"", "cv":"", "cw":"", "cx":"", "cy":"", "cz":"", "c1":"", "c2":"", "c3":"", "c4":"",
  "da":"", "db":"", "dc":"", "dd":"", "de":"", "df":"", "dg":"", "dh":"", "di":"", "dj":"", "dk":"", "dl":"", "dm":"", "dn":"", "do":"", "dp":"", "dq":"", "dr":"", "ds":"", "dt":"", "du":"", "dv":"", "dw":"", "dx":"", "dy":"", "dz":"", "d1":"", "d2":"", "d3":"", "d4":"",
  "ea":"", "eb":"", "ec":"", "ed":"", "ee":"", "ef":"", "eg":"", "eh":"", "ei":"", "ej":"", "ek":"", "el":"", "em":"", "en":"", "eo":"", "ep":"", "eq":"", "er":"", "es":"", "et":"", "eu":"", "ev":"", "ew":"", "ex":"", "ey":"", "ez":"", "e1":"", "e2":"", "e3":"", "e4":"",
  "fa":"", "fb":"", "fc":"", "fd":"", "fe":"", "ff":"", "fg":"", "fh":"", "fi":"", "fj":"", "fk":"", "fl":"", "fm":"", "fn":"", "fo":"", "fp":"", "fq":"", "fr":"", "fs":"", "ft":"", "fu":"", "fv":"", "fw":"", "fx":"", "fy":"", "fz":"", "f1":"", "f2":"", "f3":"", "f4":"",
  "ga":"", "gb":"", "gc":"", "gd":"", "ge":"", "gf":"", "gg":"", "gh":"", "gi":"", "gj":"", "gk":"", "gl":"", "gm":"", "gn":"", "go":"", "gp":"", "gq":"", "gr":"", "gs":"", "gt":"", "gu":"", "gv":"", "gw":"", "gx":"", "gy":"", "gz":"", "g1":"", "g2":"", "g3":"", "g4":"",
  "ha":"", "hb":"", "hc":"", "hd":"", "he":"", "hf":"", "hg":"", "hh":"", "hi":"", "hj":"", "hk":"", "hl":"", "hm":"", "hn":"", "ho":"", "hp":"", "hq":"", "hr":"", "hs":"", "ht":"", "hu":"", "hv":"", "hw":"", "hx":"", "hy":"", "hz":"", "h1":"", "h2":"", "h3":"", "h4":"",
  "ia":"", "ib":"", "ic":"", "id":"", "ie":"", "if":"", "ig":"", "ih":"", "ii":"", "ij":"", "ik":"", "il":"", "im":"", "in":"", "io":"", "ip":"", "iq":"", "ir":"", "is":"", "it":"", "iu":"", "iv":"", "iw":"", "ix":"", "iy":"", "iz":"", "i1":"", "i2":"", "i3":"", "i4":"",
  "ja":"", "jb":"", "jc":"", "jd":"", "je":"", "jf":"", "jg":"", "jh":"", "ji":"", "jj":"", "jk":"", "jl":"", "jm":"", "jn":"", "jo":"", "jp":"", "jq":"", "jr":"", "js":"", "jt":"", "ju":"", "jv":"", "jw":"", "jx":"", "jy":"", "jz":"", "j1":"", "j2":"", "j3":"", "j4":"",
  "ka":"", "kb":"", "kc":"", "kd":"", "ke":"", "kf":"", "kg":"", "kh":"", "ki":"", "kj":"", "kk":"", "kl":"", "km":"", "kn":"", "ko":"", "kp":"", "kq":"", "kr":"", "ks":"", "kt":"", "ku":"", "kv":"", "kw":"", "kx":"", "ky":"", "kz":"", "k1":"", "k2":"", "k3":"", "k4":"",
  "la":"", "lb":"", "lc":"", "ld":"", "le":"", "lf":"", "lg":"", "lh":"", "li":"", "lj":"", "lk":"", "ll":"", "lm":"", "ln":"", "lo":"", "lp":"", "lq":"", "lr":"", "ls":"", "lt":"", "lu":"", "lv":"", "lw":"", "lx":"", "ly":"", "lz":"", "l1":"", "l2":"", "l3":"", "l4":"",
  "ma":"", "mb":"", "mc":"", "md":"", "me":"", "mf":"", "mg":"", "mh":"", "mi":"", "mj":"", "mk":"", "ml":"", "mm":"", "mn":"", "mo":"", "mp":"", "mq":"", "mr":"", "ms":"", "mt":"", "mu":"", "mv":"", "mw":"", "mx":"", "my":"", "mz":"", "m1":"", "m2":"", "m3":"", "m4":"",
  "na":"", "nb":"", "nc":"", "nd":"", "ne":"", "nf":"", "ng":"", "nh":"", "ni":"", "nj":"", "nk":"", "nl":"", "nm":"", "nn":"", "no":"", "np":"", "nq":"", "nr":"", "ns":"", "nt":"", "nu":"", "nv":"", "nw":"", "nx":"", "ny":"", "nz":"", "n1":"", "n2":"", "n3":"", "n4":"",
  "oa":"", "ob":"", "oc":"", "od":"", "oe":"", "of":"", "og":"", "oh":"", "oi":"", "oj":"", "ok":"", "ol":"", "om":"", "on":"", "oo":"", "op":"", "oq":"", "or":"", "os":"", "ot":"", "ou":"", "ov":"", "ow":"", "ox":"", "oy":"", "oz":"", "o1":"", "o2":"", "o3":"", "o4":"",
  "pa":"", "pb":"", "pc":"", "pd":"", "pe":"", "pf":"", "pg":"", "ph":"", "pi":"", "pj":"", "pk":"", "pl":"", "pm":"", "pn":"", "po":"", "pp":"", "pq":"", "pr":"", "ps":"", "pt":"", "pu":"", "pv":"", "pw":"", "px":"", "py":"", "pz":"", "p1":"", "p2":"", "p3":"", "p4":"",
  "qa":"", "qb":"", "qc":"", "qd":"", "qe":"", "qf":"", "qg":"", "qh":"", "qi":"", "qj":"", "qk":"", "ql":"", "qm":"", "qn":"", "qo":"", "qp":"", "qq":"", "qr":"", "qs":"", "qt":"", "qu":"", "qv":"", "qw":"", "qx":"", "qy":"", "qz":"", "q1":"", "q2":"", "q3":"", "q4":"",
  "ra":"", "rb":"", "rc":"", "rd":"", "re":"", "rf":"", "rg":"", "rh":"", "ri":"", "rj":"", "rk":"", "rl":"", "rm":"", "rn":"", "ro":"", "rp":"", "rq":"", "rr":"", "rs":"", "rt":"", "ru":"", "rv":"", "rw":"", "rx":"", "ry":"", "rz":"", "r1":"", "r2":"", "r3":"", "r4":"",
  "sa":"", "sb":"", "sc":"", "sd":"", "se":"", "sf":"", "sg":"", "sh":"", "si":"", "sj":"", "sk":"", "sl":"", "sm":"", "sn":"", "so":"", "sp":"", "sq":"", "sr":"", "ss":"", "st":"", "su":"", "sv":"", "sw":"", "sx":"", "sy":"", "sz":"", "s1":"", "s2":"", "s3":"", "s4":"",
  "ta":"", "tb":"", "tc":"", "td":"", "te":"", "tf":"", "tg":"", "th":"", "ti":"", "tj":"", "tk":"", "tl":"", "tm":"", "tn":"", "to":"", "tp":"", "tq":"", "tr":"", "ts":"", "tt":"", "tu":"", "tv":"", "tw":"", "tx":"", "ty":"", "tz":"", "t1":"", "t2":"", "t3":"", "t4":"",
  "ua":"", "ub":"", "uc":"", "ud":"", "ue":"", "uf":"", "ug":"", "uh":"", "ui":"", "uj":"", "uk":"", "ul":"", "um":"", "un":"", "uo":"", "up":"", "uq":"", "ur":"", "us":"", "ut":"", "uu":"", "uv":"", "uw":"", "ux":"", "uy":"", "uz":"", "u1":"", "u2":"", "u3":"", "u4":"",
  "va":"", "vb":"", "vc":"", "vd":"", "ve":"", "vf":"", "vg":"", "vh":"", "vi":"", "vj":"", "vk":"", "vl":"", "vm":"", "vn":"", "vo":"", "vp":"", "vq":"", "vr":"", "vs":"", "vt":"", "vu":"", "vv":"", "vw":"", "vx":"", "vy":"", "vz":"", "v1":"", "v2":"", "v3":"", "v4":"",
  "wa":"", "wb":"", "wc":"", "wd":"", "we":"", "wf":"", "wg":"", "wh":"", "wi":"", "wj":"", "wk":"", "wl":"", "wm":"", "wn":"", "wo":"", "wp":"", "wq":"", "wr":"", "ws":"", "wt":"", "wu":"", "wv":"", "ww":"", "wx":"", "wy":"", "wz":"", "w1":"", "w2":"", "w3":"", "w4":"",
  "xa":"", "xb":"", "xc":"", "xd":"", "xe":"", "xf":"", "xg":"", "xh":"", "xi":"", "xj":"", "xk":"", "xl":"", "xm":"", "xn":"", "xo":"", "xp":"", "xq":"", "xr":"", "xs":"", "xt":"", "xu":"", "xv":"", "xw":"", "xx":"", "xy":"", "xz":"", "x1":"", "x2":"", "x3":"", "x4":"",
  "ya":"", "yb":"", "yc":"", "yd":"", "ye":"", "yf":"", "yg":"", "yh":"", "yi":"", "yj":"", "yk":"", "yl":"", "ym":"", "yn":"", "yo":"", "yp":"", "yq":"", "yr":"", "ys":"", "yt":"", "yu":"", "yv":"", "yw":"", "yx":"", "yy":"", "yz":"", "y1":"", "y2":"", "y3":"", "y4":"",
  "za":"", "zb":"", "zc":"", "zd":"", "ze":"", "zf":"", "zg":"", "zh":"", "zi":"", "zj":"", "zk":"", "zl":"", "zm":"", "zn":"", "zo":"", "zp":"", "zq":"", "zr":"", "zs":"", "zt":"", "zu":"", "zv":"", "zw":"", "zx":"", "zy":"", "zz":"", "z1":"", "z2":"", "z3":"", "z4":"",
  "1a":"", "1b":"", "1c":"", "1d":"", "1e":"", "1f":"", "1g":"", "1h":"", "1i":"", "1j":"", "1k":"", "1l":"", "1m":"", "1n":"", "1o":"", "1p":"", "1q":"", "1r":"", "1s":"", "1t":"", "1u":"", "1v":"", "1w":"", "1x":"", "1y":"", "1z":"", "11":"", "12":"", "13":"", "14":"",
  "2a":"", "2b":"", "2c":"", "2d":"", "2e":"", "2f":"", "2g":"", "2h":"", "2i":"", "2j":"", "2k":"", "2l":"", "2m":"", "2n":"", "2o":"", "2p":"", "2q":"", "2r":"", "2s":"", "2t":"", "2u":"", "2v":"", "2w":"", "2x":"", "2y":"", "2z":"", "21":"", "22":"", "23":"", "24":"",
  "3a":"", "3b":"", "3c":"", "3d":"", "3e":"", "3f":"", "3g":"", "3h":"", "3i":"", "3j":"", "3k":"", "3l":"", "3m":"", "3n":"", "3o":"", "3p":"", "3q":"", "3r":"", "3s":"", "3t":"", "3u":"", "3v":"", "3w":"", "3x":"", "3y":"", "3z":"", "31":"", "32":"", "33":"", "34":"",
               },
         "s" : {
  "aa":"", "ab":"", "ac":"", "ad":"", "ae":"", "af":"", "ag":"", "ah":"", "ai":"", "aj":"", "ak":"", "al":"", "am":"", "an":"", "ao":"", "ap":"", "aq":"", "ar":"", "as":"", "at":"", "au":"", "av":"", "aw":"", "ax":"", "ay":"", "az":"", "a1":"", "a2":"", "a3":"", "a4":"",
  "ba":"", "ab":"", "ac":"", "ad":"", "ae":"", "af":"", "ag":"", "ah":"", "ai":"", "aj":"", "ak":"", "al":"", "am":"", "an":"", "ao":"", "ap":"", "aq":"", "ar":"", "as":"", "at":"", "au":"", "av":"", "aw":"", "ax":"", "ay":"", "az":"", "a1":"", "a2":"", "a3":"", "a4":"",
  "ca":"", "cb":"", "cc":"", "cd":"", "ce":"", "cf":"", "cg":"", "ch":"", "ci":"", "cj":"", "ck":"", "cl":"", "cm":"", "cn":"", "co":"", "cp":"", "cq":"", "cr":"", "cs":"", "ct":"", "cu":"", "cv":"", "cw":"", "cx":"", "cy":"", "cz":"", "c1":"", "c2":"", "c3":"", "c4":"",
  "da":"", "db":"", "dc":"", "dd":"", "de":"", "df":"", "dg":"", "dh":"", "di":"", "dj":"", "dk":"", "dl":"", "dm":"", "dn":"", "do":"", "dp":"", "dq":"", "dr":"", "ds":"", "dt":"", "du":"", "dv":"", "dw":"", "dx":"", "dy":"", "dz":"", "d1":"", "d2":"", "d3":"", "d4":"",
  "ea":"", "eb":"", "ec":"", "ed":"", "ee":"", "ef":"", "eg":"", "eh":"", "ei":"", "ej":"", "ek":"", "el":"", "em":"", "en":"", "eo":"", "ep":"", "eq":"", "er":"", "es":"", "et":"", "eu":"", "ev":"", "ew":"", "ex":"", "ey":"", "ez":"", "e1":"", "e2":"", "e3":"", "e4":"",
  "fa":"", "fb":"", "fc":"", "fd":"", "fe":"", "ff":"", "fg":"", "fh":"", "fi":"", "fj":"", "fk":"", "fl":"", "fm":"", "fn":"", "fo":"", "fp":"", "fq":"", "fr":"", "fs":"", "ft":"", "fu":"", "fv":"", "fw":"", "fx":"", "fy":"", "fz":"", "f1":"", "f2":"", "f3":"", "f4":"",
  "ga":"", "gb":"", "gc":"", "gd":"", "ge":"", "gf":"", "gg":"", "gh":"", "gi":"", "gj":"", "gk":"", "gl":"", "gm":"", "gn":"", "go":"", "gp":"", "gq":"", "gr":"", "gs":"", "gt":"", "gu":"", "gv":"", "gw":"", "gx":"", "gy":"", "gz":"", "g1":"", "g2":"", "g3":"", "g4":"",
  "ha":"", "hb":"", "hc":"", "hd":"", "he":"", "hf":"", "hg":"", "hh":"", "hi":"", "hj":"", "hk":"", "hl":"", "hm":"", "hn":"", "ho":"", "hp":"", "hq":"", "hr":"", "hs":"", "ht":"", "hu":"", "hv":"", "hw":"", "hx":"", "hy":"", "hz":"", "h1":"", "h2":"", "h3":"", "h4":"",
  "ia":"", "ib":"", "ic":"", "id":"", "ie":"", "if":"", "ig":"", "ih":"", "ii":"", "ij":"", "ik":"", "il":"", "im":"", "in":"", "io":"", "ip":"", "iq":"", "ir":"", "is":"", "it":"", "iu":"", "iv":"", "iw":"", "ix":"", "iy":"", "iz":"", "i1":"", "i2":"", "i3":"", "i4":"",
  "ja":"", "jb":"", "jc":"", "jd":"", "je":"", "jf":"", "jg":"", "jh":"", "ji":"", "jj":"", "jk":"", "jl":"", "jm":"", "jn":"", "jo":"", "jp":"", "jq":"", "jr":"", "js":"", "jt":"", "ju":"", "jv":"", "jw":"", "jx":"", "jy":"", "jz":"", "j1":"", "j2":"", "j3":"", "j4":"",
  "ka":"", "kb":"", "kc":"", "kd":"", "ke":"", "kf":"", "kg":"", "kh":"", "ki":"", "kj":"", "kk":"", "kl":"", "km":"", "kn":"", "ko":"", "kp":"", "kq":"", "kr":"", "ks":"", "kt":"", "ku":"", "kv":"", "kw":"", "kx":"", "ky":"", "kz":"", "k1":"", "k2":"", "k3":"", "k4":"",
  "la":"", "lb":"", "lc":"", "ld":"", "le":"", "lf":"", "lg":"", "lh":"", "li":"", "lj":"", "lk":"", "ll":"", "lm":"", "ln":"", "lo":"", "lp":"", "lq":"", "lr":"", "ls":"", "lt":"", "lu":"", "lv":"", "lw":"", "lx":"", "ly":"", "lz":"", "l1":"", "l2":"", "l3":"", "l4":"",
  "ma":"", "mb":"", "mc":"", "md":"", "me":"", "mf":"", "mg":"", "mh":"", "mi":"", "mj":"", "mk":"", "ml":"", "mm":"", "mn":"", "mo":"", "mp":"", "mq":"", "mr":"", "ms":"", "mt":"", "mu":"", "mv":"", "mw":"", "mx":"", "my":"", "mz":"", "m1":"", "m2":"", "m3":"", "m4":"",
  "na":"", "nb":"", "nc":"", "nd":"", "ne":"", "nf":"", "ng":"", "nh":"", "ni":"", "nj":"", "nk":"", "nl":"", "nm":"", "nn":"", "no":"", "np":"", "nq":"", "nr":"", "ns":"", "nt":"", "nu":"", "nv":"", "nw":"", "nx":"", "ny":"", "nz":"", "n1":"", "n2":"", "n3":"", "n4":"",
  "oa":"", "ob":"", "oc":"", "od":"", "oe":"", "of":"", "og":"", "oh":"", "oi":"", "oj":"", "ok":"", "ol":"", "om":"", "on":"", "oo":"", "op":"", "oq":"", "or":"", "os":"", "ot":"", "ou":"", "ov":"", "ow":"", "ox":"", "oy":"", "oz":"", "o1":"", "o2":"", "o3":"", "o4":"",
  "pa":"", "pb":"", "pc":"", "pd":"", "pe":"", "pf":"", "pg":"", "ph":"", "pi":"", "pj":"", "pk":"", "pl":"", "pm":"", "pn":"", "po":"", "pp":"", "pq":"", "pr":"", "ps":"", "pt":"", "pu":"", "pv":"", "pw":"", "px":"", "py":"", "pz":"", "p1":"", "p2":"", "p3":"", "p4":"",
  "qa":"", "qb":"", "qc":"", "qd":"", "qe":"", "qf":"", "qg":"", "qh":"", "qi":"", "qj":"", "qk":"", "ql":"", "qm":"", "qn":"", "qo":"", "qp":"", "qq":"", "qr":"", "qs":"", "qt":"", "qu":"", "qv":"", "qw":"", "qx":"", "qy":"", "qz":"", "q1":"", "q2":"", "q3":"", "q4":"",
  "ra":"", "rb":"", "rc":"", "rd":"", "re":"", "rf":"", "rg":"", "rh":"", "ri":"", "rj":"", "rk":"", "rl":"", "rm":"", "rn":"", "ro":"", "rp":"", "rq":"", "rr":"", "rs":"", "rt":"", "ru":"", "rv":"", "rw":"", "rx":"", "ry":"", "rz":"", "r1":"", "r2":"", "r3":"", "r4":"",
  "sa":"", "sb":"", "sc":"", "sd":"", "se":"", "sf":"", "sg":"", "sh":"", "si":"", "sj":"", "sk":"", "sl":"", "sm":"", "sn":"", "so":"", "sp":"", "sq":"", "sr":"", "ss":"", "st":"", "su":"", "sv":"", "sw":"", "sx":"", "sy":"", "sz":"", "s1":"", "s2":"", "s3":"", "s4":"",
  "ta":"", "tb":"", "tc":"", "td":"", "te":"", "tf":"", "tg":"", "th":"", "ti":"", "tj":"", "tk":"", "tl":"", "tm":"", "tn":"", "to":"", "tp":"", "tq":"", "tr":"", "ts":"", "tt":"", "tu":"", "tv":"", "tw":"", "tx":"", "ty":"", "tz":"", "t1":"", "t2":"", "t3":"", "t4":"",
  "ua":"", "ub":"", "uc":"", "ud":"", "ue":"", "uf":"", "ug":"", "uh":"", "ui":"", "uj":"", "uk":"", "ul":"", "um":"", "un":"", "uo":"", "up":"", "uq":"", "ur":"", "us":"", "ut":"", "uu":"", "uv":"", "uw":"", "ux":"", "uy":"", "uz":"", "u1":"", "u2":"", "u3":"", "u4":"",
  "va":"", "vb":"", "vc":"", "vd":"", "ve":"", "vf":"", "vg":"", "vh":"", "vi":"", "vj":"", "vk":"", "vl":"", "vm":"", "vn":"", "vo":"", "vp":"", "vq":"", "vr":"", "vs":"", "vt":"", "vu":"", "vv":"", "vw":"", "vx":"", "vy":"", "vz":"", "v1":"", "v2":"", "v3":"", "v4":"",
  "wa":"", "wb":"", "wc":"", "wd":"", "we":"", "wf":"", "wg":"", "wh":"", "wi":"", "wj":"", "wk":"", "wl":"", "wm":"", "wn":"", "wo":"", "wp":"", "wq":"", "wr":"", "ws":"", "wt":"", "wu":"", "wv":"", "ww":"", "wx":"", "wy":"", "wz":"", "w1":"", "w2":"", "w3":"", "w4":"",
  "xa":"", "xb":"", "xc":"", "xd":"", "xe":"", "xf":"", "xg":"", "xh":"", "xi":"", "xj":"", "xk":"", "xl":"", "xm":"", "xn":"", "xo":"", "xp":"", "xq":"", "xr":"", "xs":"", "xt":"", "xu":"", "xv":"", "xw":"", "xx":"", "xy":"", "xz":"", "x1":"", "x2":"", "x3":"", "x4":"",
  "ya":"", "yb":"", "yc":"", "yd":"", "ye":"", "yf":"", "yg":"", "yh":"", "yi":"", "yj":"", "yk":"", "yl":"", "ym":"", "yn":"", "yo":"", "yp":"", "yq":"", "yr":"", "ys":"", "yt":"", "yu":"", "yv":"", "yw":"", "yx":"", "yy":"", "yz":"", "y1":"", "y2":"", "y3":"", "y4":"",
  "za":"", "zb":"", "zc":"", "zd":"", "ze":"", "zf":"", "zg":"", "zh":"", "zi":"", "zj":"", "zk":"", "zl":"", "zm":"", "zn":"", "zo":"", "zp":"", "zq":"", "zr":"", "zs":"", "zt":"", "zu":"", "zv":"", "zw":"", "zx":"", "zy":"", "zz":"", "z1":"", "z2":"", "z3":"", "z4":"",
  "1a":"", "1b":"", "1c":"", "1d":"", "1e":"", "1f":"", "1g":"", "1h":"", "1i":"", "1j":"", "1k":"", "1l":"", "1m":"", "1n":"", "1o":"", "1p":"", "1q":"", "1r":"", "1s":"", "1t":"", "1u":"", "1v":"", "1w":"", "1x":"", "1y":"", "1z":"", "11":"", "12":"", "13":"", "14":"",
  "2a":"", "2b":"", "2c":"", "2d":"", "2e":"", "2f":"", "2g":"", "2h":"", "2i":"", "2j":"", "2k":"", "2l":"", "2m":"", "2n":"", "2o":"", "2p":"", "2q":"", "2r":"", "2s":"", "2t":"", "2u":"", "2v":"", "2w":"", "2x":"", "2y":"", "2z":"", "21":"", "22":"", "23":"", "24":"",
  "3a":"", "3b":"", "3c":"", "3d":"", "3e":"", "3f":"", "3g":"", "3h":"", "3i":"", "3j":"", "3k":"", "3l":"", "3m":"", "3n":"", "3o":"", "3p":"", "3q":"", "3r":"", "3s":"", "3t":"", "3u":"", "3v":"", "3w":"", "3x":"", "3y":"", "3z":"", "31":"", "32":"", "33":"", "34":"",
  "4a":"", "4b":"", "4c":"", "4d":"", "4e":"", "4f":"", "4g":"", "4h":"", "4i":"", "4j":"", "4k":"", "4l":"", "4m":"", "4n":"", "4o":"", "4p":"", "4q":"", "4r":"", "4s":"", "4t":"", "4u":"", "4v":"", "4w":"", "4x":"", "4y":"", "4z":"", "41":"", "42":"", "43":"", "44":""
               },
         "w" : {
  "aa":"", "ab":"", "ac":"", "ad":"", "ae":"", "af":"", "ag":"", "ah":"", "ai":"", "aj":"", "ak":"", "al":"", "am":"", "an":"", "ao":"", "ap":"", "aq":"", "ar":"", "as":"", "at":"", "au":"", "av":"", "aw":"", "ax":"", "ay":"", "az":"", "a1":"", "a2":"", "a3":"", "a4":"",
  "ba":"", "ab":"", "ac":"", "ad":"", "ae":"", "af":"", "ag":"", "ah":"", "ai":"", "aj":"", "ak":"", "al":"", "am":"", "an":"", "ao":"", "ap":"", "aq":"", "ar":"", "as":"", "at":"", "au":"", "av":"", "aw":"", "ax":"", "ay":"", "az":"", "a1":"", "a2":"", "a3":"", "a4":"",
  "ca":"", "cb":"", "cc":"", "cd":"", "ce":"", "cf":"", "cg":"", "ch":"", "ci":"", "cj":"", "ck":"", "cl":"", "cm":"", "cn":"", "co":"", "cp":"", "cq":"", "cr":"", "cs":"", "ct":"", "cu":"", "cv":"", "cw":"", "cx":"", "cy":"", "cz":"", "c1":"", "c2":"", "c3":"", "c4":"",
  "da":"", "db":"", "dc":"", "dd":"", "de":"", "df":"", "dg":"", "dh":"", "di":"", "dj":"", "dk":"", "dl":"", "dm":"", "dn":"", "do":"", "dp":"", "dq":"", "dr":"", "ds":"", "dt":"", "du":"", "dv":"", "dw":"", "dx":"", "dy":"", "dz":"", "d1":"", "d2":"", "d3":"", "d4":"",
  "ea":"", "eb":"", "ec":"", "ed":"", "ee":"", "ef":"", "eg":"", "eh":"", "ei":"", "ej":"", "ek":"", "el":"", "em":"", "en":"", "eo":"", "ep":"", "eq":"", "er":"", "es":"", "et":"", "eu":"", "ev":"", "ew":"", "ex":"", "ey":"", "ez":"", "e1":"", "e2":"", "e3":"", "e4":"",
  "fa":"", "fb":"", "fc":"", "fd":"", "fe":"", "ff":"", "fg":"", "fh":"", "fi":"", "fj":"", "fk":"", "fl":"", "fm":"", "fn":"", "fo":"", "fp":"", "fq":"", "fr":"", "fs":"", "ft":"", "fu":"", "fv":"", "fw":"", "fx":"", "fy":"", "fz":"", "f1":"", "f2":"", "f3":"", "f4":"",
  "ga":"", "gb":"", "gc":"", "gd":"", "ge":"", "gf":"", "gg":"", "gh":"", "gi":"", "gj":"", "gk":"", "gl":"", "gm":"", "gn":"", "go":"", "gp":"", "gq":"", "gr":"", "gs":"", "gt":"", "gu":"", "gv":"", "gw":"", "gx":"", "gy":"", "gz":"", "g1":"", "g2":"", "g3":"", "g4":"",
  "ha":"", "hb":"", "hc":"", "hd":"", "he":"", "hf":"", "hg":"", "hh":"", "hi":"", "hj":"", "hk":"", "hl":"", "hm":"", "hn":"", "ho":"", "hp":"", "hq":"", "hr":"", "hs":"", "ht":"", "hu":"", "hv":"", "hw":"", "hx":"", "hy":"", "hz":"", "h1":"", "h2":"", "h3":"", "h4":"",
  "ia":"", "ib":"", "ic":"", "id":"", "ie":"", "if":"", "ig":"", "ih":"", "ii":"", "ij":"", "ik":"", "il":"", "im":"", "in":"", "io":"", "ip":"", "iq":"", "ir":"", "is":"", "it":"", "iu":"", "iv":"", "iw":"", "ix":"", "iy":"", "iz":"", "i1":"", "i2":"", "i3":"", "i4":"",
  "ja":"", "jb":"", "jc":"", "jd":"", "je":"", "jf":"", "jg":"", "jh":"", "ji":"", "jj":"", "jk":"", "jl":"", "jm":"", "jn":"", "jo":"", "jp":"", "jq":"", "jr":"", "js":"", "jt":"", "ju":"", "jv":"", "jw":"", "jx":"", "jy":"", "jz":"", "j1":"", "j2":"", "j3":"", "j4":"",
  "ka":"", "kb":"", "kc":"", "kd":"", "ke":"", "kf":"", "kg":"", "kh":"", "ki":"", "kj":"", "kk":"", "kl":"", "km":"", "kn":"", "ko":"", "kp":"", "kq":"", "kr":"", "ks":"", "kt":"", "ku":"", "kv":"", "kw":"", "kx":"", "ky":"", "kz":"", "k1":"", "k2":"", "k3":"", "k4":"",
  "la":"", "lb":"", "lc":"", "ld":"", "le":"", "lf":"", "lg":"", "lh":"", "li":"", "lj":"", "lk":"", "ll":"", "lm":"", "ln":"", "lo":"", "lp":"", "lq":"", "lr":"", "ls":"", "lt":"", "lu":"", "lv":"", "lw":"", "lx":"", "ly":"", "lz":"", "l1":"", "l2":"", "l3":"", "l4":"",
  "ma":"", "mb":"", "mc":"", "md":"", "me":"", "mf":"", "mg":"", "mh":"", "mi":"", "mj":"", "mk":"", "ml":"", "mm":"", "mn":"", "mo":"", "mp":"", "mq":"", "mr":"", "ms":"", "mt":"", "mu":"", "mv":"", "mw":"", "mx":"", "my":"", "mz":"", "m1":"", "m2":"", "m3":"", "m4":"",
  "na":"", "nb":"", "nc":"", "nd":"", "ne":"", "nf":"", "ng":"", "nh":"", "ni":"", "nj":"", "nk":"", "nl":"", "nm":"", "nn":"", "no":"", "np":"", "nq":"", "nr":"", "ns":"", "nt":"", "nu":"", "nv":"", "nw":"", "nx":"", "ny":"", "nz":"", "n1":"", "n2":"", "n3":"", "n4":"",
  "oa":"", "ob":"", "oc":"", "od":"", "oe":"", "of":"", "og":"", "oh":"", "oi":"", "oj":"", "ok":"", "ol":"", "om":"", "on":"", "oo":"", "op":"", "oq":"", "or":"", "os":"", "ot":"", "ou":"", "ov":"", "ow":"", "ox":"", "oy":"", "oz":"", "o1":"", "o2":"", "o3":"", "o4":"",
  "pa":"", "pb":"", "pc":"", "pd":"", "pe":"", "pf":"", "pg":"", "ph":"", "pi":"", "pj":"", "pk":"", "pl":"", "pm":"", "pn":"", "po":"", "pp":"", "pq":"", "pr":"", "ps":"", "pt":"", "pu":"", "pv":"", "pw":"", "px":"", "py":"", "pz":"", "p1":"", "p2":"", "p3":"", "p4":"",
  "qa":"", "qb":"", "qc":"", "qd":"", "qe":"", "qf":"", "qg":"", "qh":"", "qi":"", "qj":"", "qk":"", "ql":"", "qm":"", "qn":"", "qo":"", "qp":"", "qq":"", "qr":"", "qs":"", "qt":"", "qu":"", "qv":"", "qw":"", "qx":"", "qy":"", "qz":"", "q1":"", "q2":"", "q3":"", "q4":"",
  "ra":"", "rb":"", "rc":"", "rd":"", "re":"", "rf":"", "rg":"", "rh":"", "ri":"", "rj":"", "rk":"", "rl":"", "rm":"", "rn":"", "ro":"", "rp":"", "rq":"", "rr":"", "rs":"", "rt":"", "ru":"", "rv":"", "rw":"", "rx":"", "ry":"", "rz":"", "r1":"", "r2":"", "r3":"", "r4":"",
  "sa":"", "sb":"", "sc":"", "sd":"", "se":"", "sf":"", "sg":"", "sh":"", "si":"", "sj":"", "sk":"", "sl":"", "sm":"", "sn":"", "so":"", "sp":"", "sq":"", "sr":"", "ss":"", "st":"", "su":"", "sv":"", "sw":"", "sx":"", "sy":"", "sz":"", "s1":"", "s2":"", "s3":"", "s4":"",
  "ta":"", "tb":"", "tc":"", "td":"", "te":"", "tf":"", "tg":"", "th":"", "ti":"", "tj":"", "tk":"", "tl":"", "tm":"", "tn":"", "to":"", "tp":"", "tq":"", "tr":"", "ts":"", "tt":"", "tu":"", "tv":"", "tw":"", "tx":"", "ty":"", "tz":"", "t1":"", "t2":"", "t3":"", "t4":"",
  "ua":"", "ub":"", "uc":"", "ud":"", "ue":"", "uf":"", "ug":"", "uh":"", "ui":"", "uj":"", "uk":"", "ul":"", "um":"", "un":"", "uo":"", "up":"", "uq":"", "ur":"", "us":"", "ut":"", "uu":"", "uv":"", "uw":"", "ux":"", "uy":"", "uz":"", "u1":"", "u2":"", "u3":"", "u4":"",
  "va":"", "vb":"", "vc":"", "vd":"", "ve":"", "vf":"", "vg":"", "vh":"", "vi":"", "vj":"", "vk":"", "vl":"", "vm":"", "vn":"", "vo":"", "vp":"", "vq":"", "vr":"", "vs":"", "vt":"", "vu":"", "vv":"", "vw":"", "vx":"", "vy":"", "vz":"", "v1":"", "v2":"", "v3":"", "v4":"",
  "wa":"", "wb":"", "wc":"", "wd":"", "we":"", "wf":"", "wg":"", "wh":"", "wi":"", "wj":"", "wk":"", "wl":"", "wm":"", "wn":"", "wo":"", "wp":"", "wq":"", "wr":"", "ws":"", "wt":"", "wu":"", "wv":"", "ww":"", "wx":"", "wy":"", "wz":"", "w1":"", "w2":"", "w3":"", "w4":"",
  "xa":"", "xb":"", "xc":"", "xd":"", "xe":"", "xf":"", "xg":"", "xh":"", "xi":"", "xj":"", "xk":"", "xl":"", "xm":"", "xn":"", "xo":"", "xp":"", "xq":"", "xr":"", "xs":"", "xt":"", "xu":"", "xv":"", "xw":"", "xx":"", "xy":"", "xz":"", "x1":"", "x2":"", "x3":"", "x4":"",
  "ya":"", "yb":"", "yc":"", "yd":"", "ye":"", "yf":"", "yg":"", "yh":"", "yi":"", "yj":"", "yk":"", "yl":"", "ym":"", "yn":"", "yo":"", "yp":"", "yq":"", "yr":"", "ys":"", "yt":"", "yu":"", "yv":"", "yw":"", "yx":"", "yy":"", "yz":"", "y1":"", "y2":"", "y3":"", "y4":"",
  "za":"", "zb":"", "zc":"", "zd":"", "ze":"", "zf":"", "zg":"", "zh":"", "zi":"", "zj":"", "zk":"", "zl":"", "zm":"", "zn":"", "zo":"", "zp":"", "zq":"", "zr":"", "zs":"", "zt":"", "zu":"", "zv":"", "zw":"", "zx":"", "zy":"", "zz":"", "z1":"", "z2":"", "z3":"", "z4":"",
  "1a":"", "1b":"", "1c":"", "1d":"", "1e":"", "1f":"", "1g":"", "1h":"", "1i":"", "1j":"", "1k":"", "1l":"", "1m":"", "1n":"", "1o":"", "1p":"", "1q":"", "1r":"", "1s":"", "1t":"", "1u":"", "1v":"", "1w":"", "1x":"", "1y":"", "1z":"", "11":"", "12":"", "13":"", "14":"",
  "2a":"", "2b":"", "2c":"", "2d":"", "2e":"", "2f":"", "2g":"", "2h":"", "2i":"", "2j":"", "2k":"", "2l":"", "2m":"", "2n":"", "2o":"", "2p":"", "2q":"", "2r":"", "2s":"", "2t":"", "2u":"", "2v":"", "2w":"", "2x":"", "2y":"", "2z":"", "21":"", "22":"", "23":"", "24":"",
  "3a":"", "3b":"", "3c":"", "3d":"", "3e":"", "3f":"", "3g":"", "3h":"", "3i":"", "3j":"", "3k":"", "3l":"", "3m":"", "3n":"", "3o":"", "3p":"", "3q":"", "3r":"", "3s":"", "3t":"", "3u":"", "3v":"", "3w":"", "3x":"", "3y":"", "3z":"", "31":"", "32":"", "33":"", "34":"",
  "4a":"", "4b":"", "4c":"", "4d":"", "4e":"", "4f":"", "4g":"", "4h":"", "4i":"", "4j":"", "4k":"", "4l":"", "4m":"", "4n":"", "4o":"", "4p":"", "4q":"", "4r":"", "4s":"", "4t":"", "4u":"", "4v":"", "4w":"", "4x":"", "4y":"", "4z":"", "41":"", "42":"", "43":"", "44":""
               } };
