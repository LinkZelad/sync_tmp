return function()
	require("Trans").setup({
		theme = "dracula",
		strategy = {
			default = {
				frontend = "hover",
				backend = "*",
			},
		},
		frontend = {
			default = {
				auto_play = false,
			},
			hover = {
				keymaps = {
					vim.keymap.set("n", "ti", "<Cmd>TranslateInput<CR>"),
					vim.keymap.set({ "n", "x" }, "tm", "<Cmd>Translate<CR>"),
					vim.keymap.set({ "n", "x" }, "tk", "<Cmd>TransPlay<CR>"),
				},
				order = {
					default = {
						"str",
						"translation",
						"definition",
					},
					offline = {
						"title",
						"tag",
						"pos",
						"exchange",
						"translation",
						"definition",
					},
					baidu = {
						"title",
						"translation",
						"definition",
						"web",
					},
				},
			},
		},
	})
end
