import requests
from bs4 import BeautifulSoup
import re

channels = [
		"https://t.me/s/v2rayng_org",
		"https://t.me/s/v2rayngvpn",
		"https://t.me/s/flyv2ray",
		"https://t.me/s/v2ray_outlineir",
		"https://t.me/s/v2_vmess",
		"https://t.me/s/FreeVlessVpn",
		"https://t.me/s/freeland8",
		"https://t.me/s/vmess_vless_v2rayng",
		"https://t.me/s/PrivateVPNs",
		"https://t.me/s/vmessiran",
		"https://t.me/s/Outline_Vpn",
		"https://t.me/s/vmessq",
		"https://t.me/s/WeePeeN",
		"https://t.me/s/V2rayNG3",
		"https://t.me/s/ShadowsocksM",
		"https://t.me/s/shadowsocksshop",
		"https://t.me/s/v2rayan",
		"https://t.me/s/ShadowSocks_s",
		"https://t.me/s/VmessProtocol",
		"https://t.me/s/napsternetv_config",
		"https://t.me/s/Easy_Free_VPN",
		"https://t.me/s/V2Ray_FreedomIran",
		"https://t.me/s/V2RAY_VMESS_free",
		"https://t.me/s/v2ray_for_free",
		"https://t.me/s/V2rayN_Free",
		"https://t.me/s/free4allVPN",
		"https://t.me/s/vpn_ocean",
		"https://t.me/s/configV2rayForFree",
		"https://t.me/s/FreeV2rays{all_messages}",
		"https://t.me/s/DigiV2ray",
		"https://t.me/s/v2rayNG_VPN",
		"https://t.me/s/freev2rayssr",
		"https://t.me/s/v2rayn_server",
		"https://t.me/s/Shadowlinkserverr",
		"https://t.me/s/iranvpnet",
		"https://t.me/s/vmess_iran",
		"https://t.me/s/mahsaamoon1",
		"https://t.me/s/V2RAY_NEW",
		"https://t.me/s/v2RayChannel",
		"https://t.me/s/configV2rayNG{all_messages}",
		"https://t.me/s/config_v2ray",
		"https://t.me/s/vpn_proxy_custom",
		"https://t.me/s/vpnmasi{all_messages}",
		"https://t.me/s/v2ray_custom",
		"https://t.me/s/VPNCUSTOMIZE",
		"https://t.me/s/HTTPCustomLand",
		"https://t.me/s/vpn_proxy_custom",
		"https://t.me/s/ViPVpn_v2ray",
		"https://t.me/s/FreeNet1500",
		"https://t.me/s/v2ray_ar{all_messages}",
		"https://t.me/s/beta_v2ray",
		"https://t.me/s/vip_vpn_2022",
		"https://t.me/s/FOX_VPN66",
		"https://t.me/s/VorTexIRN",
		"https://t.me/s/YtTe3la",
		"https://t.me/s/V2RayOxygen",
		"https://t.me/s/Network_442",
		"https://t.me/s/VPN_443",
		"https://t.me/s/v2rayng_v",
		"https://t.me/s/ultrasurf_12",
		"https://t.me/s/iSeqaro{all_messages}",
		"https://t.me/s/frev2rayng",
		"https://t.me/s/frev2ray",
		"https://t.me/s/FreakConfig",
		"https://t.me/s/Awlix_ir",
		"https://t.me/s/v2rayngvpn",
		"https://t.me/s/God_CONFIG{all_messages}",
		"https://t.me/s/Configforvpn01",
		"https://t.me/s/polproxy",
		"https://t.me/s/v2rayvpnchannel",
		"https://t.me/s/proxy_mtm",
		"https://t.me/s/vpn_ioss{all_messages}",
		"https://t.me/s/V2Ray_FreedomIran",
		"https://t.me/s/v2rayfree1",
		"https://t.me/s/free_v2rayyy",
		"https://t.me/s/nx_v2ray",
		"https://t.me/s/nufilter",
		"https://t.me/s/Free_HTTPCustom",
		"https://t.me/s/customv2ray",
		"https://t.me/s/vpn_Nv1",
		"https://t.me/s/AliAlma_GSM{all_messages}",
		"https://t.me/s/reality_daily{all_messages}",
		"https://t.me/s/shopingv2ray",
		"https://t.me/s/v2rayng_vpnrog",
		"https://t.me/s/ServerNett",
		"https://t.me/s/MT_TEAM_IRAN",
		"https://t.me/s/V2ray_Team",
		"https://t.me/s/VpnProsecc",
		"https://t.me/s/ConfigsHUB",
		"https://t.me/s/melov2ray",
		"https://t.me/s/V2pedia",
		"https://t.me/s/FalconPolV2rayNG",
		"https://t.me/s/ShadowProxy66",
		"https://t.me/s/VPNCUSTOMIZE",
		"https://t.me/s/prrofile_purple",
		"https://t.me/s/MsV2ray",
		"https://t.me/s/VlessConfig",
		"https://t.me/s/vless_vmess",
		"https://t.me/s/MehradLearn",
		"https://t.me/s/kingofilter",
		"https://t.me/s/IRN_VPN",
		"https://t.me/s/V2raysFree",
		"https://t.me/s/SvnTeam",
		"https://t.me/s/flyv2ray",
		"https://t.me/s/free1_vpn",
		"https://t.me/s/UnlimitedDev",
		"https://t.me/s/vpn_xw",
		"https://t.me/s/V2RayTz",
		"https://t.me/s/ipV2Ray",
		"https://t.me/s/OutlineVpnOfficial",
		"https://t.me/s/mehrosaboran",
		"https://t.me/s/mftizi",
		"https://t.me/s/https_config_injector",
		"https://t.me/s/Hope_Net",
		"https://t.me/s/V2rayng_Fast",
		"https://t.me/s/DailyV2RY",
		"https://t.me/s/shh_proxy",
		"https://t.me/s/forwardv2ray",
		"https://t.me/s/Lockey_vpn",
]

configs = {
    "ss": "",
    "vmess": "",
    "trojan": "",
    "vless": "",
    "mixed": "",
}

myregex = {
    "vmess": r'vmess:\/\/',
    "vless": r'vless:\/\/',
}

for channel_url in channels:
    all_messages = False
    if "{all_messages}" in channel_url:
        all_messages = True
        channel_url = channel_url.split("{all_messages}")[0]

    response = requests.get(channel_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    messages = soup.select('.tgme_widget_message_wrap')
    last_message = messages[-1]['data-post'] if messages and 'data-post' in messages[-1].attrs else None

    if len(messages) < 100 and last_message:
        print(last_message)
        response = requests.get(f"{channel_url}/{last_message}")
        soup = BeautifulSoup(response.text, 'html.parser')

    if all_messages:
        for message in soup.select('.tgme_widget_message_text'):
            lines = message.get_text().split("\n")
            for line in lines:
                for proto, _ in configs.items():
                    if proto in line:
                        configs["mixed"] += f"\n{line}\n"
    else:
        for code in soup.select('code,pre'):
            lines = code.get_text().split("\n")
            for line in lines:
                for proto_regex, regex_value in myregex.items():
                    re_match = re.match(regex_value, line)
                    if re_match:
                        if proto_regex == "ss":
                            if re_match.group(1)[:3] in ["vme", "vle"]:
                                configs["vmess"] += f"\n{line}\n"
                            else:
                                configs["ss"] += f"\n{line[3:]}\n"
                        else:
                            configs[proto_regex] += f"\n{line}\n"

for proto, config_content in configs.items():
    with open(f"{proto}_iran.txt", 'w', encoding='utf-8') as file:
        file.write(config_content)
        print(f"File {proto}_iran.txt written successfully.")

