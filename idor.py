#!/usr/bin/env python3
# TBH-IDOR - Detector (Educational - Check IDOR via ID increment)
import requests, argparse, json, re

BANNER = """\033[91m╔════════════════════════════════════╗
\033[91m║ \033[97mTBH-IDOR \033[91m- Detector               \033[91m║
\033[91m║ \033[90mTulungagung Black Hat | uchil404 \033[91m║
\033[91m╚════════════════════════════════════╝\033[0m"""

def check(url):
    # Try increment ID param
    m=re.search(r"(\?|&)(id|user|account|profile)=(\d+)", url)
    results=[]
    if m:
        param=m.group(2); orig_id=m.group(3)
        for test_id in [str(int(orig_id)+1), str(int(orig_id)-1), "1"]:
            test_url=url.replace(f"{param}={orig_id}", f"{param}={test_id}")
            try:
                r=requests.get(test_url,timeout=5,headers={'User-Agent':'TBH-IDOR/1.0'})
                # Simple heuristic: if 200 and content length similar but not same
                results.append({"test_id":test_id,"url":test_url,"status":r.status_code,"length":len(r.content),"potential":r.status_code==200})
            except: results.append({"test_id":test_id,"error":True})
    else:
        # No ID param, try add
        test_url=url + ("&" if "?" in url else "?") + "id=1"
        try:
            r=requests.get(test_url,timeout=5)
            results.append({"test_id":"1","url":test_url,"status":r.status_code,"potential":r.status_code==200})
        except: pass
    return results

def main():
    print(BANNER)
    print("\033[91m[!] Hanya untuk scope yang diizinkan! Test IDOR dengan akun sendiri!\033[0m\n")
    parser=argparse.ArgumentParser(description="IDOR")
    parser.add_argument("-u","--url",required=True,help="URL dengan ?id=")
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    print(f"[*] Testing {args.url} untuk IDOR (increment ID)")
    results=check(args.url)
    for r in results:
        if r.get("potential"): print(f"\033[93m[?] {r['test_id']} -> {r['status']} {r['url'][:60]} - cek manual! Apakah data berubah?\033[0m")
        else: print(f"\033[90m[-] {r['test_id']} -> {r.get('status','err')}\033[0m")
    print("-> Jika test_id=2 menampilkan data user lain, potensi IDOR High!")
    if args.json:
        open(args.json,'w').write(json.dumps(results,indent=2)); print(f"[✓] JSON: {args.json}")

if __name__=="__main__": main()
