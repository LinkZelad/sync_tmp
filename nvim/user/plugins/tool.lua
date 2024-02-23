local custom = {}

custom["Exafunction/codeium.vim"] = {
	event = "Bufenter",
	config = require("configs.tool.codeium"),
}

custom["JuanZoran/Trans.nvim"] = {
	build = function()
		require("Trans").install()
	end,
	dependencies = { "kkharji/sqlite.lua" },
	config = require("configs.tool.trans"),
}

custom["akinsho/flutter-tools.nvim"] = {
	lazy = false,
	dependencies = {
		"nvim-lua/plenary.nvim",
		"stevearc/dressing.nvim", -- optional for vim.ui.select
	},
	config = require("configs.tool.flutter-tools"),
}

-- custom["nvim-telescope/telescope-file-browser.nvim"] = {
-- 	dependencies = {
-- 		"nvim-telescope/telescope.nvim",
-- 		"nvim-lua/plenary.nvim",
-- 	},
-- 	config = require("configs.tool.file-browser"),
-- }

custom["tadachs/ros-nvim"] = {
	lazy = true,
	event = "CmdlineEnter",
	config = require("configs.tool.ros-nvim"),
	dependencies = {
		"nvim-lua/plenary.nvim",
	},
}

custom["Shatur/neovim-cmake"] = {
	lazy = true,
	event = "CmdlineEnter",
	config = require("configs.tool.neovim-cmake"),
	dependencies = {
		{ "nvim-lua/plenary.nvim" },
	},
}

custom["Bryley/neoai.nvim"] = {
	dependencies = {
		"MunifTanjim/nui.nvim",
	},
	cmd = {
		"NeoAI",
		"NeoAIOpen",
		"NeoAIClose",
		"NeoAIToggle",
		"NeoAIContext",
		"NeoAIContextOpen",
		"NeoAIContextClose",
		"NeoAIInject",
		"NeoAIInjectCode",
		"NeoAIInjectContext",
		"NeoAIInjectContextCode",
	},
	keys = {
		{ "<leader>as", desc = "summarize text" },
		{ "<leader>ag", desc = "generate git message" },
	},
	config = require("configs.tool.neoai"),
}

-- custom["jackMort/ChatGPT.nvim"] = {
-- 	event = "VeryLazy",
-- 	config = require("configs.tool.chatgpt"),
-- 	dependencies = {
-- 		"MunifTanjim/nui.nvim",
-- 		"nvim-lua/plenary.nvim",
-- 		"nvim-telescope/telescope.nvim",
-- 	},
-- }

return custom
