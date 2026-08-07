import sys
path = r'c:\Users\Jasneek\OneDrive\Desktop\Final\supplylink.html'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = lines[:3119]

content = """        const msgDiv = document.createElement('div');
        msgDiv.className = 'message';
        msgDiv.innerHTML = `
      <div class="msg-avatar av-blue">BP</div>
      <div class="msg-content">
        <div class="msg-header">
          <span class="msg-sender">bajaj.planthead@aashita.ai</span>
          <span class="msg-time">${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
        </div>
        <div class="msg-text" contenteditable="true">${this.value}</div>
      </div>
    `;
        messagesContainer.appendChild(msgDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        this.value = '';
      }
    });
  </script>

  <!-- Modal Overlay -->
  <div class="modal-overlay" id="pullTeamsModal">
    <div class="modal-content">
      <div class="modal-header">
        <h3>Invite Team Members</h3>
        <i class="fas fa-times modal-close" onclick="closePullTeamsModal()"></i>
      </div>
      <div class="modal-body">
        <div class="member-list" id="teamMembersList">
          <!-- Populated by JS -->
        </div>
      </div>
      <div class="modal-footer">
        <input type="text" id="groupNameInput" class="group-name-input" placeholder="Enter Group Name...">
        <div class="modal-actions">
          <button class="btn-outline" onclick="closePullTeamsModal()">Cancel</button>
          <button class="btn-primary" id="inviteBtn" onclick="submitPullTeams()" disabled>Invite</button>
        </div>
      </div>
    </div>
  </div>

  <script>
    // Pull Teams Modal Logic
    const teamMembers = [
      { name: "Production Head", email: "aashita.production@aashita.ai", avatar: "AP", color: "av-pink" },
      { name: "Quality Head", email: "aashita.quality@aashita.ai", avatar: "AQ", color: "av-teal" },
      { name: "Engineering", email: "bajaj.engineeringhead@aashita.ai", avatar: "BE", color: "av-green" },
      { name: "Accounts", email: "bajaj.accounts@aashita.ai", avatar: "BA", color: "av-orange" }
    ];
    let selectedMembers = new Set();

    function openPullTeamsModal() {
      const list = document.getElementById('teamMembersList');
      list.innerHTML = '';
      selectedMembers.clear();
      updateInviteUI();
      
      teamMembers.forEach((member, index) => {
        const item = document.createElement('div');
        item.className = 'member-item';
        item.onclick = () => toggleMember(item, index);
        item.innerHTML = `
          <div class="member-checkbox"><i class="fas fa-check"></i></div>
          <div class="ic-avatar ${member.color}">${member.avatar}</div>
          <div class="member-info">
            <div class="member-name">${member.name}</div>
            <div class="member-email">${member.email}</div>
          </div>
        `;
        list.appendChild(item);
      });
      document.getElementById('pullTeamsModal').classList.add('active');
    }

    function closePullTeamsModal() {
      document.getElementById('pullTeamsModal').classList.remove('active');
    }

    function toggleMember(element, index) {
      element.classList.toggle('selected');
      if (selectedMembers.has(index)) {
        selectedMembers.delete(index);
      } else {
        selectedMembers.add(index);
      }
      updateInviteUI();
    }

    function updateInviteUI() {
      const groupInput = document.getElementById('groupNameInput');
      const inviteBtn = document.getElementById('inviteBtn');
      
      if (selectedMembers.size > 1) {
        groupInput.style.display = 'block';
        inviteBtn.innerText = 'Create Group';
        inviteBtn.disabled = false;
      } else if (selectedMembers.size === 1) {
        groupInput.style.display = 'none';
        inviteBtn.innerText = 'Invite Individual';
        inviteBtn.disabled = false;
      } else {
        groupInput.style.display = 'none';
        inviteBtn.innerText = 'Invite';
        inviteBtn.disabled = true;
      }
    }

    function submitPullTeams() {
      if (selectedMembers.size > 1) {
        const groupName = document.getElementById('groupNameInput').value || 'New Group';
        alert('Created group "' + groupName + '" with ' + selectedMembers.size + ' members!');
      } else {
        const memberIdx = Array.from(selectedMembers)[0];
        alert('Invited ' + teamMembers[memberIdx].name + ' to the workspace!');
      }
      closePullTeamsModal();
    }
    document.addEventListener('click', function(e) {
      const dropdown = document.getElementById('mainReqDropdown');
      if (dropdown && dropdown.classList.contains('show') && !e.target.closest('.req-title-wrapper')) {
        dropdown.classList.remove('show');
      }
    });

    // NDA Modal Logic
    function openNdaModal() {
      document.getElementById('ndaModal').classList.add('active');
    }
    
    function closeNdaModal() {
      document.getElementById('ndaModal').classList.remove('active');
    }

    function toggleMembersList(e) {
      e.preventDefault();
      const list = document.querySelector('.members-list');
      const btn = document.getElementById('toggleMembersBtn');
      list.classList.toggle('expanded');
      if (list.classList.contains('expanded')) {
        btn.innerText = 'View Less';
      } else {
        btn.innerText = 'View All Members';
      }
    }

    // View Pulled Teams Modal Logic
    function openViewPulledTeamsModal() {
      document.getElementById('viewPulledTeamsModal').classList.add('active');
    }

    function closeViewPulledTeamsModal() {
      document.getElementById('viewPulledTeamsModal').classList.remove('active');
    }
  </script>

  <!-- NDA Modal -->
  <div class="modal-overlay" id="ndaModal">
    <div class="modal-content" style="max-width: 650px;">
      <div class="modal-header">
        <h3 contenteditable="true">NDA Status & Document Preview</h3>
        <i class="fas fa-times modal-close" onclick="closeNdaModal()"></i>
      </div>
      <div class="modal-body">
        <div style="display: flex; gap: 20px;">
          <div style="flex: 2;">
            <h4 style="margin-bottom: 10px; font-size: 13px; font-weight: 600; color: #0f172a;">Document Preview</h4>
            <div style="border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px; height: 320px; overflow-y: auto; background: #f8fafc; font-size: 11px; color: #475569; line-height: 1.6;">
              <p><strong style="color: #0f172a;">MUTUAL NON-DISCLOSURE AGREEMENT</strong></p>
              <p>This Mutual Non-Disclosure Agreement (this "Agreement") is entered into as of July 12, 2026, by and between Bajaj Auto Ltd. ("Disclosing Party") and the undersigned Supplier ("Receiving Party").</p>
              <br>
              <p><strong style="color: #0f172a;">1. Confidential Information.</strong> "Confidential Information" means any and all technical and non-technical information provided by either party to the other...</p>
              <br>
              <p><strong style="color: #0f172a;">2. Non-Use and Non-Disclosure.</strong> The Receiving Party agrees not to use any Confidential Information for any purpose except to evaluate and engage in discussions regarding the proposed business relationship.</p>
              <br>
              <p><strong style="color: #0f172a;">3. Maintenance of Confidentiality.</strong> The Receiving Party agrees that it shall take reasonable measures to protect the secrecy of and avoid disclosure and unauthorized use of the Confidential Information of the Disclosing Party.</p>
            </div>
          </div>
          <div style="flex: 1;">
            <h4 style="margin-bottom: 10px; font-size: 13px; font-weight: 600; color: #0f172a;">Signatures</h4>
            <div style="display: flex; flex-direction: column; gap: 10px;">
              <div style="display: flex; align-items: center; gap: 8px; padding: 10px; border: 1px solid #e2e8f0; border-radius: 6px; background: #fff;">
                <div class="ic-avatar av-green" style="width: 28px; height: 28px; font-size: 10px; flex-shrink: 0;">BE</div>
                <div style="min-width: 0;">
                  <div style="font-size: 11px; font-weight: 600; color: #0f172a; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">bajaj.eng...</div>
                  <div style="font-size: 10px; color: #22c55e;">Signed 12 Jul</div>
                </div>
              </div>
              <div style="display: flex; align-items: center; gap: 8px; padding: 10px; border: 1px solid #e2e8f0; border-radius: 6px; background: #fff;">
                <div class="ic-avatar av-green" style="width: 28px; height: 28px; font-size: 10px; flex-shrink: 0;">AS</div>
                <div style="min-width: 0;">
                  <div style="font-size: 11px; font-weight: 600; color: #0f172a; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">aashita.sales...</div>
                  <div style="font-size: 10px; color: #22c55e;">Signed 13 Jul</div>
                </div>
              </div>
              <div style="display: flex; align-items: center; gap: 8px; padding: 10px; border: 1px solid #e2e8f0; border-radius: 6px; background: #fff;">
                <div class="ic-avatar av-yellow" style="width: 28px; height: 28px; font-size: 10px; flex-shrink: 0;">XY</div>
                <div style="min-width: 0;">
                  <div style="font-size: 11px; font-weight: 600; color: #0f172a; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">xyz.sales...</div>
                  <div style="font-size: 10px; color: #eab308;">Viewed 13 Jul</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- View Pulled Teams Modal -->
  <div class="modal-overlay" id="viewPulledTeamsModal">
    <div class="modal-content" style="max-width: 450px;">
      <div class="modal-header">
        <h3 contenteditable="true">Pulled Teams</h3>
        <i class="fas fa-times modal-close" onclick="closeViewPulledTeamsModal()"></i>
      </div>
      <div class="modal-body">
        <p style="font-size: 13px; color: #64748b; margin-bottom: 16px;">The following internal teams have been pulled into this workspace.</p>
        <div class="member-list">
          <div class="member-item selected" style="cursor: default;">
            <div class="ic-avatar av-pink">AP</div>
            <div class="member-info">
              <div class="member-name">Production Head</div>
              <div class="member-email">aashita.production@aashita.ai</div>
            </div>
          </div>
          <div class="member-item selected" style="cursor: default;">
            <div class="ic-avatar av-teal">AQ</div>
            <div class="member-info">
              <div class="member-name">Quality Head</div>
              <div class="member-email">aashita.quality@aashita.ai</div>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <div class="modal-actions" style="margin-left: 0; width: 100%;">
          <button class="btn-primary" style="width: 100%;" onclick="closeViewPulledTeamsModal()">Close</button>
        </div>
      </div>
    </div>
  </div>
</body>

</html>
"""

new_lines.append(content)
with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
