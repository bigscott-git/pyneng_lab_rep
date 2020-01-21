#!/usr/bin/env python3

import json
from pprint import pprint

with open('exported_data.xml', 'r') as source, open('fw_result.txt', 'w') as dest:
        dict = {}
        for lines in source:
                if '<rule_entry comment' in lines:
                        pass
                elif 'tag=' in lines and '<rule_entry' in lines:
                        policy = lines[lines.index('tag=') + 5 : lines.index('>') - 3]
                        dict[policy] = {}
                elif '<match_source_ref' in lines:
                        dict[policy]['srcaddr'] = lines[lines.index('value="') + 7 : lines.index('"/>')]
                elif '<match_destination_ref' in lines:
                        dict[policy]['dstaddr'] = lines[lines.index('value="') + 7 : lines.index('"/>')]
                elif '<match_service_ref' in lines:
                        dict[policy]['service'] = lines[lines.index('value="') + 7 : lines.index('"/>')]
                elif '<action type=' in lines:
                        dict[policy]['action'] = lines[lines.index('type="') + 6 : lines.index('"/>')]
                               
        dest.write(json.dumps(dict))
        pprint(json.dumps(dict))

