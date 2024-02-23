local custom = {}

custom["Mofiqul/dracula.nvim"] = {
	lazy = false,
	config = require("configs.ui.dracula"),
}

-- custom["goolord/alpha-nvim"] = {
-- 	enable = false,
-- 	config = require("configs.ui.alpha"),
-- }

custom["zorbn/rider-dark.nvim"] = {
	lazy = false,
	-- config = require("configs.ui.rider-dark"),
}

return custom
