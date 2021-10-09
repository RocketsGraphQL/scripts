"backend-0001": {
	"listen": [
		":443"
	],
	"routes": [
		{
			"match": [
				{
					"host": [
						"backend-0001.rocketgraph.app"
					]
				}
			],
			"handle": [
				{
					"handler": "reverse_proxy",
					"upstreams": [
						{
							"dial":"localhost:3001"
						}
					]
				}
			]
		}
	]
}


curl -X POST \
	-H "Content-Type: application/json" \
	-d '{
            "handle": [
			                  {
				                  "handler": "subroute",
				                  "routes": [
				                    {
					                    "handle": [
					                      {
						                      "handler": "reverse_proxy",
                                  "upstreams": [
                                    {
                                      "dial": "3.139.105.219:8080"
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
			                  }
			                ],
			      "match": [
                        {
                          "host": [
                            "hasura-0012.rocketgraph.app"
                          ]
                        }
            ],
            "terminal": true
        }' \
	"http://3.22.214.239:2019/config/apps/http/servers/srv0/routes"


curl localhost:2019/load \
    -X POST \
    -H "Content-Type: application/json" \
    -d @- << EOF
    {
        "apps": {
            "http": {
                "servers": {
                    "srv": {
                        "listen": [":443"],
                    }
                }
            }
        }
    }
EOF


{
  "apps": {
    "http": {
      "servers": {
        "srv0": {
          "listen": [
            ":443"
          ],
          "routes": [
            {
              "handle": [
                {
                  "handler": "subroute",
                  "routes": [
                    {
                      "handle": [
                        {
                          "handler": "reverse_proxy",
                          "upstreams": [
                            {
                              "dial": "3.139.105.219:7000"
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "match": [
                {
                  "host": [
                    "backend-0012.rocketgraph.app"
                  ]
                }
              ],
              "terminal": true
            }
          ]
        }
      }
    }
  }
}