ALTER TABLE `mailbox_insert_queue` ADD COLUMN `item_id2` INT(30) DEFAULT '0' NOT NULL AFTER `item_stack`, ADD COLUMN `item_stack2` INT(30) DEFAULT '0' NOT NULL AFTER `item_id2`;
ALTER TABLE `mailbox_insert_queue` ADD COLUMN `item_id3` INT(30) DEFAULT '0' NOT NULL AFTER `item_stack2`, ADD COLUMN `item_stack3` INT(30) DEFAULT '0' NOT NULL AFTER `item_id3`;
ALTER TABLE `mailbox_insert_queue` ADD COLUMN `item_id4` INT(30) DEFAULT '0' NOT NULL AFTER `item_stack3`, ADD COLUMN `item_stack4` INT(30) DEFAULT '0' NOT NULL AFTER `item_id4`;
ALTER TABLE `mailbox_insert_queue` ADD COLUMN `item_id5` INT(30) DEFAULT '0' NOT NULL AFTER `item_stack4`, ADD COLUMN `item_stack5` INT(30) DEFAULT '0' NOT NULL AFTER `item_id5`;
ALTER TABLE `mailbox_insert_queue` ADD COLUMN `item_id6` INT(30) DEFAULT '0' NOT NULL AFTER `item_stack5`, ADD COLUMN `item_stack6` INT(30) DEFAULT '0' NOT NULL AFTER `item_id6`;
ALTER TABLE `mailbox_insert_queue` ADD COLUMN `item_id7` INT(30) DEFAULT '0' NOT NULL AFTER `item_stack6`, ADD COLUMN `item_stack7` INT(30) DEFAULT '0' NOT NULL AFTER `item_id7`;
ALTER TABLE `mailbox_insert_queue` ADD COLUMN `item_id8` INT(30) DEFAULT '0' NOT NULL AFTER `item_stack7`, ADD COLUMN `item_stack8` INT(30) DEFAULT '0' NOT NULL AFTER `item_id8`;
ALTER TABLE `mailbox_insert_queue` ADD COLUMN `item_id9` INT(30) DEFAULT '0' NOT NULL AFTER `item_stack8`, ADD COLUMN `item_stack9` INT(30) DEFAULT '0' NOT NULL AFTER `item_id9`;
ALTER TABLE `mailbox_insert_queue` ADD COLUMN `item_id10` INT(30) DEFAULT '0' NOT NULL AFTER `item_stack9`, ADD COLUMN `item_stack10` INT(30) DEFAULT '0' NOT NULL AFTER `item_id10`;
ALTER TABLE `mailbox_insert_queue` ADD COLUMN `item_id11` INT(30) DEFAULT '0' NOT NULL AFTER `item_stack10`, ADD COLUMN `item_stack11` INT(30) DEFAULT '0' NOT NULL AFTER `item_id11`;
ALTER TABLE `mailbox_insert_queue` ADD COLUMN `item_id12` INT(30) DEFAULT '0' NOT NULL AFTER `item_stack11`, ADD COLUMN `item_stack12` INT(30) DEFAULT '0' NOT NULL AFTER `item_id12`;
UPDATE `arcemu_db_version` SET `LastUpdate` = '4636';