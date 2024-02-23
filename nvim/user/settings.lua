-- Please check `lua/core/settings.lua` to view the full list of configurable settings
local settings = {}

-- Examples
settings["use_ssh"] = true

-- settings["colorscheme"] = "rider-dark"
settings["colorscheme"] = "dracula"

settings["null_ls_deps"] = function(defaults)
	return {
		-- defaults[1],
		-- defaults[4],
		-- defaults[5],
		-- defaults[6],
		-- defaults[7],
	}
end

settings["dashboard_image"] = function(defaults)
	return {
		[[___________________         ______                ]],
		[[< GOOD GOOD STUDY! >       / DAY \                ]],
		[[ -------------------      |      |                ]],
		[[    \                     \  DAY |                ]],
		[[     \  /\/\              /      |                ]],
		[[       \   /             |   UP  |                ]],
		[[       |  0 >>           \       |                ]],
		[[       |___|              \ !!!!/                 ]],
		[[ __((_<|   |              -------                 ]],
		[[(          |                  \   ^__^            ]],
		[[(__________)                   \  (oo)\______     ]],
		[[   |      |                       (__)\       )\/\]],
		[[   |      |                           ||----w |   ]],
		[[  /\     /\     007                   ||     ||   ]],
	}
end

return settings
